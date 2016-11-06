# -*- coding: utf-8 -*-
from http_api.base_obj import BaseHandler


class BasePara(BaseHandler):
    def get(self):
        self.render('basepara.html')

    def post(self):
        server_username = self.get_argument("server_username", "")
        server_password = self.get_argument("server_password", "")
        server_host = self.get_argument("server_host", "")
        server_port = self.get_argument("server_port", "")
        # check data whet exited and store data that do not still exited.

