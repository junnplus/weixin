# -*- coding: utf-8 -*-


class Config(object):

    SECRET_KEY = 'secret_key'

    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # WEIXIN
    WEIXIN_TOKEN = 'token'
    WEIXIN_CONSUMER_KEY = 'wx6ebca2c3abe568af'
    WEIXIN_CONSUMER_SECRET = '15cbe6cbd0c40eea496ca8ca0d2c8a7e'


class DevelopmentConfig(Config):

    DEBUG = True


class TestingConfig(Config):

    TESTING = True


class ProductionConfig(Config):

    pass


config = {
    'default': DevelopmentConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
