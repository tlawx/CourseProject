from Treatment import Treatment


class Category:
    def __init__(self, name, letter, treatments=[]):
        self.letter = letter
        self.name = name
        self.treatments = treatments

