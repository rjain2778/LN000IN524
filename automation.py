import email
import smtplib
import ssl
from email import encoders
from email import mime
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import time
import pandas as pd
start_time = time.time()


receiver_email=[]//list of emails
subject="Invitation to Fellowship 2020 Convocation | Contree"
body1="""Dear"""
body2="""\

Hope to find you in the best of your health and cheerful spirits.
"""
       
sender_email = 'avibomb2000@gmail.com'
file = 'PPB(3).pdf' # in the same directory as script
password = 'abc'//enter email password
space="""\
        <html>
        <body>
        <br>
        </body>
        <html>"""
html1=""" """
html2 = """\
<html>
 <body>
   <img src="cid:Mailtrapimage" width="800" height="500">
 </body>
</html>
"""
for i in range(0,len(receiver_email)):
    email = MIMEMultipart()
    email["From"] = sender_email
    email["To"] = receiver_email[i]
    email["Subject"] = subject
    
    email.attach(MIMEText(body1))
    email.attach(MIMEText(html1,"html"))
    fp = open('unnamed.png', 'rb')
    image = MIMEImage(fp.read())
    fp.close()
    image.add_header('Content-ID', '<Mailtrapimage>')
    email.attach(image)

    fp1=open('convo.png','rb')
    image1 = MIMEImage(fp1.read())
    fp1.close()
    image1.add_header('Content-ID','<Mailtrapimage1>')
    email.attach(image1)

    
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_email, password) #login with mail_id and password
    text = email.as_string()
    session.sendmail(sender_email, receiver_email[i], text)
    session.quit()
    print('Mail sent')
print("--- %s seconds ---" % (time.time() - start_time))