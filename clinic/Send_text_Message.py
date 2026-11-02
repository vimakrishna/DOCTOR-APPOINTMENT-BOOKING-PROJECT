# Account_sid = "AC5aa08afe9424b12b35f0f631d35ba6d7"
# Token = "a210ca36dfa2ce52a9ef1ece08a36a63"


import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+919037610037",
    from_="+17372508034",
    body="Booked Successfully ",
)

print(message.sid)

