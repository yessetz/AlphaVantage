import pandas as pd
import pathlib
import json

path = pathlib.Path(__file__).parent.parent.joinpath("output/income_statement/incomeStatement.json")

print(path)
with open(path) as fileData:
    data = json.load(fileData)

df = pd.json_normalize(data["annualReports"])
print(df)










import pathlib

companySymbol = "IBM"

path = pathlib.Path(__file__).parent.parent.joinpath("keys/data.json")
print(path) 

with open(path) as keys:
    keys = json.load(keys)

key = keys["accounts"][0]["key"]

df = getListingStatus(key)

outputPath = pathlib.Path(__file__).parent.parent.joinpath("output/income_statement/listingStatus.json")

with open(outputPath, "w", newline="", encoding="utf-8") as csvdata:
with open('thefile.csv', 'rb') as f:
  data = list(csv.reader(f))

import collections
counter = collections.defaultdict(int)
for row in data:
    counter[row[0]] += 1


writer = csv.writer(open("/path/to/my/csv/file", 'w'))
for row in data:
    if counter[row[0]] >= 4:
        writer.writerow(row)



#with open(outputPath, "w", encoding="utf-8") as f:
#    json.dump(df, f)
