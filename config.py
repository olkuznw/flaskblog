import os

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY') or 'QhIUeulzGyyV5uJ8eurm'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False

@staticmethod
def init_app(app):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://' + ':'.join([os.environ.get('DB_DEV_USER'), os.environ.get('DB_DEV_PASS')]) + ':password@localhost/' + os.environ.get('DB_DEV_NAME')

class TestConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://' + ':'.join([os.environ.get('DB_TEST_USER'), os.environ.get('DB_TEST_PASS')]) + ':password@localhost/' + os.environ.get('DB_TEST_NAME')

class LiveConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://' + ':'.join([os.environ.get('DB_LIVE_USER'), os.environ.get('DB_LIVE_PASS')]) + ':password@localhost/' + os.environ.get('DB_LIVE_NAME')

config = {
    'dev': DevelopmentConfig,
    'test': TestConfig,
    'live': LiveConfig,
    'default': DevelopmentConfig
}
