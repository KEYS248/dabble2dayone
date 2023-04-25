import argparse
import json
import dateutil.parser
from dateutil.relativedelta import relativedelta

parser = argparse.ArgumentParser(
    description="""Convert Dabble JSON file into Day One JSON file.
    If for Journey App, you will need to zip and rename exported Day One JSON as shown here: https://help.journey.cloud/en/article/import-day-one-spkats/""")
parser.add_argument('--dabble', required=True, help="input file in the Dabble JSON format")
parser.add_argument('--dayone', required=True, help="output file in the Day One JSON format")
args = parser.parse_args()

f = open(args.dabble, "r")
dabble_data = json.load(f)
f.close()

dayone_meta = {}
dayone_meta["version"] = "1.0"

dayone_entries = []
for dabble_entry in dabble_data:
    dayone_entry = {}
    dayone_entry['creationDate'] = str(dateutil.parser.isoparse(dabble_entry['date']) + relativedelta(days = 1))
    dayone_entry['text'] = dabble_entry['body']
    dayone_entries.append(dayone_entry)
    
dayone_data = {}
dayone_data['metadata'] = dayone_meta
dayone_data['entries'] = dayone_entries
dayone = json.dumps(dayone_data, indent = 2)

f = open(args.dayone, "w")
f.write(dayone)
f.close()