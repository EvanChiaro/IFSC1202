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
        self.Size = size
        x = []
        #for i in range(size):
        #    x.append(" ")
      #     self.Canvas.append(x)
        for i in range(size):
            self.Canvas.append([" "] * size)
    def printsketch(self):
        print("+", end="")
        for i in range(self.Size):
            print("-", end="")
        print("+")
        for i in range(len(self.Canvas)):
            print("|", end = "")
            for j in range(self.Size):
                print(self.Canvas[-i-1][j], end = "")
            print('|')
        print("+", end="")
        for i in range(self.Size):
            print("-", end="")
        print("+")
    def penup(self):
        self.Pen = "U"
    def pendown(self):
        self.Pen = "D"
    def turnleft(self):
        if self.Direction == "U":
            self.Direction = "L"
        elif self.Direction == "L":
            self.Direction = "D"
        elif self.Direction == "D":
            self.Direction = "R"
        elif self.Direction == "R":
            self.Direction = "U"
    def turnright(self):
        if self.Direction == "U":
            self.Direction = "R"
        elif self.Direction == "L":
            self.Direction = "U"
        elif self.Direction == "D":
            self.Direction = "L"
        elif self.Direction == "R":
            self.Direction = "D"
    def move(self,distance):
        distance = distance.split(',')
        for i in range(int(distance[1])):
            if self.Pen == "D":
                self.Canvas[self.Ypos][self.Xpos] = '*'
            if self.Direction == "U":
                self.Ypos += 1
            elif self.Direction == "D":
                self.Ypos -= 1
            elif self.Direction == "R":
                self.Xpos += 1
            elif self.Direction == "L":
                self.Xpos -= 1



#main function
instructfile = open("Cshape.txt")
length = instructfile.readlines()
instructfile.close()
instructfile = open("Cshape.txt")
instruct = instructfile.readline()
size = int(instruct)
sketch1 = Sketch()
sketch1.init(size)
for i in range(len(length)):
    instruct = instructfile.readline()
    instruct = instruct.strip()
    ins = instruct.split(',')
    if ins[0] == "1":
        sketch1.penup()
    elif ins[0] == "2":
        sketch1.pendown()
    elif ins[0] == "3":
        sketch1.turnright()
    elif ins[0] == "4":
        sketch1.turnleft()
    elif ins[0] == "5":
        sketch1.move(instruct)
    elif ins[0] == "6":
        sketch1.printsketch()
instructfile.close()

print("X = {}  Y = {}  Direction = {}".format(sketch1.Xpos, sketch1.Ypos,sketch1.Direction))