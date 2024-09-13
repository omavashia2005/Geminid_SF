import pandas as pd
import requests
# converts pandas data frame to json array

df = pd.read_csv("/Users/omavashia/Downloads/Test Accounts - Sheet2.csv")
jsonArray = df.head().to_json(orient='records')
print(jsonArray)

# generates response (200) from the given url using given credentials using HTTP get through the request library
response = requests.get('https://geminidsystems4-dev-ed.develop.my.salesforce.com', headers={'Authroization':'access_token admin@geminidsystems.com.om'})

# upserting
instance_url = "https://geminidsystems4-dev-ed.develop.my.salesforce.com"

