from typing import Optional
from pydantic import BaseModel
from datetime import date
from sqlalchemy import (Column, DateTime, Integer, MetaData, String, Table,DATE,
                        create_engine)



us_states_table = Table(
    "us_states",
    MetaData(),
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


class StateRecordBase(BaseModel):
    record_date: date
    state:str
    fips: Optional[int]
    cases: Optional[int]
    deaths: Optional[int]
    confirmed_cases: Optional[int]
    confirmed_deaths: Optional[int]
    probable_cases: Optional[int]
    probable_deaths: Optional[int]



class StateRecord(StateRecordBase):
    id: int

    def addBaseRecord(self,baserecord : StateRecordBase):
            self.record_date: baserecord.record_date
            self.state = baserecord.state
            self.fips = baserecord.fips
            self.cases = baserecord.cases
            self.deaths = baserecord.deaths
            self.confirmed_cases = baserecord.confirmed_cases
            self.confirmed_deaths = baserecord.confirmed_deaths
            self.probable_cases = baserecord.probable_cases
            self.probable_deaths = baserecord.probable_deaths

    class Config:
        orm_mode = True


class StateRecordResponse(BaseModel):
    message: Optional[str]
    modifiedRecord: Optional[StateRecordBase]


