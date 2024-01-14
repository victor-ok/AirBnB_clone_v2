#!/usr/bin/python3
"""defines a user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    a user that inherits from the BaseModel

    attr:
        email (str): the email of the user.
        password (str): the password of the user.
        first_name (str): the first name of the user.
        lat_name (str): the last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
