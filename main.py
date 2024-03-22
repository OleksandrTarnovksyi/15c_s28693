import math


class SquareGenerator:
    def e_squares(self, start, end):
        if start > end:
            print("Invalid")
        else:
            squares = [number * number for number in range(start, end)]
            return [math.sqrt(square) for square in squares]
