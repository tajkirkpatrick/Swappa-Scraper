import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path
from datetime import datetime


class MailSender(object):

    def __init__(self):
        pass

    def sendEmail(self):
        client_email = ""
        password = ""
        send_to_email = ""
        subject = "Swappa Price Spider Alert!"
        message = f"This is an automated message sent by your Scrapy script run on {str(datetime.now())}!"
        file_location = "/home/tkirkp18/development/gits/Swappa-Scraper/priceSpider/swappa_web.txt"

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
