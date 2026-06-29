import os

import requests
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

url = "https://dummyjson.com/carts"
data = requests.get(url).json()
df = pd.DataFrame(data['carts'])
df = df[['id', 'userId', 'totalProducts']]


load_dotenv()
password = os.getenv("DB_PASSWORD") 



# YOUR CHALLENGE STARTS HERE!

engine = create_engine(f'postgresql://postgres:{password}@localhost:5433/dataengg_db')

print(f"Success connecting to the database! with password starting with {password[:2]}")


df.to_sql('cleaned_pod_orders', engine, if_exists='replace', index=False)  

print("Example successful: 'cleaned_pod_orders' created!")