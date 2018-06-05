import os
import sys
import requests
import json

d = sys.argv[1]
c = sys.argv[2]
if d == "get":
    r = requests.get(c)
    print(r.json())
    sys.exit()
if d == "post":
    d = {"id":"10010010",
         "group":"test"}
    r = requests.post(c,json=d)
    print(r.json())