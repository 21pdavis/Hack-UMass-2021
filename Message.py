import os
from twilio.rest import Client

account_sid = 'AC68cb445f7aee74876779d2c93748b227'
auth_token = 'd2420dbcd9cc3d2ae8eb4b697fe48cdc'
client = Client(account_sid, auth_token)

def sendMessage(text, outgoing):
    message = client.messages \
                    .create(
                        body=text,
                        from_='+13082183325',
                        to=outgoing
                    )
    print(message.sid)