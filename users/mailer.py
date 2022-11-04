import smtp
import os 
from dotenv import load_dotenv

load_dotenv()



PORT = os.getenv['PORT']
HOST = os.getenv['HOST']
USER = os.getenv['USERNAME']
PASS = os.getenv['PASSWORD']

class Mailer:
    def __init__(self, message, recipient):
        self.message = message
        self.recipient = message
    


    def __call__():
        server = smtplib.SMTP(HOST,PORT)
        server.login(sender_email, password)


    def send(self):
        server.send()






