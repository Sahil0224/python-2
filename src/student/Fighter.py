from src.student.Character import Character


class Fighter(Character):
    # method to return 
    def __repr__(self):
        return f"Fighter: {self.hit_points} hit points."