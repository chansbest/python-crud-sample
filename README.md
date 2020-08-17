# python crud sample


## installation 
### Prerequisites:
 Python 3.8 ( should probably work fine 3.6+)<br>
 git<br>

### Steps
step 1: <br>
clone repository to local drive <br>
`git clone https://github.com/chansbest/python-crud-sample.git`

step 2: move into python-crud-sample directory and create python enviroment named env to run all. <br>
`cd python-crud-sample` <br>
`python3 -m venv env`  <br>
alternatively `python -m venv env`  <br>



step 3: activate enviroment
on windows<br>
`env\Scripts\activate`<br>
on linux<br>
`source env\bin\activate`<br>


step 4 : install dependencies <br>
`pip install -r requirements.txt` <br>

![creating env!](/assets/images/env_creation.JPG  "creating env")

step 5 (optional):
initialize sqllite dataset by running sqllite.py,<br>
this will create a new sqllite file and insert records from us-states.csv file.<br>
exiting sqllite file already contains data so this step is optional.<br>

`python3 sqllite.py`<br>
![creating sqllite!](/assets/images/sqllite.JPG  "sqllite")

step 6: move into api directory<br>
`cd app`

step 7: (optional)  run test cases for api<br>
'pytest'<br>
![test cases!](/assets/images/testcases.JPG  "test cases")

step 8: start rest api in server<br>
 'uvicorn main:app --host 0.0.0.0'<br>
![run api!](/assets/images/runningapi.JPG  "run api")


you can try out api on browser by going to <br>
http://localhost:8000/docs
![try!](/assets/images/trying.JPG  "try")


