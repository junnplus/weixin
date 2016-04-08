# -*- coding: utf-8 -*-

import os


class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY', 'secret_key')

    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # WEIXIN
    WEIXIN_TOKEN = os.environ.get('WEIXIN_TOKEN', 'token')
    WEIXIN_CONSUMER_KEY = os.environ.get('WEIXIN_CONSUMER_KEY',
                                         'wx6ebca2c3abe568af')
    WEIXIN_CONSUMER_SECRET = os.environ.get('WEIXIN_CONSUMER_SECRET',
                                            '15cbe6cbd0c40eea496ca8ca0d2c8a7e')


class DevelopmentConfig(Config):

    DEBUG = True


class TestingConfig(Config):

    TESTING = True


class ProductionConfig(Config):

    # SENTRY
    SENTRY_DSN = os.environ.get('SENTRY_DSN', 'https://3880902278bb48699e9cdd99aa2da7d5:a97e1346bdae42dca912ff90d6c8c3bd@app.getsentry.com/73089')  # noqa


config = {
    'default': DevelopmentConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
