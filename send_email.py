import json
import smtplib
import ssl

json_file = open("config.json")
cfg = json.load(json_file)
# print(cfg)


def Send_Email():
    smtp_server = cfg['server']
    sender = cfg["email"]
    receiver = cfg["to"]
    password = cfg["pwd"]
    msg = """\
    Subject: Hi!
    Test Message from Medium"""
    c = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, 587) as s:
        print('got to position 1')
        print(f"the receiver is {receiver}.")
        s.ehlo()  
        s.starttls(context=c)
        s.ehlo()
        s.login(sender, password)
        s.sendmail(sender, receiver, msg)
        print('The email has been sent.')

if __name__ == "__main__":
    Send_Email()