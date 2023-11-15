import random

class Character:
    # constructor with one paramerter 
    def __init__(self, hit_points):
        self.hit_points = hit_points
    # fight method with one parameter character
    def fight(self, character):
        # generate a random number between 1 to 20
        random_number = random.randint(1, 20)
        # reduce the hit points of other character by random number
        character.hit_points -= random_number
        # making sure to hit point and do not fall below zero
        if character.hit_points < 0:
            character.hit_points = 0