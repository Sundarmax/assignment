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

    def get_user_list(self):
        self.conn.request("GET", "/v2/users?status=active&page_size=30", headers=self.headers)
        res = self.conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))
    
    def create_new_meeting(self):
        request_url  = "/v2/users/"+"sundar.rajan@clinilead.com"+"/meetings"
        input_dict = {"type":"1"}
        json_input = json.dumps(input_dict) 
        self.conn.request("POST",request_url,json_input,headers=self.headers)
        res = self.conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))

    def get_all_participant(self):
        metting_id  = "73748445565"
        request_url = "/v2/meetings/" + metting_id +"/registrants"
        self.conn.request("GET",request_url,headers=self.headers)
        res = self.conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))

    def add_new_participant(self):
        metting_id  = "99264396904"
        request_url = "/v2/meetings/" + metting_id +"/registrants"
        input_dict = {
                "email": "sundar.info22@gmail.com",
                "first_name": "Sundar",
                "last_name": "Rajan",
                "address": "123 Main ST",
                "city": "San Jose",
                "country": "US",
                "zip": "95550",
                "state": "CA",
                "phone": "111-444-4444",
                "industry": "Tech",
                "org": "IT",
                "job_title": "DA",
                "purchasing_time_frame": "More Than 6 Months",
                "role_in_purchase_process": "Influencer",
                "no_of_employees": "1-20",
                "comments": "Excited to host you.",
                "custom_questions": [
                    {
                    "title": "Favorite thing about Zoom",
                    "value": "Meet Happy"
                    }
                ]
            }
        json_input = json.dumps(input_dict) 
        self.conn.request("POST",request_url,json_input,headers=self.headers)
        res = self.conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))

    def test_with_request_lib(self):
        target_url = "https://api.zoom.us/v2/users/"
        #security_key = "TOK" +':'+"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOm51bGwsImlzcyI6IlRSQWNZQVN0U0dpdGRZX2ZJUGpJdHciLCJleHAiOjE2MDI0OTMzMDgsImlhdCI6MTYwMjQ4NzkwOH0.0iAglbTwQJ03TbdVM7Dj__fxXn69n58uSClEmioSMjE"
        result = requests.get(target_url,headers=self.headers)
        print(result.text)

    def update_registrant_status(self):
        request_url  = "/v2/meetings/99264396904/registrants/status"
        input_dict = {
                "action": "deny",
                "registrants": [
                    {
                    "id": "gxMfl6L_Qe6EXX72-s8h-w",
                    "email": "sundar.info22@gmail.com"
                    }
                ]
            }
        json_input = json.dumps(input_dict) 
        self.conn.request("PUT",request_url,json_input,headers=self.headers)
        res = self.conn.getresponse()
        print(res.status)
        data = res.read()
        print(data.decode("utf-8"))

obj = ZoomAPIClient()
#obj.update_registrant_status()
#obj.add_new_participant()
#obj.test_with_request_lib()
#obj.get_all_participant()
#obj.add_new_participant()
obj.get_user_list()
#obj.create_new_meeting()