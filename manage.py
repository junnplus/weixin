# -*- coding: utf-8 -*-

from flask_script import Manager, Server, Shell
from werkzeug.contrib.fixers import ProxyFix

from weixin import create_app

app = create_app()
app.wsgi_app = ProxyFix(app.wsgi_app)

manager = Manager(app)
manager.add_command(Shell(make_context=lambda: dict(app=app)))
manager.add_command('runserver', Server(host='0.0.0.0', port='4000'))

if __name__ == '__main__':
    manager.run()
