from fastapi.testclient import TestClient
from main import app
import pytest
from sql import us_states_dao
import pytest
from fastapi.testclient import TestClient
import json



@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client 


def test_read_all_states(test_app, monkeypatch):
     # basic sanity read
    response = test_app.get("/staterecords")
    assert response.status_code == 200

def test_read_all_states_invalidstart_1(test_app, monkeypatch):
    # test if start index is grater than total number of records by passing a very high number
    response = test_app.get("/staterecords?start=10000000")
    assert response.status_code == 422

def test_read_all_states_invalidstart_2(test_app, monkeypatch):
    # test by passing start index as string
    response = test_app.get("/staterecords?start=abc")
    assert response.status_code == 422

def test_read_0_records_in_db(test_app, monkeypatch):
    # test api to handle , if 0 records returned from database by mocking service
    def mock_get(self):
        return []
    monkeypatch.setattr(us_states_dao, "read", mock_get)
    response = test_app.get("/staterecords")
    assert response.status_code == 200    


def test_add_basic(test_app, monkeypatch):
     # basic sanity read
    test_request_payload = {
    "record_date": "2020-08-16",
    "state": "Maha",
    "fips": 0,
    "cases": 0,
    "deaths": 0,
    "confirmed_cases": 0,
    "confirmed_deaths": 0,
    "probable_cases": 0,
    "probable_deaths": 0
    }
    response = test_app.post("/staterecord", json=test_request_payload)
    assert response.status_code == 201

def test_add_basic_fail(test_app, monkeypatch):
     # basic sanity add fail invalid json without mandatory fields
    test_invalid_payload = {
    "fips": 0,
    "cases": 0,
    "deaths": 0,
    "confirmed_cases": 0,
    "confirmed_deaths": 0,
    "probable_cases": 0,
    "probable_deaths": 0
}
    response = test_app.post("/staterecord", json = test_invalid_payload)
    assert response.status_code == 422


def test_del_basic(test_app, monkeypatch):
     # basic sanity read
    def mock_del(self,id):
        return 0
    monkeypatch.setattr(us_states_dao, "delete", mock_del)
    response = test_app.delete("/staterecord/56")
    assert response.status_code == 200

def test_del_fail(test_app, monkeypatch):
     # basic sanity read
    def mock_del(self,id):
        return 1
    monkeypatch.setattr(us_states_dao, "delete", mock_del)
    response = test_app.delete("/staterecord/56")
    assert response.status_code == 500


def test_update_basic(test_app, monkeypatch):
     # basic sanity update by mock update
    test_request_payload = {
    "record_date": "2020-08-16",
    "state": "Maha",
    "fips": 0,
    "cases": 0,
    "deaths": 0,
    "confirmed_cases": 0,
    "confirmed_deaths": 0,
    "probable_cases": 0,
    "probable_deaths": 0
    }
    def mock_up(self,id,payload):
        return payload,0
    monkeypatch.setattr(us_states_dao, "update", mock_up)
    response = test_app.put("/staterecord/56",json = test_request_payload)
    assert response.status_code == 200

def test_update_fail(test_app, monkeypatch):
    test_request_payload = {
    "record_date": "2020-08-16",
    "state": "Maha",
    "fips": 0,
    "cases": 0,
    "deaths": 0,
    "confirmed_cases": 0,
    "confirmed_deaths": 0,
    "probable_cases": 0,
    "probable_deaths": 0
    }
     # basic sanity update fail by mock update
    def mock_up(self,id,payload):
        return None,1
    monkeypatch.setattr(us_states_dao, "update", mock_up)
    response = test_app.put("/staterecord/56",json = test_request_payload)
    assert response.status_code == 500



