import json
import redis
from lib import config

class redis_session():

    def __init__(self):
        self.r = redis.StrictRedis(host=config.REDIS_HOST,port=config.REDIS_PORT)

    def set(self,set_name,data,per=0):
        self.r.set(set_name,data)
        if per != 0:
            self.r.expire(set_name,per)

    def get(self,set_name):
        return self.r.get(set_name)

    def del(self,set_name):
        self.r.delete(set_name)

    def topic(self,t_name,data=""):
        self.r.publish(t_name,data)

    def hset(self,h_name,key,value,per=0):
        self.r.hset(h_name,key,value)
        if per != 0:
            self.r.expier(h_name,per)

    def hget(self,h_name,key):
        return self.r.hget(hname,key)

    def hkeys(self,h_name):
        return self.r.hkeys(h_name)