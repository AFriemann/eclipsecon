# -*- coding: utf-8 -*-

import os

try:
    import ujson as json
except ImportError:
    import json


def load(path):
    if os.path.exists(path) and os.path.isfile(path):
        with open(path, 'rb') as stream:
            data = stream.read().decode()

            return json.loads(data)

    return {}

#
