import requests

class Token:
    post_url = 'http://localhost:8080/realms/master/protocol/openid-connect/token'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic YWRtaW4tY2xpOg==',
        'Content-Length': '49'
    }
    data = 'grant_type=password&username=admin&password=admin'
    access_token = ''

token = Token

r = requests.post(token.post_url, data=token.data, headers=token.headers)
token.access_token = r.json()['access_token']
print(r.text)
assert r.status_code == 200
assert token.access_token is not ''

class User:
    get_url = 'http://localhost:8080/admin/realms/RASENMAEHER/users?username='
    post_url = 'http://localhost:8080/admin/realms/RASENMAEHER/users/'
    delete_url = post_url
    get_headers = {
        'Authorization': 'Bearer ' + token.access_token,
    }
    delete_headers = get_headers

    post_headers =  {
        **get_headers,
        'Content-Type': 'application/json',
        'Content-Length': '28'
    }
    data = '{"username": "testi4"}'
    id = ''
