# -*- coding: utf-8 -*-

from sqlalchemy import func

from .db.basic import db_session
from .db.models import Balance
from .exceptions import BalanceException, ChargeException
from .settings import DEBT


def update_balance(name, symbol, change):
    """update account balance
    when change is greater than 0, means deposit
    when change is less than 0, means withdraw
    """

    balance = db_session.query(Balance).filter(
        Balance.user == name, Balance.symbol == symbol
    ).first()

    new_balance = balance.balance + change if balance else change

    if name == DEBT and new_balance > 0 or name != DEBT and new_balance < 0:
        raise ChargeException('Illegal Charge')
    else:
        if balance:
            balance.balance = new_balance
        else:
            balance = Balance()
            balance.user = name
            balance.symbol = symbol
            balance.balance = new_balance
            db_session.add(balance)

        if name != DEBT:
            update_balance(DEBT, symbol, -1*change)

        db_session.commit()


def check_balance():
    """check coin balance
    """

    result = db_session.query(
        Balance.symbol, func.sum(Balance.balance).label('balance')
    ).group_by(Balance.symbol).all()

    for r in result:
        if r.balance != 0:
            raise BalanceException(f'{r.symbol} balance is fault!')
