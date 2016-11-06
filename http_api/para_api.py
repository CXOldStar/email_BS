# -*- coding: utf-8 -*-
from http_api.base_obj import BaseHandler


class BasePara(BaseHandler):
    def get(self):
        # get data from database.
        self.render('basepara.html')

    def post(self):
        server_username = self.get_argument("server_username", "")
        server_password = self.get_argument("server_password", "")
        server_host = self.get_argument("server_host", "")
        server_port = self.get_argument("server_port", "")
        # check data whet exited and store data that do not still exited.


class RecvAccount(BaseHandler):
    def get(self):
        self.render('manage_account.html')

    def post(self):
        optoin = self.get_argument("option", "")
        account_name = self.get_argument("account_name", "")
        # check data whet exited and store data that do not still exited.
