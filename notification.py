import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning,InsecurePlatformWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)
from argparse import ArgumentParser
parser = ArgumentParser("webex.py")  
parser.add_argument("-m", "--message", help="the message you want to send", required=True)
args = parser.parse_args() 
message = args.message

def post_message(message,room_id):
   token = 'NGJlMWVlNGMtZjg3Ny00YjA1LThjNzQtMTgwYTc0OTVkMWQzOThhN2JiMDAtNzll_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
   header = {
   "Authorization": "Bearer %s" % token,
   "Content-Type": "application/json"
   }
   data = {
   "roomId": room_id,
   "markdown": message
   }
   #print(message)
   requests.post("https://webexapis.com/v1/messages/", headers=header, data=json.dumps(data), verify=True)


post_message(message,"Y2lzY29zcGFyazovL3VzL1JPT00vOWMxM2EyODAtMjNhMi0xMWVkLTg4MWQtMzMxMDQ4NmI4NTBi")
