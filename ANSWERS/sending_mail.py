#!/usr/bin/env python
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

DEBUG = False # default, but just in case
# DEBUGGING output for an image will overwhelm most
#  IDEs' output buffers

SMTP_SERVER = "smtpcorp.com"
SMTP_PORT = 2525
SMTP_USER = 'jstrickpython'
SMTP_PWD = 'python(monty)'

SENDER = 'jstrick@mindspring.com'
RECIPIENTS = ['jstrickler@gmail.com']

smtpserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
smtpserver.login(SMTP_USER, SMTP_PWD)
smtpserver.set_debuglevel(DEBUG) # show communication with the server

msg = MIMEMultipart("Here are some attachments")
msg['Subject'] = "Sending email from class"

with open('save_potus_info.py') as file_in:
    attachment_data = file_in.read()

attachment = MIMEText(attachment_data)
attachment.add_header(
    'Content-Disposition', 'attachment', filename='save_potus_info.py'
)
msg.attach(attachment)

with open('../DATA/salad.gif', 'rb') as file_in:
    attachment_data = file_in.read()

attachment = MIMEImage(attachment_data)
attachment.add_header(
    'Content-Disposition', 'attachment', filename='salad.gif'
)

msg.attach(attachment)

try:
    smtpserver.sendmail(
        SENDER,
        RECIPIENTS,
        msg.as_string()
    )
finally:
    smtpserver.quit()

