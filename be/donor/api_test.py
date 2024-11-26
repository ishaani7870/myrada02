import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from dotenv import dotenv_values
from pymongo import MongoClient
from be.main import app

config = dotenv_values(".env")
app.database = app.mongodb_client["DB_BOOK" + "_test"]

#create
def test_create_donor():
    with TestClient(app) as client:
        response = client.post("/api/donor/" , json={"donor_name": "myrada"})
        assert response.status_code == 201

        body = response.json()
        assert body.get("donor_name") == "myrada"
        assert "_id" in body


#list
def test_list_donors(capsys):
    with TestClient(app) as client:
        with capsys.disabled():
            print('list donors')
        get_donors_response = client.get("/api/donor/")
        assert get_donors_response.status_code == 200


#find     
def test_find_donor():
    with TestClient(app) as client:
        new_donor = client.post("/api/donor/", json={"donor_name": "myrada"}).json()

        get_donor_response = client.get("/api/donor/" + new_donor.get("_id"))
        assert get_donor_response.status_code == 200
        assert get_donor_response.json() == new_donor


#delete
def test_delete_donor():
    with TestClient(app) as client:
        new_donor = client.post("/api/donor/",json={"donor_name": "myrada"}).json()

        delete_donor_response = client.delete("/api/donor/" + new_donor.get("_id"))
        assert delete_donor_response.status_code == 204


# update donor name
def test_update_donor_name():
    with TestClient(app) as client:
        new_donor = client.post("/api/donor/", json={"donor_name": "myrada"}).json()

        response = client.post("/api/donor/" + new_donor.get("_id"), json={"donor_name": "donor 1"})
        assert response.status_code == 200
        assert response.json().get("donor_name") == "donor 1"
