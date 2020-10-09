import http.client
import json

class ZoomAPIClient:

    def __init__(self):
        self.conn = http.client.HTTPSConnection("api.zoom.us")
        self.headers = {
            'authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOm51bGwsImlzcyI6IlFqZTMxZnFNUm5pMlJ2WVBlbW9jVHciL"
                        + "CJleHAiOjE2MDI3NTgyNTMsImlhdCI6MTYwMjE1MzQ1M30.OG2ZyAD-ekhblbm_OQhoRUnOnziQXN7Esy4aiHopmCA",
            'content-type': "application/json"
            }

    def get_user_list(self):
        self.conn.request("GET", "/v2/users?status=active&page_size=30&page_number=1", headers=self.headers)
        res = self.conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))
    
    def create_new_meeting(self):
        request_url  = "/v2/users/"+"sundar.info22@gmail.com"+"/meetings"
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
        metting_id  = "71739438599"
        request_url = "/v2/meetings/" + metting_id +"/registrants"
        input_dict = {
                "email": "sundarmax15@gmail.com",
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

obj = ZoomAPIClient()
obj.get_all_participant()
#obj.add_new_participant()
#obj.get_user_list()
#obj.create_new_meeting()