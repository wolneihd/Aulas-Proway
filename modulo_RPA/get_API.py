import requests

url = 'https://fakestoreapi.com/products'

# GET
response = requests.get(url)
data = response.json()
print('get', data)

# POST
data = {
    "title": "teste",
    "price": 100.00,
    "description": "teste",
    "category": "teste",
    "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg",
    "rating": {
      "rate": 3.9,
      "count": 120
    }
  }
response = requests.post(url=url, data=data)
print('post', response)

# PUT
id = 1
response = requests.put(f'{url}/{id}', data=data)
print('put', response)

# PUT
id = 1
response = requests.delete(f'{url}/{id}')
print('delete', response)