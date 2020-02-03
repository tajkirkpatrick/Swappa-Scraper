import json
import os
import smtplib
from datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

with open(os.path.join(os.getcwd(), 'priceSpider/creds.json'), 'r') as fin:
    data = json.load(fin)
    client_email = data['client_email']
    password = data['password']
    send_to_email = data['send_to_email']


class MailSender(object):

    def __init__(self):
        pass

    def sendEmail(self):
        global client_email
        global password
        global send_to_email
        subject = "Swappa Price Spider Alert!"
        message = f"This is an automated message sent by your Scrapy script run on {str(datetime.now())}!"
        file_location = os.path.join(os.getcwd(), 'swappa_web.txt')

        msg = MIMEMultipart()
        msg["From"] = client_email
        msg["To"] = send_to_email
        msg["Subject"] = subject

        msg.attach(MIMEText(message, 'plain'))

        filename = os.path.basename(file_location)
        attachment = open(file_location, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        'attachment; filename= %s' % filename)

        msg.attach(part)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(client_email, password)
        text = msg.as_string()
        server.sendmail(client_email, send_to_email, text)

        return
