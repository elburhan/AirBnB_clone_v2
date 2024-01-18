#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    # Class attribute for the table name
    __tablename__ = 'users'

    # Column for email
    email = Column(String(128), nullable=False)

    # Column for password
    password = Column(String(128), nullable=False)

    # Column for first name
    first_name = Column(String(128), nullable=True)

    # Column for last name
    last_name = Column(String(128), nullable=True)