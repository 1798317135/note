import requests

url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=TpztlBy74OgzwHHm2c7jLNE9&client_secret=jPtbyck0FRhao4zT1pxAY85I4E4bTqbf'

headers = {
    'ontent-Type':'application/json; charset=UTF-8',
}
response = requests.get(url = url, headers = headers)
content = response.json()
if (content):
    print(content)