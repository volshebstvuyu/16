class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __call__(self):
        return self.width, self.height

    def getSizes(self):
        return self.getWidth(), self.getHeight()

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getArea(self):
        return self.width * self.height

class Square:
    def __init__(self, a):
        self.a = a

class Circle:
    def __init__(self, r):
        self.r = r
    def getArea(self):
        return 3.14 * self.r ** 2