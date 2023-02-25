import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from ATSIGraph import *
from MinnHubGraph import *
from CentralHubGraph import *
from LZSouthGraph import *
import os


time.sleep(250)

email = "vcvdigitalteam@outlook.com"
password = "***"

host = "smtp-mail.outlook.com"
port = ***

server = smtplib.SMTP(host, port)

'''
check = server.ehlo()

if check[0] == 250:
    print("yes")
else:
    print("no")
    exit(0)
'''

server.starttls()
server.login(email, password)


#def send_mail(body):
sender_mail = email
receiver_email = "***" 
##receiver_email = "carter.cribbs@duke.edu"

html = '''\
    <html>
        <body>
            <h1> Daily LMP Data:</h1>
            <p>PJM ATSI Hub Data for CLEAVELAND SITE</p>
            <p>MISO Minn Hub Data for MINNESOTA SITE</p>
            <p>NYISO Central Hub Data for BINGHAMTON SITE</p>
            <p></p>
            <p>Have a Great Day!</p>
        <body>
    <html>
    '''


##str_today = "yes"

msg = MIMEMultipart()
msg['Subject'] = str_today + " Daily LMP Data Update"
msg['From'] = sender_mail
msg['To'] = receiver_email

msg.attach(MIMEText(html, "html"))




with open("ATSI Hub Data.png", 'rb') as fp:
    img = MIMEImage(fp.read())
    img.add_header('Content-Disposition', 'attachment', filename = "PJM ATSI Hub Data " + str_today)
    msg.attach(img)

with open("Minn Hub Data.png", 'rb') as fp:
    img = MIMEImage(fp.read())
    img.add_header('Content-Disposition', 'attachment', filename = "MISO Minn Hub Data " + str_today)
    msg.attach(img)

with open("Central Hub Data.png", 'rb') as fp:
    img = MIMEImage(fp.read())
    img.add_header('Content-Disposition', 'attachment', filename = "NYISO Central Hub Data " + str_today)
    msg.attach(img)

with open("South Loading Zone Data.png", 'rb') as fp:
    img = MIMEImage(fp.read())
    img.add_header('Content-Disposition', 'attachment', filename = "ERCOT LZ South Data " + str_today)
    msg.attach(img)


email_string = msg.as_string()


output = server.sendmail(sender_mail, receiver_email, email_string)

print("sent")


'''
Delete Graphs and CSVs
'''

os.remove("/Users/cartercribbs/VCV/ATSI Hub Data.png")
os.remove("/Users/cartercribbs/Downloads/" + csv_ATSI_file_name)
os.remove("/Users/cartercribbs/VCV/Central Hub Data.png")
os.remove("/Users/cartercribbs/Downloads/" + csv_NYISOC_file_name)
os.remove("/Users/cartercribbs/VCV/Minn Hub Data.png")
os.remove("/Users/cartercribbs/Downloads/" + csv_MINN_file_name)
os.remove("/Users/cartercribbs/VCV/South Loading Zone Data.png")
os.remove("/Users/cartercribbs/Downloads/" + csv_LZSouth_file_name)


