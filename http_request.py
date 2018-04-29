import json
import requests

url = "http://www.google.com/"
headers = {
    'Content-Type': "application/json",
    'Cache-Control': "no-cache",
    }
f = open('response','w')
with open('request') as request:
    payload = json.load(request)
    try:
        str_payload = json.dumps(payload)
        #print "request:"
        #print str_payload
        response = requests.request("POST", url, data=str_payload, headers=headers)
        #print "response:"
        print(response.text)
    except:
        f.write("error")

f.close()
