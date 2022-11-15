import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Jara Guta'
email['to'] = 'testdummytrue@gmail.com'
email['subject'] = 'you have won a $100 gift card'

email.set_content('visit our shop to collect ur gift card')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('testdummytrue@gail.com', 'dummypassword')
    smtp.send_message(email)
    print('task done!!!')
