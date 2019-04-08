# -*- coding: utf-8 -*-

import time
import uuid

from sqlalchemy import (
    BIGINT, DECIMAL, Column, String,
    Table, UniqueConstraint, ForeignKey
)
from sqlalchemy.dialects.mysql import BIGINT

from ..utils import UUID, now_timestamp, generate_uuid
from .basic import metadata


# balance table
balance = Table(
    'balance', metadata,
    Column(
        'id', String(32), primary_key=True, nullable=False,
        default=generate_uuid
    ),
    Column('user', String(10), nullable=False),
    Column('symbol', String(10), index=True, nullable=False),
    Column('balance', DECIMAL(50, 10), nullable=False, default=0),
    Column(
        'create_time', BIGINT(unsigned=True),
        default=now_timestamp, index=True
    ),
    Column(
        'update_time', BIGINT(unsigned=True),
        default=now_timestamp,
        onupdate=now_timestamp
    ),
    UniqueConstraint('id', 'symbol')
)


__all__ = ['balance']
