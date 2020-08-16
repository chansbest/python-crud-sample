"""
This file reads the csv file data and creates sqllite database file with it,
if exiting file is found then it is removed first
"""

from sqlalchemy import *

import pandas as pd
import os

if os.path.isfile('covid.sqllite'):
    print('deleting file')
    os.remove("covid.sqllite")

engine = create_engine('sqlite:///covid.sqllite',echo=False)
sqlite_connection = engine.connect()

print('reading csv')
data = pd.read_csv('us-states.csv')
data = data.rename(columns={"date": "record_date"})

print('writing to sqllite file')

sqlite_table = "us_states"
data.to_sql(sqlite_table, sqlite_connection, if_exists='fail',index_label='id')
print('done')







