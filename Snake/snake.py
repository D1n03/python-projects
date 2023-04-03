from msilib.schema import SelfReg


class Snake():
    def __init__(self):
        self.x = 50
        self.y = 50

        self.body = [(50, 50), (50, 40), (50, 30), (50, 20)]
        self.direction = "R"
    
    def move(self, foodPos):
        if self.direction == "R":
            self.x += 10
        if self.direction == "L":
            self.x -= 10
        if self.direction == "U":
            self.y -= 10
        if self.direction == "D":
            self.y += 10

        self.body.insert(0, (self.x, self.y))

        if self.x == foodPos[0] and self.y == foodPos[1]:
            return True

        self.body.pop()
        return False
    
    def changeDir(self, newDir):
        if newDir == "R" and not self.direction == "L":
            self.direction = "R"
        if newDir == "L" and not self.direction == "R":
            self.direction = "L"
        if newDir == "U" and not self.direction == "D":
            self.direction = "U"
        if newDir == "D" and not self.direction == "U":
            self.direction = "D"
        
    def CheckisDead(self):
        if self.x > 490 or self.x < 0 or self.y > 490 or self.y < 0:
            return True
        
        for bodyPart in self.body[1:]:
            if (self.x, self.y) == bodyPart:
                return True
            
        return False