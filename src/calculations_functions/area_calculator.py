class AreaCalculator:


    def rectangle_calculations(self,length, width):

        if length <= 0 or width <= 0:
            raise ValueError("The length and the width have to be greater than 0")
        else:
            return length * width



