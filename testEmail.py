# https://automatetheboringstuff.com/2e/chapter18/
# https://mailtrap.io/blog/python-send-email/

def sendEmail(email, password):
    import smtplib

    smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login("physics12305@outlook.com", "PhysicsEmail1")

    sender = "physics12305@outlook.com"

    receiver = email
    message = f"Subject: Test Email\n\nThis is a test email from the program. {password}"

    smtpObj.sendmail(sender, receiver, message)
    smtpObj.quit()

sendEmail("kostispapd@outlook.com", "password")
