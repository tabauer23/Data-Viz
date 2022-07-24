import requests

HOST = "https://api.census.gov/data"
year = "2020"
dataset = "dec/sf1"

base_url = "/".join([HOST, year, dataset])

predicates = {}
get_vars = ["NAME", "GEO_ID", "P001001"]
predicates["get"] = ",".join(get_vars)
predicates["for"] = "state:33"
r = requests.get(base_url, params=predicates)

#print(r.text)

print(r.json()[0])

col_names = ["name", "GEO_ID", "total_pop", "state"]

import pandas as pd

df = pd.DataFrame(columns=col_names, data=r.json()[1:])

#Fix data types
df["total_pop"] = df["total_pop"].astype(int)

print(df.head())