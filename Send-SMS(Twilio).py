# Send SMS with Twilio

from twilio.rest import Client

account_sid = 'add sid'
auth_token = 'add token'

client = Client(account_sid, auth_token)
message = client.messages.create(
    from_='add phone number from which the msg will be sent',
    body='Test_1',
    to='add phone number to which the msg will be sent'
)
print(message.sid)

#numbers should be based in US or UK
#works only in united states and kingdom
