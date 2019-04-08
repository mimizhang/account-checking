# -*- coding: utf-8 -*-

from .basic import Base
from .tables import balance


class Balance(Base):
    __table__ = balance
