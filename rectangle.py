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

