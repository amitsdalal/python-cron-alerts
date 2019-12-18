#!/usr/bin/python
import requests, sys, ssl, email, smtplib, time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

url = sys.argv[1]

### define url hit

def hit():
    pull_pubs = requests.get(url)
    if pull_pubs.status_code != 200:
            #send_mail()
            name = "MageHost Team"
            from_address = "no-reply@your-domain.com"
            to_address = "a@your-domain.com, b@client-domain.com"
            subject = url
            msg = MIMEMultipart()
            msg['From'] = from_address
            msg['To'] = to_address
            msg['Subject'] = "Cron fail with status code:  " +((str(pull_pubs.status_code)) + "  URL  " + (subject))
            #status_code_int = (pull_pubs.status_code)
            content = ((str(pull_pubs.status_code)) + (pull_pubs.text))
            body = """

                Hello {0}.

                    Cron failed for said subject URL.

                    If you have any questions regarding the same, kindly contact us at your support Desk ID.

                    --
                Regards 
                NOC team.
                The error status and text are encoded below for your reference on the same.

                """.format(name) +(content)
            msg.attach(MIMEText(body, 'plain'))
            server = smtplib.SMTP('email-smtp.eu-west-1.amazonaws.com', 587)
            server.starttls()
            server.login("yourSesUserName", "yourSesPasswordHere")
            text = msg.as_string()
            server.sendmail(from_address, to_address, text)
            server.quit()   
##Hit the URL
hit()
