import logging


class Person:
    """
    A class representing a person.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.

    Methods:
        display_info(): Displays the name and age of the person using logging.
    """
    
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

    def display_info(self):
        logging.info(f"Name: {self.name}")
        logging.info(f"Age: {self.age}")




