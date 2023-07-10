from fastapi import APIRouter
from pydantic import BaseModel
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from dotenv import dotenv_values

router = APIRouter()


class EmailItem(BaseModel):
    name: str
    email: str
    message: str


@router.post("/api/send-email")
async def send_email(item: EmailItem):
    env_vars = dotenv_values('.env.local')

    # Access the environment variables
    from_email = env_vars['FROM_EMAIL']
    from_email_password = env_vars['FROM_EMAIL_PASSWORD']
    to_email = env_vars['TO_EMAIL']
    smtp_server = env_vars['SMTP_SERVER']
    # Convert to an integer
    smtp_server_port = int(env_vars['SMTP_SERVER_PORT'])

    msg = MIMEMultipart()
    msg['From'] = item.email
    msg['To'] = to_email
    msg['Subject'] = f'Message from {item.name}'

    body = item.message
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP(smtp_server, smtp_server_port) as server:
        server.starttls()
        server.login(from_email, from_email_password)
        text = msg.as_string()
        server.sendmail(item.email, to_email, text)

    return {'message': 'Email sent successfully'}