from App import mail
from flask import url_for
from flask_mail import Message
from .models import User


def send_reset_link(user: User):
    token = user.generate_reset_token(30 * 60)
    print(token)
    msg = Message(
        subject='Reset Password Link',
        sender='noreply@demo.com',
        recipients=[user.email],
        body=f"""
        To reset your password, visit the following link:
        {url_for('authentication.reset_token', token=token, _external=True)}
        If you did not make this request then simply ignore this email and no changes will be made.
        """
    )
    mail.send(msg)
