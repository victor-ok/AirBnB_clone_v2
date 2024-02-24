#!/usr/bin/python3
"""defines a city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    reps a city

    attr:
        state_id (str): the state id
        name (str): the name of the city
    """

    state_id = ""
    name = ""
