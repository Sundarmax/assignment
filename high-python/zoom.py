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

obj = ZoomAPIClient()
#obj.get_user_list()
obj.create_new_meeting()
