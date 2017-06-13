class Box:
    def __init__(self, width, height, depth):
        self.width = width
        self.heigth = height
        self.depth = depth

    def __call__(self):
        volume = self.width * self.heigth * self.depth
        print("Объём равен", volume)


obj = Box(10, 20, 30)
obj()
