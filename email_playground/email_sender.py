import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Ashuxie'
email['to'] = 'minhquach8@gmail.com'
email['subject'] = 'Haha wow'

email.set_content('I am Python Master!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('mqtestingemail@gmail.com', 'Minh112233')
    smtp.send_message(email)
    print('All good')
