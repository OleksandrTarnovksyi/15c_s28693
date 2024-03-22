import math

from square_generator import SquareGenerator


class CubicGenerator(SquareGenerator):
    def e_squares(self, start, end):
        if start > end:
            print("Invalid")
        else:
            squares = [number * number*number for number in range(start, end)]
            return [math.sqrt(square) for square in squares]