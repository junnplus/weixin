# -*- coding: utf-8 -*-

from flask import url_for
from flask import redirect
from flask import session

from weixin.extensions import weixin
from . import bp


@bp.route('/login')
def login():
    return weixin.authorize(callback=url_for('weixin.authorized',
                            _external=True))


@bp.route('/login/authorized')
def authorized():
    resp = weixin.authorized_response()
    if resp is None:
        return 'Access denied', 401
    session['weixin_oauth'] = resp
    return redirect(url_for('weixin.index'))
