import smtp
import os 
from dotenv import load_dotenv

load_dotenv()

SMTP_USERNAME = os.getenv['SMTP_USERNAME']
SMTP_PASSWORD = os.getenv['SMTP_PASSWORD']
SMTP_PORT = os.getenv['SMTP_PORT']
SMTP_API = os.getenv['SMTP_API']
SMTP_HOST = os.getenv['SMTP_HOST']
SMTP_EMAIL = os.getenv['SMTP_EMAIL']



class Mailer:
    def __init__(self, message, recipient):
        self.message = message
        self.recipient = message
    


    def __call__():
        server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
        server.login(sender_email, password)


    def send(self):
        server.send()






