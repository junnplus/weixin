# -*- coding: utf-8 -*-

from flask import session
from werkzeug.urls import url_parse
from werkzeug.urls import url_encode
from flask_oauthlib.client import OAuth
from raven.contrib.flask import Sentry

oauth = OAuth()
sentry = Sentry()

weixin = oauth.remote_app(
    'weixin',
    app_key='WEIXIN',
    request_token_params={'scope': 'snsapi_userinfo', 'state': 1},
    base_url='https://api.weixin.qq.com',
    authorize_url='https://open.weixin.qq.com/connect/oauth2/authorize',
    access_token_url='https://api.weixin.qq.com/sns/oauth2/access_token',
    content_type='application/json')

original_methods = {
    'authorize': weixin.authorize,
    'authorized_response': weixin.authorized_response,
}


def authorize(*args, **kwargs):
    response = original_methods['authorize'](*args, **kwargs)
    url = url_parse(response.headers['Location'])
    args = url.decode_query()

    args['appid'] = args.pop('client_id')
    url = url.replace(query=url_encode(args, sort=True),
                      fragment='wechat_redirect')

    response.headers['Location'] = url.to_url()
    return response


def authorized_response(*args, **kwargs):
    original_access_token_params = weixin.access_token_params
    weixin.access_token_params = {
        'appid': weixin.consumer_key,
        'secret': weixin.consumer_secret,
    }
    response = original_methods['authorized_response'](*args, **kwargs)
    weixin.access_token_params = original_access_token_params
    return response


weixin.authorize = authorize
weixin.authorized_response = authorized_response


@weixin.tokengetter
def get_weixin_token():
    if 'weixin_oauth' in session:
        resp = session['weixin_oauth']
        return resp['access_token'], ''
