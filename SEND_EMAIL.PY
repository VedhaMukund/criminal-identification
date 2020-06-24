#pip install smtplib
#vim send-email.py
import smtplib
import config
def send_email(subject,msg):
   try:
     server=smtplib.SMTP('vedhamukund@gmail.com:587')
     server.ehlo()
     server.starttls()
     server.login(config.EMAIL_ADDRESS,config.PASSWORD)







     