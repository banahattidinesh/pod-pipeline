import requests
import pandas as pd

# 1. Get a larger chunk of data so we have overlapping users
url = "https://dummyjson.com/carts"
data = requests.get(url, params={"limit": 50}).json()
df = pd.DataFrame(data['carts'])

# 2. Group the data by 'userId' and SUM the 'totalProducts'
# reset_index() just keeps it as a clean dataframe instead of a weird list
summary_df = df.groupby('userId')['totalProducts'].mean().reset_index()

# 3. Rename the column so the business team knows what it is
summary_df = summary_df.rename(columns={'totalProducts': 'average_cart_size'})

print("Total Products Ordered By Each User:")
print(summary_df.head()) # .head() just prints the first 5 rows to keep the terminal clean