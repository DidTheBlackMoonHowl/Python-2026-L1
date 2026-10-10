import math
import numpy as np

# Classes
class student:
    def __init__(self, sID: str, sName: str, sBirth: str):
        self.id = sID
        self.name = sName
        self.birth = sBirth

    def __str__(self):
        return f"{self.id}"

    def outPrint(self):
        print(f"ID: {self.id}. Name: {self.name}. Date of Birth: {self.birth}")

    def getID(self):
        return self.id

    def getName(self):
        return self.name

    def getDoB(self):
        return self.birth

class course:
    def __init__(self, sID: str, sName: str, iCredit: int):
        self.id = sID
        self.name = sName
        self.credit = iCredit
            
    def __str__(self):
        return f"{self.id}"

    def outPrint(self):
        print(f"ID: {self.id}. Name: {self.name}. Credits: {self.credit}")

    def getID(self):
        return self.id

    def getName(self):
        return self.name

    def getPoint(self):
        return self.credit

class mark:
    def __init__(self, fMark: float, studentIn: student, courseIn: course):
        self.course = courseIn
        self.courseID = courseIn.id
        self.courseName = courseIn.name
        self.student = studentIn
        self.studentID = studentIn.id
        self.studentName = studentIn.name
        self.markPoint = math.floor(fMark*10)/10
        self.creditPoint = courseIn.credit

    def __str__(self):
        return "Mark"

    def outPrint(self):
        print(f"Course ID: {self.courseID}. Course Name: {self.courseName}")
        print(f"Student ID: {self.studentID}. Student Name: {self.studentName}. Mark: {self.markPoint}. Credits: {self.creditPoint}")

    def getStudent(self):
        return self.student

    def getStudentID(self):
        return self.studentID

    def getCourse(self):
        return self.course

    def getCourseID(self):
        return self.courseID

    def getMark(self):
        return self.markPoint

    def getCredit(self):
        return self.creditPoint

# Functions
# Generic Functions
def addObjects(lList: list, oObject: object):
    lList.append(oObject)

def getObject(lList: list, sID: str):
    for obj in lList:
        if (((type(obj) == student) or (type(obj) == course)) and (obj.getID() == sID)):
            return obj
    return -1

def listObjects(lList: list):
    for obj in lList:
        if ((type(obj) == student)
            or (type(obj) == course) 
            or (type(obj) == mark)):
            obj.outPrint()
    print()

# Student Functions
def addStudents(lStudents: list, iAmount: int = 1):
    for i in range(0,iAmount):
        sID = input("Enter Student ID: ")
        sName = input("Enter Student Name: ")
        sDoB = input("Enter Student Birthday: ")
        print()
        addObjects(lStudents, student(sID, sName, sDoB))

# Course Functions
def addCourses(lCourses: list, iAmount: int = 1):
    for i in range(0,iAmount):
        sID = input("Enter Course ID: ")
        sName = input("Enter Course Name: ")
        iCredits = int(input("Enter Course Credit: "))
        print()
        addObjects(lCourses, course(sID, sName, iCredits))

# Mark Functions
def addMarks(lStudents: list, lCourses: list, lMarks: list, iMode: int = 0):
    # iMode = 0: By Course. 1: By Student
    # Add marks by course: Add marks for all student in a course
    # Add marks by student: Add marks in all course for a student
    amount = len(lStudents)
    ID: str
    # Selection
    if (iMode):
        # Enter marks by student, so only 1 student selected then enter marks for courses
        # amount = number of courses
        ID = input("Enter Student ID: ")
        amount = len(lCourses)
        if (amount == 0):
            print("Enter course informations first\n")
    else:
        # Enter marks by course, so only 1 course selected then enter marks for students
        ID = input("Enter Course ID: ")
        if (amount == 0):
            print("Enter student informations first\n")

    # Input
    for i in range(0, amount):
        if (iMode):
            Mark = float(input(f"Enter student {ID} - course {lCourses[i].id} mark: "))
            lMarks.append(mark(Mark, getObject(lStudents, ID), lCourses[i]))
        else:
            Mark = float(input(f"Enter course {ID} - student {lStudents[i].id} mark: "))
            lMarks.append(mark(Mark, lStudents[i], getObject(lCourses, ID)))

def listMark(lMarks: list, sID: str = "", iMode: int = 0):
    # 1: By Courses
    # 2: By Students
    # Else: All
    for obj in lMarks:
        if (iMode == 2):
            if (obj.studentID == sID): 
                obj.outPrint()
        elif (iMode == 1):
            if (obj.courseID == sID):
                obj.outPrint()
        else:
            obj.outPrint()

# GPA Related Functions
def getSumPoint(lMarks: list, sID: str, iMode = 0):
    p = 0
    for obj in lMarks:
        if obj.getStudentID() == sID:
            if (iMode): # Mode == 1 -> Total Credits
                p += obj.getCredit()
            else:       # Mode == 0 -> Total Weighted Marks
                p += obj.getMark()/5*obj.getCredit()
    return p

def getGPA(lMarks: list, sID: str):
    return getSumPoint(lMarks, sID)/getSumPoint(lMarks, sID, 1)

def getGPAS(lMarks: list):
    ID = np.array([])
    GPA = np.array([])
    for obj in lMarks:
        # If the student id is new
        if (obj.getStudentID() in ID) == False:
            ID = np.append(ID, obj.getStudentID())
            GPA = np.append(GPA, round(getGPA(lMarks, obj.getStudentID()), 3))
    GPAs = np.array([ID, GPA])
    return GPAs

def sortGPA(aGPAs: np.ndarray):
    ID = aGPAs[0]
    GPA = aGPAs[1]
    # [::-1] Is descending arrange
    # For ascending order, remove the slicing [::-1]
    sortedIndices = np.argsort(GPA)[::-1]
    ID = ID[sortedIndices]
    GPA = GPA[sortedIndices]
    return np.array([ID, GPA])

def main():
    sList = []
    cList = []
    mList = []
    enterStudents = 0
    enterCourses = 0
    enterMarks = 0
    while True:
        print("Available options:")
        if (enterStudents and enterCourses):
            if (enterMarks):
                print("0. Exit loop \n1. Enter student informations \n2. Enter course informations \n3. Enter marks \n4. List students \n5. List courses \n6. List marks \n7. List student by GPA")
            else:
                print("0. Exit loop \n1. Enter student informations \n2. Enter course informations \n3. Enter marks \n4. List students \n5. List courses")
        else:
            print("0. Exit loop \n1. Enter student informations \n2. Enter course informations")
        print()
    
        c = int(input("Enter a number to select: "))
        t = 0
        if (c == 0):
            return
        elif (c == 1):
            enterStudents = 1
            print()
            t = int(input("Enter number of students: "))
            print()
            addStudents(sList, t)
        elif (c == 2):
            enterCourses = 1
            print()
            t = int(input("Enter number of courses: "))
            print()
            addCourses(cList, t)
        elif (c == 3):
            if (enterStudents and enterCourses):
                enterMarks = 1
                print()
                print("Mode: \n0. Enter mark by course \n1. Enter mark by student")
                t = int(input("Enter mode: "))
                addMarks(sList, cList, mList, t)
            else:
                print("The option is not available\n")
        elif (c == 4):
            if (enterStudents):
                listObjects(sList)
            else:
                print("The option is not available\n")
        elif (c == 5):
            if (enterCourses):
                listObjects(cList)
            else:
                print("The option is not available\n")
        elif (c == 6):
            if (enterMarks):
                print("Mode: \n0. List all \n1. List by student \n2. List by course")
                t1 = int(input("Select mark listing mode: "))
                t2 = ""
                if (t1 == 1):
                    t2 = input("Enter student id: ")
                elif (t1 == 2):
                    t2 = input("Enter course id: ")
                listMark(mList, t2, t1)
            else:
                print("The option is not available\n")
        elif (c == 7):
            if (enterMarks):
                gArray = sortGPA(getGPAS(mList))
                length = np.shape(gArray)[1]
                for i in range(0, length):
                    IDString = str(gArray[0, i])
                    GPA = (float(gArray[1, i]))
                    for obj in sList:
                        if (IDString == obj.getID()):
                            print(f"ID: {obj.getID()}. Name: {obj.getName()}. Date of Birth: {obj.getDoB()}. GPA: {GPA}")
                print()
            else:
                print("The option is not available\n")
        else:
            print("The option is not available\n")
main()
