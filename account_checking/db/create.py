# -*- coding: utf-8 -*-

from .basic import metadata
from .tables import balance


def create_all_table():
    metadata.create_all()


if __name__ == "__main__":
    create_all_table()
