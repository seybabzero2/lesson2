# class Student:
#     def __init__(self):
#         self.height = 165
#         print("OK")
#
# firstStudent = Student()
# print(firstStudent)
# print("Height: " + str(firstStudent.height))

# class Student:
#     kolichestvo = 0;
#     def __init__(self, height):
#         self.height = height
#         self.kolichestvo += 1
#
# andre = Student(height = 150)
# kate = Student(height = 160)
# print(kate.height)
# print(andre.height)
# print(andre.kolichestvo)
# print(kate.kolichestvo)

# class Student:
#     def __init__(self, name = None):
#         self.Name = name
#     def text(self):
#         return f"My name is {self.Name}"
#
# nick = Student(name = "Roberto")
# print(nick.text())

import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 0
        self.progress = 0
        self.alive = True
    def to_study(self):
        print("UCHITSA")
        self.progress += 0.12
        self.gladness -= 5
    def to_sleep(self):
        print("Отдохнуть бы конечно не помешало")
        self.gladness +=3
    def to_chill(self):
        print("Три в ряд")
        self.gladness += 5
        self.progress -= 0.1
    def is_alive(self):
        if (self.progress < -0.5):
            print("YOU DIED!")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression")
            self.alive = False
        elif self.progress > 5:
            print("Extern")
            self.alive = False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
    def live(self, day):
        day = "Day: " + str(day) + " of " + self.name + " suffering"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
            self.end_of_day()
            self.is_alive()
nick = Student(name = "Anatolii")
for day in range(9999):
    if nick.alive == False:
        break
    nick.live(day)
