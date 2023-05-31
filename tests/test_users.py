import requests
from conftest import User
user = User

def test_no_users():
    r = requests.get(user.get_url, headers=user.get_headers)
    print(r.text)
    assert r.json() == []

def test_create_user():
    r = requests.post(user.post_url, data=user.data, headers=user.post_headers)
    print(r.text)
    assert r.status_code == 201

def test_get_user():
    r = requests.get(user.get_url, headers=user.get_headers)
    user.id = r.json()[0]['id']
    print(r.text)
    assert user.id is not ''

def test_delete_user():
    r = requests.delete(user.delete_url + user.id, headers=user.delete_headers)
    print(r.text)
    assert r.status_code == 204
