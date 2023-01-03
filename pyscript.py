
import requests

simpletext= "Define Bluetooth"

API_ENDPOINT = "http://localhost:5005/webhooks/rest/webhook"

messagePayload = {
       "sender": "test_user",
  "message": simpletext,
      }


r = requests.post(url = API_ENDPOINT, json=messagePayload)
print(r.json()[0]["text"])