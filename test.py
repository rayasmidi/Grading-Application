import csv
import sys

def main():
    while(BKX):
        print("\nTo add a student press 1")
        print("To edit a student detail press 2")
        print("To delete a student press 3")
        print("To Display Data press 4")
        print("To exit the program press 5")
        Choice = int(input("Enter Your Choice: "))
        if (Choice == 5):
            print("Exiting the program")
            sys.exit(0)
        selection(Choice)

def FindGrade(marks):
    # marks=marks/8
    if marks>=90:
        return "A"
    elif marks>=80 and marks <90:
        return "B"
    elif marks>=70 and marks <80:
        return "C"
    elif marks>=60 and marks <70:
        return "D"
    else:
        return "F"

class student:
    def __init__(self):
        self.name = ""
        self.grades = {"HK1": 0, "HK2": 0, "HK3": 0, "HK4": 0, "TK1": 0, "TK2": 0, "TK3": 0, "TK4": 0}
        self.marks = {}

    def add(self):
        print("Adding A Student")
        Name=input("Enter Name : ")
        self.name = Name
        BKX = True
        while (BKX):
            HW_1=float(input("Enter First Homework Marks : "))
            if (HW_1>=0)&(HW_1<=100):
                self.grades["HK1"] = HW_1
                BKX = False
            else:
                print("Enter in range 0 - 100")
        BKX = True
        while (BKX):
            HW_2=float(input("Enter second Homework Marks : "))
            if (HW_2>=0)&(HW_2<=100):
                self.grades["HK2"] = HW_2
                BKX = False
            else:
                print("Enter in range 0 - 100")
        BKX = True
        while (BKX):
            HW_3=float(input("Enter third Homework Marks : "))
            if (HW_3>=0)&(HW_3<=100):
                self.grades["HK3"] = HW_3
                BKX = False
            else:
                print("Enter in range 0 - 100")
        BKX = True
        while (BKX):
            HW_4=float(input("Enter Fourth Homework Marks : "))
            if (HW_4>=0)&(HW_4<=100):
                self.grades["HK4"] = HW_4
                BKX = False
            else:
                print("Enter in range 0 - 100")
        BKX = True
        while (BKX):
            Test_1=float(input("Enter First Test Marks : "))
            if (Test_1>=0)&(Test_1<=100):
                self.grades["TK1"] = Test_1
                BKX = False
            else:
                print("Enter in range 0 - 100")
        BKX = True
        while (BKX):
            Test_2=float(input("Enter Second Test Marks : "))
            if (Test_2>=0)&(Test_2<=100):
                self.grades["TK2"] = Test_2
                BKX = False
            else:
                print("Enter in range 0 - 100")
        BKX = True
        while (BKX):
            Test_3=float(input("Enter Third Test Marks : "))
            if (Test_3>=0)&(Test_3<=100):
                self.grades["TK3"] = Test_3
                BKX = False
            else:
                print("Enter in range 0 - 100")
        BKX = True
        while (BKX):
            Test_4=float(input("Enter Fourth Test Marks : "))
            if (Test_4>=0)&(Test_4<=100):
                self.grades["TK4"] = Test_4
                BKX = False
            else:
                print("Enter in range 0 - 100")
        for grade in self.grades:
            self.marks[grade] = FindGrade(self.grades[grade])
            
    def print(self):
        stri = ""
        for grade in self.grades:
            stri = stri + f'Your grade for {grade} is {self.grades[grade]}:{self.marks[grade]}\n'
        print(stri)

student = student()
student.add()
student.print()