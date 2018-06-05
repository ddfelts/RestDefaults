import os
import json

def rtMessage(status,msg):
    data = {"status":status,
            "msg":msg}
    return data

def rtError(msg):
    return json.dumps(rtMessage("error",msg))

def rtSuccess(msg):
    return json.dumps(rtMessage("success",msg))

