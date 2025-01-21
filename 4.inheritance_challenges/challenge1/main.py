class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get_area(self):
        pass

    def get_perimeter(self):
        perimeter = self.__length * 4
        return perimeter
        


class Square(Rectangle):
    def __init__(self, length):
        self.__length = length

