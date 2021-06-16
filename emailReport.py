import smtplib
import os
from email.message import EmailMessage
import imghdr

email_id = "digitalinvigilator@gmail.com"
email_pass = "Password1a"
msg = EmailMessage()
msg['From'] = email_id
msg["To"] = "ry7979231@gmail.com"
# smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtp = smtplib.SMTP_SSL('smtp.gmail.com', 587)

smtp.login(email_id, email_pass)

def sendEmail(result):
    msg['Subject'] = "Cheating Detected"
    msg.set_content(f'Cheating Detected in {os.getlogin() } : {result}')
    with open("Cheating.jpg", 'rb') as m:
        file_data = m.read()
    file_name = "cheating_" + str(os.getlogin())
    msg.add_attachment(file_data, maintype = "image", subtype = "jpg", filename = "Cheating")

    # with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    # smtp.login(email_id, email_pass)
    smtp.send_message(msg)
    smtp.quit()
    del msg['To']