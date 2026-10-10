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
        self.markPoint = fMark
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

'''def getObjectByIndex(lList, iIndex):
    return lList[iIndex]'''

# Student Functions
def addStudents(lStudents: list, iAmount: int = 1):
    for i in range(0,iAmount):
        sID = input("Enter Student ID: ")
        sName = input("Enter Student Name: ")
        sDoB = input("Enter Student Birthday: ")
        addObjects(lStudents, student(sID, sName, sDoB))

# Course Functions
def addCourses(lCourses: list, iAmount: int = 1):
    for i in range(0,iAmount):
        sID = input("Enter Course ID: ")
        sName = input("Enter Course Name: ")
        iCredits = int(input("Enter Course Credit: "))
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
    else:
        # Enter marks by course, so only 1 course selected then enter marks for students
        ID = input("Enter Course ID: ")

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
        if (iMode == 1):
            if (obj.studentID == sID): 
                obj.outPrint()
        elif (iMode == 0):
            if (obj.courseID == sID):
                obj.outPrint()
        else:
            obj.outPrint()

'''
# Quick Test
sList = []
cList = []
mList = []
addObjects(sList, student("2510332", "Nguyen Viet Hoang", "26 08 2007"))
addObjects(sList, student("2510333", "Nguyen Viet Hoang", "26 08 2007"))
addObjects(cList, course("B2.ICT1", "OOP", 4))
addObjects(cList, course("B2.ICT2", "APP", 4))
addObjects(mList, mark(12.236, sList[1], cList[0]))
addObjects(mList, mark(12.414, sList[1], cList[1]))
addObjects(mList, mark(16.18, sList[0], cList[0]))
addObjects(mList, mark(13.14, sList[0], cList[1]))
listObjects(sList)
listObjects(cList)
listObjects(mList)
'''
