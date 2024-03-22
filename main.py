import math


class SquareGenerator:
    def e_squares(self, start, end):
        squares = [number * number for number in range(start, end)]
        return [math.sqrt(square) for square in squares]
