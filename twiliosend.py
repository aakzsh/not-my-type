import os
from twilio.rest import Client
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']

def send(email):
    message = Mail(
        from_email='zaniecompany@gmail.com',
        to_emails=email,
        subject='hehehe temsting',
        html_content='<strong>aur frooti, kesi ho</strong>')
    sg = SendGridAPIClient('APIKEY')
    response = sg.send(message)
    print(response.status_code, response.body, response.headers)

    # print("hello")


    