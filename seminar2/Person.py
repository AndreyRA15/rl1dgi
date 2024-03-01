from enum import Enum

class Gender(Enum):
    Male = 0
    Female = 1

class Person():
    def __init__(self, name, gender):
        self.Name = name
        self.Age = 0
        self.Gender= gender
    def Birthday(self):
        self.Age += 1

    # def __repr__(self) -> str:
    #     return self.Name + ", Age "+ str(self.Age)+ ", Gender " + Gender(self.Gender).name
p = Person("Bob", Gender.Male)

if __name__ == "__main__":
    print(p)
    p.Birthday()
    print(p)


