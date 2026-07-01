# https://www.codewars.com/kata/54fe05c4762e2e3047000add

CREW = 1.5

class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

    def is_worth_it(self):
        return True if self.draft - (self.crew * CREW) >= 20 else False