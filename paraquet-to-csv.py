import pandas as pd
import sys

# Usage: python3 paraquet-to-csv.py file.paraquet

parquet_file = sys.argv[1]

pd.set_option('display.max_rows', 50000)
pd.set_option('display.max_columns', 50000)
pd.set_option('display.width', 15000000)
pd.set_option('display.max_colwidth', -1)

df = pd.read_parquet(str(parquet_file),engine='auto')
df.to_csv(str(parquet_file)+".csv")
#print(df)
