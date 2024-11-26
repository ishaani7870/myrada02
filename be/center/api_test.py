import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from dotenv import dotenv_values
from pymongo import MongoClient
from be.main import app

config = dotenv_values(".env")
app.database = app.mongodb_client["DB_BOOK" + "_test"]

#create
def test_create_center():
    with TestClient(app) as client:
        response = client.post("/api/center/" , json={"center_name": "myrada"})
        assert response.status_code == 201

        body = response.json()
        assert body.get("center_name") == "myrada"
        assert "_id" in body


#list
def test_list_centers(capsys):
    with TestClient(app) as client:
        with capsys.disabled():
            print('list centers')
        get_centers_response = client.get("/api/center/")
        assert get_centers_response.status_code == 200


#find     
def test_find_center():
    with TestClient(app) as client:
        new_center = client.post("/api/center/", json={"center_name": "myrada"}).json()

        get_center_response = client.get("/api/center/" + new_center.get("_id"))
        assert get_center_response.status_code == 200
        assert get_center_response.json() == new_center


#delete
def test_delete_center():
    with TestClient(app) as client:
        new_center = client.post("/api/center/",json={"center_name": "myrada"}).json()

        delete_center_response = client.delete("/api/center/" + new_center.get("_id"))
        assert delete_center_response.status_code == 204


# update center name
def test_update_center_name():
    with TestClient(app) as client:
        new_center = client.post("/api/center/", json={"center_name": "myrada"}).json()

        response = client.post("/api/center/" + new_center.get("_id"), json={"center_name": "center 1"})
        assert response.status_code == 200
        assert response.json().get("center_name") == "center 1"
