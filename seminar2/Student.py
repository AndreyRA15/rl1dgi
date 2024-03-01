# from Person import Person
class Student():
    group = 1
    semestr = 6
    chair = "РЛ1"
    lastSessionPass = False

    def __init__(self, groupNum, chairName):
        # super().__init__("AA", 34)
        self.group = groupNum
        self.chair = chairName
        
        


    def getInfo(self):
        print("Учится в группе", self.chair+"-"+str(self.semestr)+str(self.group))
        if self.lastSessionPass: 
            print("Сессия сдана") 
        else:
            print("Сессия провалена")

s = Student(2,"RL1")

s.getInfo()

# print(s.Age)
