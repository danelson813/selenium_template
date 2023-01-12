import pandas as pd

# read a feather file into a database
df = pd.read_feather('data.feather')

# Write a DataFrame to a Feather  file
df.to_feather('data.feather')

# Write a DataFrame to a compressed Parquet file
# can use gzip, snappy and brotli
df.to_parquet('data.parquet', compressiom='gzip', index=False)

# customize the schema of a Parquet file
# Define the schema
schema = {'name': "string", 'age': 'int32'}

#Write a DataFrame to a Parquet file with a custom schema
df.to_parquet('data.parquet', schema=schema, index=False)
