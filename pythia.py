import random

class PyPythia():
    def __init__(self):
        self.results = []

    def generate(self):
        present = True
        while present:
            mynum = int(random.random()*9007199254740992)
            if mynum not in self.results:
                present = False

        return mynum

    def reset(self):
        self.results = []

