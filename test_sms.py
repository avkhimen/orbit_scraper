# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACcf02cf1eaeef8da693d5cfc5133c5005'
auth_token = '21336328f05607005b6a6f74d6b2dce8'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+12012124816',
                     to='+17809321716'
                 )

print(message.sid)