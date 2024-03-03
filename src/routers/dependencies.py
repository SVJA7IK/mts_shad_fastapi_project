from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.dao import SellerDAO, BookDAO


def get_session():
    raise NotImplementedError


def get_seller_dao(session: Annotated[AsyncSession, Depends(get_session)]):
    return SellerDAO(session)


def get_book_dao(session: Annotated[AsyncSession, Depends(get_session)]):
    return BookDAO(session)
