import re

"""

ISO codes can be in the form:

- ISO 3004: Foobar some stuff
- ISO/IEC 8012: Barfoo other things
- ISO/IEC TRS 55401: Wobble gizmos

"""
regexp = re.compile("(ISO(?:/[A-Z]+)? .*?)[:\s]\d*(.*)")

from requests_html import HTMLSession
session = HTMLSession()
r = session.get('https://en.everybodywiki.com/List_of_ISO_standards')

# Extract all elements from lists
li_tags = r.html.find('.mw-parser-output ul > li')
# Magic numbers to remove everything that is not in the main article
iso_tags = (t.text for t in li_tags[36:-471])
iso_tags = map(regexp.findall, iso_tags)
iso_tags = filter(lambda x: len(x) > 0, iso_tags)
# Get pairs of (ISO code, title)
tags = []
for t in iso_tags:
    tags += t

# Build dict (ISO code -> titles)
# titles can consist in several parts separated by a newline
iso_dict = {}
for k, v in tags:
    try:
        k = re.findall('(ISO(?:/[A-Z\s]+)? \d+).*', k)[0]
    except IndexError:
        print(f"Weird format: {k}")
    if k in iso_dict.keys():
        iso_dict[k] += '\n' + v.strip()
    else:
        iso_dict[k] = v.strip()
        
# Give a sample
import random
print(random.choice(list(iso_dict.items())))


# Write result in CSV file
import csv
csv_columns = ['Code', 'Title']
csv_file = "iso_standards.csv"
with open(csv_file, 'w') as f:
    w = csv.writer(f)
    w.writerow(csv_columns)
    w.writerows(iso_dict.items())

# Write result in JSON file
import json
with open("iso_standards.json", 'w') as f:
    json.dump(iso_dict, f)

