# -*- coding: utf-8 -*-

from flask import Blueprint

bp = Blueprint('weixin', __name__)

from .index import *  # noqa
