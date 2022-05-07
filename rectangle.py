class Rectangle:
    def __init__(self, width, heigth):
        self.width = width
        self.height = heigth
    def getWidth(self):
        return self.width

    def getHeigth(self):
        return self.height

    def getArea(self):
        return self.width * self.height
