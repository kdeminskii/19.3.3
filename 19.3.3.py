import requests

# метод POST:
url = 'https://petstore.swagger.io/v2/pet'

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

data = {
    "id": 0,
    "category": {
        "id": 0,
        "name": "string"
    },
    "name": "doggie",
    "photoUrls": ["string"],
    "tags": [
        {
            "id": 0,
            "name": "string"
        }
    ],
    "status": "available"
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.text)
print(response.json())


#метод PUT:
url = 'https://petstore.swagger.io/v2/pet'
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

data = {
    "id": 9223372036854602804,
    "username": "string",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 0
}

response = requests.put(url, headers=headers, json=data)

print(response.status_code)
print(response.json())



#метод GET:
petID = 9223372036854602804
url = f'https://petstore.swagger.io/v2/pet/{petID}'
headers = {'accept': 'application/json'}
data = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

response = requests.get(url, headers=headers, json=data)

print(response.status_code)
print(response.json())


# метод DELETE:
petID = 9223372036854602804
url = f'https://petstore.swagger.io/v2/pet/{petID}'
headers = {'accept': 'application/json'}
response = requests.delete(f'https://petstore.swagger.io/v2/pet/{petID}', headers=headers)

print(response.status_code)
print(response.json())