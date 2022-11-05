from email.message import EmailMessage
import ssl
import smtplib

# Create credentials for login
email_sender = "your_email@gmail.com"
email_password = "application_password"

# Leave that blank until you know who will be
# the recipient of the message
email_receiver = "his/her_email@email.com"

# We have to have a subject for neet email
subject = "Don't forget ro call!"

# In 'body' goes our message for the email
body = """
Please call back when you arrive in the hotel! 
"""

# Here we create a 'instance' of 'EmailMessage' from email.message
em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = subject
em.set_content(body)

# Now we need to create a 'context'
# Before we proceed we need to import ssl/smtp package
context = ssl.create_default_context()

# Now we use credentials for login to gmail account
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
