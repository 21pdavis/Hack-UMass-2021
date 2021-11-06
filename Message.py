import os
from twilio.rest import Client

account_sid = 'AC68cb445f7aee74876779d2c93748b227'
auth_token = '8f1a118cdbc10768d8761b0e63e262f5'
client = Client(account_sid, auth_token)

def sendMessage(text):
    message = client.messages \
                    .create(
                        body=text,
                        from_='+13082183325',
                        to='+14134064010'
                    )
    print(message.sid)