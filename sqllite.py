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
meta = MetaData()

print('creating table')
us_states_table = Table(
    "us_states",
    meta,
    Column("id", Integer, primary_key=True),
    Column("state", String(50),nullable=False),
    Column("record_date", DATE, nullable=False),
    Column("fips", Integer, nullable=True),
    Column("cases", Integer, nullable=True),
    Column("deaths", Integer, nullable=True),
    Column("confirmed_cases", Integer, nullable=True),
    Column("confirmed_deaths", Integer, nullable=True),
    Column("probable_cases", Integer, nullable=True),
    Column("probable_deaths", Integer, nullable=True),
    sqlite_autoincrement=True
)
meta.create_all(engine)

print('reading csv')
data = pd.read_csv('us-states.csv')
data = data.rename(columns={"date": "record_date"})

print('writing to sqllite file')

sqlite_table = "us_states"
data.to_sql(sqlite_table, sqlite_connection,if_exists='append',index_label='id')
print('done')







