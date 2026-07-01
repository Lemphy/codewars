# https://www.codewars.com/kata/568018a64f35f0c613000054

class Guesser:
    def __init__(self, number: int, lives: int):
        self.number = number
        self.lives = lives

    def guess(self, n : int) -> bool:
        if self.lives > 0:
            if n == self.number:
                return True
            else:
                self.lives -= 1
                return False
        else:
            raise ValueError ('Lives ran out should throw')

    def __str__(self) -> str:
        return (f'{self.number}\n'
                f'{self.lives}')