#object initialize
class Sketch():
    def __init__(self, size=0, xpos=0, ypos=0, direction="U", pen="U"):
        self.Size = size
        self.Xpos = xpos
        self.Ypos = ypos
        self.Direction = direction
        self.Pen = pen
        self.Canvas = []
    def init(self,size):
        a = []
        direcfile = open("Cshape.txt")
        direction = direcfile.readline()
        size = int(direction)
        for i in range(size):
            a.append(" ")
        for i in range(size):
            self.Canvas.append(a)
    def printsketch():
        print("+", end="")
        for i in range(self.Size):
            print("-", end="")
        print("+")
        for i in range(len(canvas)):
            print("|", end = "")
            for j in range(0, len(a), -1):
                print(self.Canvas[i][j], end = "")
            print('|')
        print("+", end="")
        for i in range(self.Size):
            print("-", end="")
        print("+")
    def penup():
        self.Pen = "U"
    def pendown():
        self.Pen = "D"
    def turnleft():
        if self.Direction == "U":
            self.Direction = "L"
        elif self.Direction == "L":
            self.Direction = "D"
        elif self.Direction == "D":
            self.Direction = "R"
        elif self.Direction == "R":
            self.Direction = "U"
    def turnright():
        if self.Direction == "U":
            self.Direction = "R"
        elif self.Direction == "L":
            self.Direction = "U"
        elif self.Direction == "D":
            self.Direction = "L"
        elif self.Direction == "R":
            self.Direction = "D"
    def move(self,distance):
        distance = distane.split(',')
        for i in range(int(distance)):
            