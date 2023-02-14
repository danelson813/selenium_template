# import necessary libraries
import smtplib
from email.message import EmailMessage

email_sender = 'danelson813@gmail.com'  # Sender email
email_password = 'XXX'  # password which is the one taken from Google account.
email_receiver = 'dan.nelson1@gmail.com@gmail.com'  # email receiver
subject = 'Send mail with Python!'  # your mail subject
content = 'Please look at attached file'  # email content(you can add .txt file in here.)


def send_mail_with_attachment(email_receiver_, subject_, content_, excel_file):
    msg = EmailMessage()
    msg['Subject'] = subject_  # definition of subject
    msg['From'] = email_sender  # definition of sender
    msg['To'] = email_receiver_  # definition of receiver
    msg.set_content(content_)  # setting content
    with open(excel_file, 'rb') as f:
        file_data = f.read()  # reading of Excel file, you can change this to csv,txt,png..
    # add attachment part.need to optimize for your file.
    msg.add_attachment(file_data, maintype="application", subtype="xlsx", filename=excel_file)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:  # our port is 465 for mail.
        smtp.login(email_sender, email_password)  # login to gmail.
        smtp.send_message(msg)  # sending to email


if __name__ == '__main__':
    send_mail_with_attachment(email_receiver, subject, content, '/content/sample_data/try.xlsx')
