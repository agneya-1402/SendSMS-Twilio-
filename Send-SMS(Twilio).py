# Send SMS with Twilio

from twilio.rest import Client

account_sid = 'AC60061eaeee04748882413b6e6c678d5e'
auth_token = '8e332ec4fa28b1c62a890225d7e4ae53'

client = Client(account_sid, auth_token)
message = client.messages.create(
    from_='+918828460926',
    body='Test_1',
    to='+917715910874'
)
print(message.sid)

#numbers should be based in US or UK
#works only in united states and kingdom