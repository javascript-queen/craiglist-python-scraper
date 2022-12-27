# If using gmail remember to turn on "Access for less secure apps" in GMail via Link beforehand
# https://www.google.com/settings/security/lesssecureapps

import smtplib
from email.mime.text import MIMEText as text

def test_sendmail(subject):
    to_address ='michelemail@mail.ru' # your address
    body = subject
    subject=subject
    sendmail(to_address, subject, body)
    
def sendmail(to_address, subject, body): 
    from_address='yourmail@mail.ru' # your address
    smtp_server = 'smtp.mail.ru' # mail service (for gmail it'll be smtp.gmail.com)
    smtp_port= 465 # mail service (for gmail it'll be 587)
    smtp_user= 'yourmail@mail.ru' # your address
    smtp_password='yourpassword' # your psw

    msg = text(body)
    msg['Subject'] = subject
    msg['From'] = from_address
    msg['To'] = to_address

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.ehlo()
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.sendmail(from_address, to_address, msg.as_string())
    server.quit()