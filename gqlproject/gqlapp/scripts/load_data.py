import sqlite3
import pandas as pd

# connect to the db
conn = sqlite3.connect('db.sqlite3')
# read file
df = pd.read_csv('../sam.csv')

# data to read has no id column so let us add one here
df['id'] = df.index
# re-organiza the data
df = df[['id', 'Segment', 'Country', 'Product', 'Units', 'Sales', 'Datesold']]
# load data into the database table
# if_exists: when we run this again and data exists, lets replace it
# index=False, we dont want to write the index again
df.to_sql('gqlapp_productmodel', conn, if_exists='replace', index=False)
