#!/usr/bin/python3
"""defines a state class"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    reps a state

    attr:
        name (str): the name of the state
    """

    name = ""
