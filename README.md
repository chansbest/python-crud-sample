# python crud sample


##installation 
###Prerequisites:
Python 3.8 ( should probably work fine 3.6+)
git

###Steps
step 1:
clone repository to local drive
git clone https://github.com/chansbest/python-crud-sample.git

step 2: move into python-crud-sample directory and create python enviroment named env to run all.
cd python-crud-sample
python3 -m venv env 
alternatively python -m venv env 

step 3 : install dependencies
pip install -r requirements.txt

step 4: activate enviroment
on windows
env\Scripts\activate
on linux
source env\bin\activate

step 5 (optional):
initialize sqllite dataset by running sqllite.py,
this will create a new sqllite file and insert records from us-states.csv file.exiting sqllite file already contains data so this step is optional.

python3 sqllite.py


step 6: move into api directory
cd app

step 7: (optional)  run test cases for api
pytest

step 8: start rest api in server
 uvicorn main:app --host 0.0.0.0

you can try out api on 
http://localhost:8000/docs

