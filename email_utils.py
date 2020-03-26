import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import urllib.request
import urllib.parse

url = "localhost/project/verify_access.php?key="
def send_email(email,transaction_id):
    pass
    msg = MIMEMultipart()
    msg['Subject'] = "ATM Alert"
    html = f"""\
    <html>
      <head></head>
      <body>
      Hi,<br>
      Your ATM card is being used somewhere else, please conform the user.
      <a href="{url + transaction_id}"> Click Here</a>
      </body>
    </html>
    """
    html = MIMEText(html, 'html')
    msg.attach(html)
    send = smtplib.SMTP('smtp.gmail.com', 587)
    send.starttls()
    send.login("thisismyinternetid@gmail.com", "9443847471")
    send.sendmail("SSVM Bank", email, msg.as_string())
    send.quit()


def send_sms(number, transaction_id):
    print("Sending SMS passed....")
    return
    msg_text = f''' 
    Hi, We have seen a activity from you atm card.
    Kindly approve/decline the transaction by clicking the below link 
    http://{url+transaction_id}
    '''
    print(msg_text)
    resp = sendSMS('LMqhxysOrKc-HSuo4LU8mv4lVwETyFdEK7Mcmye1NU', "91"+number,
                   'TXTLCL', msg_text)
    print(resp)

def sendSMS(apikey, numbers, sender, message):

    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
        'message' : message, 'sender': sender})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return fr



def send_msg(input1,input2):
    send_sms(input1,input2)