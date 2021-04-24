import os


class Config:
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}' \
                              ':{PORT}/{DB_NAME}'.format(
        **{
            'USER': os.getenv('DB_USER', 'newuser'),
            'PASSWORD': os.getenv('DB_PASSWORD', 'password'),
            # 'HOST': os.getenv('DB_HOST', 'host.docker.internal'),
            'HOST': os.getenv('DB_HOST', 'localhost'),
            'PORT': os.getenv('DB_PORT', '3306'),
            'DB_NAME': os.getenv('DB_NAME', 'lear1')
        })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    COGNITO_ISS = 'https://cognito-idp.us-east-2.amazonaws.com/' \
                  'us-east-2_y201HrM5j'
    COGNITO_APP_CLIENT_ID = '1h1qachoo41mccpijjmqmgjdn1'
