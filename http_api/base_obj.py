# -*- coding: utf-8 -*-
import tornado.web
import tornado.escape


class BaseHandler(tornado.web.RequestHandler):
    COOKIE_NAME = "patap_user"

    def get_current_user(self):
        user_json = self.get_secure_cookie(self.COOKIE_NAME)
        if not user_json:
            return None
        return tornado.escape.json_decode(user_json)
