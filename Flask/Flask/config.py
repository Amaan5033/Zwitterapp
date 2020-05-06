
import os


class Config:
    SECRET_KEY = "1fa782621e7b88f755956a213c14e1ac"
    SQLALCHEMY_DATABASE_URI ="sqlite:///site.db"
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
