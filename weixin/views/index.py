# -*- coding: utf-8 -*-

import hashlib

from flask import request
from flask import current_app
from flask import session
from flask import jsonify
from flask import redirect
from flask import url_for

from weixin.extensions import weixin
from . import bp


@bp.route('/')
def index():
    if 'weixin_oauth' in session:
        weixin_oauth = session['weixin_oauth']
        openid = weixin_oauth.get('openid')
        access_token = weixin_oauth.get('access_token')
        resp = weixin.get('sns/userinfo',
                          data={'openid': openid,
                                'access_token': access_token})
        return jsonify(resp.data)
    return redirect(url_for('login'))


@bp.route('/signature_verify')
def signature_verify():
    signature = request.args.get('signature', '')
    timestamp = request.args.get('timestamp', '')
    nonce = request.args.get('nonce', '')
    echostr = request.args.get('echostr')
    if not check_signature(signature, timestamp, nonce):
        return 'signature failed', 400
    return echostr


def check_signature(signature, timestamp, nonce):
    token = current_app.config['WEIXIN_TOKEN']
    _sha1 = hashlib.sha1(
        ''.join(sorted([token, timestamp, nonce]))
    ).hexdigest()
    return True if _sha1 == signature else False
