import requests
import pandas as pd

# 1. EXTRACT (Going back to pulling all carts so we have a real table)
url = "https://dummyjson.com/carts"
data = requests.get(url).json()

# 2. CLEAN (Convert the list of carts into a pandas DataFrame)
df = pd.DataFrame(data['carts'])
df = df[['id',  'userId', 'totalProducts']]


# Print the first 5 rows of our new table
print("Raw Table Data:")    
print(df.head(3))