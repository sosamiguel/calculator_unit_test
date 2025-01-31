import math
class AreaCalculator:

    def rectangle(self,length, width):

        if length <= 0 or width <= 0:
            raise ValueError("The length and the width have to be greater than 0")
        else:
            return length * width


    def circle(self, r):
        if r <= 0:
            raise ValueError("The radius have to be greater than 0")
        return math.pi * r * r

