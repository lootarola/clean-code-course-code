class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, origin, base, height):
        self.origin = origin
        self.base = base
        self.height = height
        self.area = base*height

    def print_coordinates(self):
        top_right = self.origin.x + self.base
        bottom_left = self.origin.y + self.height
        print('Starting Coordinate (X)): ' + str(self.origin.x))
        print('Starting Coordinate (Y)): ' + str(self.origin.y))
        print('End Coordinate (X) (Top Right): ' + str(top_right))
        print('End Coordinate (Y) (Bottom Left): ' + str(bottom_left))


def build_rectangle():
    rectangle_origin = Coordinate(50, 100)
    rectangle = Rectangle(rectangle_origin, 90, 10)
    return rectangle


rectangle = build_rectangle()

print(rectangle.area)
rectangle.print_coordinates()
