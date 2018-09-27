# -*- coding: utf-8 -*-


class Client:
    def __init__(self, token):
        self.service = self.get_authenticated_service(token)

    def get_authenticated_service(self, token):
        return None

#
