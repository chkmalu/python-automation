import requests
import smtplib
import os

url = os.environ['URL']
get_status = requests.get(url).status_code

def send_mail(txt):
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as sm:
        sm.login(os.environ['EMAIL_NAME'],os.environ['EMAIL_PWD'])
        ms = txt
        sm.sendmail(os.environ['EMAIL_NAME'], os.environ['EMAIL_NAME'], ms)
try:
    if get_status == 200:
        print("application is up and running")
    else:
        print(f"applicatio is down with error code {get_status}")
        msg = "Subject: testing\nthe application is down with please restart"
        send_mail(msg)
except Exception as expt:
    print(f"applicatoin not reachable with error {expt}")
    msg = "can reach application kindly restart the server"
    send_mail(msg)
