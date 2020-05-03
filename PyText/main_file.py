from twilio.rest import Client
from PyText.configuration import acc_sid, auth_token

client = Client(acc_sid, auth_token)
call = client.messages(
    to="some number",
    from_="fffff",
    body="Some text"
)

