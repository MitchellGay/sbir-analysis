import requests
import pandas as pd
import json

url = "https://api.www.sbir.gov/public/api/awards"

response = requests.get(url)
data = response.json()

df = pd.DataFrame(data)

columns = ["firm", "award_title", "agency", "award_year", "award_amount", "abstract"]
df = df[columns]

df.to_csv("sbir_sample_awards.csv", index=False)

print("Saved 10 awards to 'sbir_sample_awards.csv'")
print(df.head())
