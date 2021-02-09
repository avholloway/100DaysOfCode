import os
from twilio.rest import Client

class NotificationManager:
    def __init__(self):
        self.account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        self.auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        self.twilio_did = os.getenv('TWILIO_DID')
        self.cell_number = os.getenv('CELL_NUMBER')
        self.client = Client(self.account_sid, self.auth_token)

    def send(self, msg: str):
        try:
            self.client.messages.create(
                body=msg,
                from_=self.twilio_did,
                to=self.cell_number
            )
        except:
            pass