import pandas as pd
import pathlib
import json

path = pathlib.Path(__file__).parent.parent.joinpath("output/income_statement/incomeStatement.json")

print(path)
with open(path) as fileData:
    data = json.load(fileData)

df = pd.json_normalize(data["annualReports"])
print(df)