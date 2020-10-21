import http.client
import requests
import json

class ZoomAPIClient:

    def __init__(self):
        self.conn   = http.client.HTTPSConnection("api.zoom.us")
        self.token  = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOm51bGwsImlzcyI6IlRSQWNZQVN0U0dpdGRZX2ZJUGpJdHciLCJleHAiOjE2MDMxMDY1ODksImlhdCI6MTYwMjUwMTc4OX0.yrRPRNLiieAKsbIwoZ6AbFmKQUTvwIigFT8vys5Pj1s"
        self.headers = {
            'authorization': "Bearer "+ self.token,
            'content-type': "application/json"
            }
    
    def list_user_meeting(self):
        self.conn.request("GET", "/v2/users/sundar.rajan@clinilead.com/meetings", headers=self.headers)
        res = self.conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))

    def create_new_meeting(self):
        request_url  = "/v2/users/"+"sundar.rajan@clinilead.com"+"/meetings"
        input_dict = {"type":"2","start_time":"2020-10-13T18:02:00Z","duration":"60"}
        json_input = json.dumps(input_dict) 
        self.conn.request("POST",request_url,json_input,headers=self.headers)
        res = self.conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))
    
    def get_user_meeting(self):
        self.conn.request("GET", "/v2/meetings/"+"97112441726", headers=self.headers)
        res = self.conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))

obj = ZoomAPIClient()
#obj.list_user_meeting()
#obj.create_new_meeting()
obj.get_user_meeting()
