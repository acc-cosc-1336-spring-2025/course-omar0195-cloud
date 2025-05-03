import random

class die:

    def __init__(self):

        die.__roll_value = None

    def roll (self):
        die.__roll_value = random.randint(1, 6)

    def get_rolled_value(self):
        return die.__roll_value

    def __str__(self):
        return f"The rolled value is {die.__roll_value}"
    