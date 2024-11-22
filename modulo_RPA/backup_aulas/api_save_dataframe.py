import pandas as pd
import requests

url = 'https://fakestoreapi.com/products'

# pegar dados
def get_api_data():
    response = requests.get(url)
    data = response.json()
    return data

data = get_api_data()
df = pd.DataFrame(data=data)
df.to_csv('dados_api.csv', index=False)
print(df.head())

