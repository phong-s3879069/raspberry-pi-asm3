import smtplib
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

recipients = ["jesshua722@gmail.com"]

def send_email():
    from_adr = "jesshua722@gmail.com"
    server = SMTP('smtp.gmail.com', 587)
    subject= "Control your light"
    
    msg = MIMEMultipart()
    msg["From"] = from_adr
    msg["To"] = recipients[0]
    msg["Subject"] = subject
    message = "If you want to manually control the light, go to this website: http://192.168.50.199/index.php"
    msg.attach(MIMEText(message))

    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("jesshua722@gmail.com", "KIKI&&KICHI4ever")
    server.sendmail(from_adr, recipients, msg.as_string())
    server.quit()


