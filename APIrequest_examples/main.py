import requests
from pprint import pprint
import json

# post_code_req = requests.get("https://api.postcodes.io/postcodes/ll369aa")
#
# # print(post_code_req.status_code)
# # print(post_code_req.headers)
# # print(post_code_req.content)
# pprint(post_code_req.json())

json_body = json.dumps({'postcodes': ["PR3 0SG", "M45 6GN", "EX16 5BL"]})
headers = {'Content Type': 'application/json'}

post_multi_req = requests.post("https://api.postcodes.io/postcodes/", headers=headers, data=json_body)

pprint(post_multi_req.json())
