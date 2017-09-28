#! env bin/python
# codding = utf-8
import requests
from requests import post, get

req = requests.get("http://google.com", params={})
print(req)
#print(req.text)
#print(req.json())
print(req.headers)



