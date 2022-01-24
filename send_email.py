'''
@author: Shivam Mishra
@date: 23-01-22 11:13 PM

'''

import os
from fastapi import BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from dotenv import load_dotenv
load_dotenv('.env')

conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv('MAIL_USERNAME'),
    MAIL_PASSWORD=os.getenv('MAIL_PASSWORD'),
    MAIL_FROM=os.getenv('MAIL_FROM'),
    MAIL_PORT=int(os.getenv('MAIL_PORT')),
    MAIL_SERVER=os.getenv('MAIL_SERVER'),
    MAIL_FROM_NAME=os.getenv('MAIN_FROM_NAME'),
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True
)


async def send_email_async(subject: str, email_to: str, token_id):
    verification_link = f'http://127.0.0.1:8000/users/verification?token_id={token_id}'
    message = MessageSchema(
        subject=subject,
        recipients=[email_to],
        body=verification_link
    )
    fm = FastMail(conf)
    await fm.send_message(message)


# def send_email_background(background_tasks: BackgroundTasks, subject: str, email_to: str, body: dict):
#     message = MessageSchema(
#         subject=subject,
#         recipients=[email_to],
#         body=body,
#         subtype='html',
#     )
#
#     fm = FastMail(conf)
#     background_tasks.add_task(
#         fm.send_message, message, template_name='email.html')