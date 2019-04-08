# -*- coding: utf-8 -*-

import time
import uuid


def now_timestamp():
    return int(time.time()*1000)


def generate_uuid():
    return uuid.uuid4().hex
