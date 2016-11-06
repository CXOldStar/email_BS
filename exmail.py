# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.gen
import tornado.web
import tornado.netutil
import tornado.process
from tornado.httpserver import HTTPServer
from tornado.options import define, options
import config


# define('server_address', default="183.230.40.230", type=str, help="set server IP address")
define('server_address', default="127.0.0.1", type=str, help="set server IP address")
define('server_port', default=9080, type=int, help="set server run in which port")
define('multi_processes', default=1, type=int,
       help="the number of fork subprocesses.And 0 mean auto forks one process per cpu;multi-process mode")


settings = {
    "patap_title": 'Tornado Patap',
    "template_path": config.TEMPLATE_PATH,
    "static_path": config.STATIC_PATH,
    "debug": config.DEBUG,
    "cookie_secret": config.COOKIE_SECRET,
    "login_url": "/auth/login/"
}


class WelCome(BaseHandler):
    def get(self):
        # self.render("docs/examples/dashboard/patap.html", current_user='zhuzhixing@cnicg.cn')
        self.render("docs/examples/dashboard/main.html")


def main():
    sockets = tornado.netutil.bind_sockets(options.server_port, address=options.server_address)
    tornado.process.fork_processes(options.multi_processes)
    application = tornado.web.Application([
        (r"/", WelCome),
        (r"/para/", patap_api.Patap),
        (r"/para/manage-account/", patap_api.PatapId),  # manage recv email account
        (r"/send/", patap_api.PatapAdd),
        (r"/send/email-para/", server_api.Server),
        (r"/send/email-para/manage/", server_api.Server),
    ], **settings)  # if use application.listen(9080), it cannot work in advanced uses (e.g. multi-process mode)
    server = HTTPServer(application)
    server.add_sockets(sockets)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
