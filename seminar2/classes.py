


class Student():
    group = 1
    semestr = 6
    chair = "РЛ1"
    lastSessionPass = False

    def __init__(self, groupNum, chairName):
        self.group = groupNum
        self.chair = chairName
        


    def getInfo(self):
        print("Учится в группе", self.chair+"-"+str(self.semestr)+str(self.group))
        if self.lastSessionPass: 
            print("Сессия сдана") 
        else:
            print("Сессия провалена")




someStudent = Student()

# someStudent.chair = "РТ1"

someStudent.lastSessionPass  = True

someStudent.getInfo()
    