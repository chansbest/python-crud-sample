from typing import Optional
from sql import us_states_dao,sqlconnection,StateRecord,StateRecordBase,StateRecordResponse
from fastapi import FastAPI,Response,status
import logging

logging.basicConfig(filename='log.log',level=logging.DEBUG)
app = FastAPI()

"""
This is application entry point, all end points/controllers/routes are defined in this file.
"""

@app.get("/staterecords/")
def read(response: Response,start: Optional[int] = 0 , count: Optional[int] = 10 ,):
    rs = us_states_dao().read()
    message = ''
    if rs and start  >= len(rs):
        message = "start index(start) cannot be >= length of records"
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        rs = None
    elif rs:
        rs = rs[start:(start+count)]

    return {"records": rs , "message":message}

@app.post("/staterecord", response_model=StateRecord, status_code=201)
def create(payload: StateRecordBase):
    response_object = us_states_dao().insert(payload)

    return response_object

@app.put("/staterecord/{id}", response_model=StateRecordResponse, status_code=201)
def update(id: int ,payload: StateRecordBase,response: Response):
    response_object,result = us_states_dao().update(id,payload)
    if result == 2:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        response_object = {"message":"item not found in database"}
    
    elif result == 0:
        response.status_code = status.HTTP_200_OK
        response_object = {"message":"success","modifiedRecord":payload}

    else :
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        response_object = {"message":"unknown error"}
    
    return response_object

@app.delete("/staterecord/{id}", status_code=201)
def delete(id: int ,response: Response):
    result = us_states_dao().delete(id)
    response_object = {}
    if result == 2:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        response_object = {"message":"item not found in database"}
    
    elif result == 0:
        response.status_code = status.HTTP_200_OK
        response_object = {"message":"success"}

    else:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        response_object = {"message":"unknown error"}
    
    return response_object