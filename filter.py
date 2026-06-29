import requests

url = "https://dummyjson.com/carts"

# The API reads these parameters to slice the data
my_filters = {
    "limit": 2,
    "skip": 10
}

# Pass the dictionary to the 'params' argument
response = requests.get(url, params=my_filters)
data = response.json()

print(f"Total carts pulled: {len(data['carts'])}")
print(f"First cart ID in this batch: {data['carts'][0]['id']}")