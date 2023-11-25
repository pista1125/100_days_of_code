import smtplib

import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders

class NotificationManager:
    def __init__(self):
        self.my_email = "pista1125@gmail.com"
        self.password = "tsewwfcqkvhforiy"

    def send_email(self):
        #encoding: "iso-8859-1" if outlook, utf-8 if gmail

        with smtplib.SMTP("smtp.gmail.com", 587, timeout=180) as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.password)
            connection.sendmail(from_addr=self.my_email, to_addrs=self.my_email,
                                msg="Subject:Hello\n\nEzt a pythonbol küldöm most neked!".encode("utf-8"))


    def send_mail(self, send_from, send_to, subject, text, username="pista1125@gmail.com", password="tsewwfcqkvhforiy", isTls=True):
        msg = MIMEMultipart()
        msg['From'] = send_from
        msg['To'] = send_to
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = subject
        msg.attach(MIMEText(text))

        part = MIMEBase('application', "octet-stream")
        part.set_payload(open("flight.xlsx", "rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="flight.xlsx"')
        msg.attach(part)

        # context = ssl.SSLContext(ssl.PROTOCOL_SSLv3)
        # SSL connection only working on Python 3+
        smtp = smtplib.SMTP("smtp.gmail.com", 587)
        if isTls:
            smtp.starttls()
        smtp.login(username, password)
        smtp.sendmail(send_from, send_to, msg.as_string())
        smtp.quit()