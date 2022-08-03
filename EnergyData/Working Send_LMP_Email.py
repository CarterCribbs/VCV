import smtplib
from email.message import EmailMessage

message = EmailMessage()
message['Subject']='Daily LMP Data'
message['From']='vcvdigitalteam@hotmail.com'
message['To']='cribbs.carter@gmail.com'
message.set_content("Test Email")

smtp_server = "smtp.live.com"
server = smtplib.SMTP(smtp_server, '465')
#identify this client to the SMTP server
#server.ehlo
#secure the SMTP connection
#server.starttls()

sender_email = "vcvdigitalteam@hotmail.com" 
password = "VCVDigital123!"




server.login(sender_email, password)

server.send_message(message)
server.quit()

print("hi")

'''
# Create a secure SSL context
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
'''









    