import os
from twilio.rest import Client
from sendgrid import SendGridAPIClient
from twilio.rest import Client
from sendgrid.helpers.mail import Mail


# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']

def send(email, code):
    message = Mail(
        from_email='aakashferrari@gmail.com',
        to_emails=email,
        subject='not your type - invite',
        html_content=f'<!DOCTYPE html><html lang="en"><head> <meta charset="UTF-8"> <meta http-equiv="X-UA-Compatible" content="IE=edge"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>Room Invite</title></head><body style="color: rgba(15, 20, 47, 1);"> <center> <img src="https://media.discordapp.net/attachments/873911486488121344/929328632848064512/Untitled_design_1_1.png" width="100px" alt=""><p>{email} has sent you an invite to join them for not-my-type typeracing game!!</p><p >head over to <a href="https://notmytype.herokuapp.com/joinn/{code},{email}" style="text-decoration: none;">join room</a> and enter the following code</p><p style="font-size: 2rem;">{code}</p><p>or</p><p>scan the following qr code</p><img src="https://api.qrserver.com/v1/create-qr-code/?data=https://notmytype.herokuapp.com/joinn/{code},{email}" alt="" title="HELLO" height="200px"/><p>goodluck with your game and let us know how you enjoyed it</p><br><br><p>© owned by not-my-type</p></center></body></html>')
    sg = SendGridAPIClient('')
    response = sg.send(message)
    print(response.status_code, response.body, response.headers)

    # print("hello")



def getResults(num):
    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="yay this works as well",
                        from_='+14844168079',
                        to=num
                    )

    print(message.sid)

# getResults()