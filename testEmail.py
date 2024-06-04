# https://automatetheboringstuff.com/2e/chapter18/
# https://mailtrap.io/blog/python-send-email/

def sendEmail(email, password):
    import smtplib
    from email.mime.text import MIMEText

    smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)

    sender = "physics12305@outlook.com"
    receiver = email

    message = f"Subject: Test Email\n\nThis is a test email from the program."

    smtpObj.sendmail(sender, receiver, message)

sendEmail("kostispapd@outlook.com", "password")
