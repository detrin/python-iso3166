import requests
import sys
from iso3166 import _records

repository_numeric = []
for country in _records:
    repository_numeric.append(country.numeric)
repository_numeric.sort()

response = requests.get('https://raw.githubusercontent.com/detrin/download-iso3166-list/main/countries.json')
records_outside = response.json()

outside_numeric = []
for d in records_outside:
    outside_numeric.append(d["Numeric"])
outside_numeric.sort()

extra = set(repository_numeric) - set(outside_numeric)
if extra:
    print("Extra in repository: ", extra)

missing = set(outside_numeric) - set(repository_numeric)
if missing:
    print("Missing in repository: ", missing)

if extra or missing:
    sys.exit(1)