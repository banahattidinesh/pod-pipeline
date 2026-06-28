import pandas as pd
from sqlalchemy import create_engine

# 1. Connect to the database (use your exact connection string)
engine = create_engine('postgresql://postgres:dinesh123@localhost:5433/dataengg_db')

# 2. Write your SQL query as a string
sql_query ="SELECT \"userId\", \"totalProducts\" FROM cleaned_pod_orders WHERE \"userId\" > 2"

# 3. Pull the data directly into a DataFrame
df_result = pd.read_sql(sql_query, engine)

print("Query Results (Orders with more than 3 products):")
print(df_result)