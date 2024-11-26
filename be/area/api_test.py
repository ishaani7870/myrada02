import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from dotenv import dotenv_values
from pymongo import MongoClient
from be.main import app

config = dotenv_values(".env")
app.database = app.mongodb_client["DB_BOOK" + "_test"]

#create
def test_create_area():
    with TestClient(app) as client:
        response = client.post("/api/area/" , json={"area_name": "banglore"})
        assert response.status_code == 201

        body = response.json()
        assert body.get("area_name") == "banglore"
        assert "_id" in body


#list
def test_list_areas(capsys):
    with TestClient(app) as client:
        with capsys.disabled():
            print('list areas')
        get_areas_response = client.get("/api/area/")
        assert get_areas_response.status_code == 200


#find     
def test_find_area():
    with TestClient(app) as client:
        new_area = client.post("/api/area/", json={"area_name": "banglore"}).json()

        get_area_response = client.get("/api/area/" + new_area.get("_id"))
        assert get_area_response.status_code == 200
        assert get_area_response.json() == new_area


#delete
def test_delete_area():
    with TestClient(app) as client:
        new_area = client.post("/api/area/",json={"area_name": "banglore"}).json()

        delete_area_response = client.delete("/api/area/" + new_area.get("_id"))
        assert delete_area_response.status_code == 204


# update area name
def test_update_area_name():
    with TestClient(app) as client:
        new_area = client.post("/api/area/", json={"area_name": "banglore"}).json()

        response = client.post("/api/area/" + new_area.get("_id"), json={"area_name": "dubai"})
        assert response.status_code == 200
        assert response.json().get("area_name") == "dubai"
