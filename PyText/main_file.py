from twilio.rest import Client
from PyText import config
client = Client(config.acc_sid, config.auth_token)
call = client.messages(
    to="some number",
    from_="fffff",
    body="Some text"
)

