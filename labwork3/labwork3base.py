# Classes
class student:
    index = -1
    def __init__(self, iID: int, sName: str, sBirth: str):
        self.id = iID
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

    def getIndex(self):
        return self.index

    def setIndex(self, iIndex: int):
        self.index = iIndex

class course:
    index = -1
    def __init__(self, iID: int, sName: str, iCredit: int):
        self.id = iID
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

    def getIndex(self):
        return self.index

    def setIndex(self, iIndex: int):
        self.index = iIndex

class mark:
    def __init__(self, fMark: float, student: student, course: course):
        self.courseID = course.id
        self.courseName = course.name
        self.studentID = student.id
        self.studentName = student.name
        self.markPoint = fMark
        self.creditPoint = course.credit

    def __str__(self):
        return "Mark"

    def outPrint(self):
        print(f"Course ID: {self.courseID}. Course Name: {self.courseName}")
        print(f"Student ID: {self.studentID}. Student Name: {self.studentName}. Mark: {self.markPoint}. Credits: {self.creditPoint}")

# Functions
# Generic
def addObjects(lList: list, oObject: object):
    lList.append(oObject)
    if ((type(oObject) == student) or type(oObject) == course):
        oObject.setIndex(len(lList) - 1)

def getObject(lList: list, iID: int):
    for obj in lList:
        if (((type(obj) == student) or (type(obj) == course)) and (obj.getID() == iID)):
            return obj
    return -1

def listObjects(lList: list):
    for obj in lList:
        if ((type(obj) == student)
            or (type(obj) == course) 
            or (type(obj) == mark)):
            obj.outPrint()
    print()

'''def getObjectByIndex(lList, iIndex):
    return lList[iIndex]'''

# Student Functions
def addStudents(lStudents: list, iAmount: int = 1):
    for i in range(0,iAmount):
        iID = int(input("Students Student ID: "))
        sName = input("Enter Student Name: ")
        sDoB = input("Enter Student Birthday: ")
        s = student(iID, sName, sDoB)
        addObjects(lStudents, s)

# Course Functions
def addCourses(lCourses: list, iAmount: int = 1):
    for i in range(0,iAmount):
        iID = int(input("Enter Course ID: "))
        sName = input("Enter Course Name: ")
        iCredits = int(input("Enter Course Credit: "))
        c = course(iID, sName, iCredits)
        addObjects(lCourses, c)

# Mark Functions
def addMarks(lStudents: list, lCourses: list, lMarks: list, iMode: int = 0):
    # iMode = 0: By Course. 1: By Student
    # Add marks by course: Add marks for all student in a course
    # Add marks by student: Add marks in all course for a student
    amount = len(lStudents)
    ID: int
    # Selection
    if (iMode):
        # Enter marks by student, so only 1 student selected then enter marks for courses
        # amount = number of courses
        ID = int(input("Enter Student ID"))
        amount = len(lCourses)
    else:
        # Enter marks by course, so only 1 course selected then enter marks for students
        ID = int(input("Enter Course ID: "))

    # Input
    for i in range(0, amount):
        if (iMode):
            Mark = float(input(f"Enter student {ID} - course {lCourses[i].id} mark: "))
            lMarks.append(mark(Mark, getObject(lStudents, ID), lCourses[i]))
        else:
            Mark = float(input(f"Enter course {ID} - student {lStudents[i].id} mark: "))
            lMarks.append(mark(Mark, lStudents[i], getObject(lCourses, ID)))

def listMark(lMarks: list, iID: int, iMode: int = 0):
    # 1: By Courses
    # 2: By Students
    # Else: All
    for obj in lMarks:
        if (iMode == 1):
            if (obj.studentID == iID): 
                obj.outPrint()
        elif (iMode == 0):
            if (obj.courseID == iID):
                obj.outPrint()
        else:
            obj.outPrint()
'''
# Quick Test
sList = []
cList = []
mList = []
addObjects(sList, student(2510332, "Nguyen Viet Hoang", "26 08 2007"))
addObjects(sList, student(2510333, "Nguyen Viet Hoang", "26 08 2007"))
addObjects(cList, course(1, "APP", 4))
addObjects(cList, course(2, "OOP", 4))
addObjects(mList, mark(12.9, sList[0], cList[0]))
addObjects(mList, mark(12.5, sList[0], cList[1]))
addObjects(mList, mark(13, sList[1], cList[0]))
addObjects(mList, mark(14, sList[1], cList[1]))
listObjects(sList)
listObjects(cList)
listObjects(mList)
'''