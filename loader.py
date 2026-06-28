import requests
import pandas as pd
from sqlalchemy import create_engine

url = "https://dummyjson.com/carts"
data = requests.get(url).json()
df = pd.DataFrame(data['carts'])
df = df[['id', 'userId', 'totalProducts']]

# YOUR CHALLENGE STARTS HERE!

engine = create_engine('postgresql://postgres:dinesh123@localhost:5433/dataengg_db')

df.to_sql('cleaned_pod_orders', engine, if_exists='replace', index=False)  

print("Example successful: 'cleaned_pod_orders' created!")