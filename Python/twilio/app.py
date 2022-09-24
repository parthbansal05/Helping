# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'sid'
auth_token = 'token'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        twiml='<Response><Play loop="10">https://demo.twilio.com/docs/classic.mp3</Play></Response>',
                        to='',
                        from_=''
                    )

print(call.sid)
