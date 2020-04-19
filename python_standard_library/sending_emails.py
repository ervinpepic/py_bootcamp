from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template

import smtplib


template = Template(Path("email_template.html").read_text())
message = MIMEMultipart
message["from"] = "Ervin"
message["to"] = "pepic_ervin@hotmail.com"
message["subject"] = "This is a test email"
body = template.substitute({"name": "Ervin"})
message.attach(MIMEText("Body", "html"))
message.attach(MIMEImage(Path("profile.jpg").read_bytes()))

with smtplib.SMTP(host="smpt.outlook.com", port=587) as smpt:
    smpt.ehlo()
    smpt.starttls()
    smpt.login("pepic_ervin@hotmail.com", "somePassword")
    smpt.send_message(message)
    print("Sent..")
