# Open in terminal only. Will return error in IDLE
import math
import numpy as np
import curses
from curses import wrapper
stdscr = curses.initscr()

# Classes
class student:
    def __init__(self, sID: str, sName: str, sBirth: str):
        self.id = sID
        self.name = sName
        self.birth = sBirth

    def __str__(self):
        return f"{self.id}"

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
def outPrint(oObject: object, scr = stdscr):
    if (type(oObject) == student):
        msg = f"ID: {oObject.id}. Name: {oObject.name}. Date of Birth: {oObject.birth}\n"
        scr.addstr(msg)
        scr.refresh()
    elif (type(oObject) == course):
        msg = f"ID: {oObject.id}. Name: {oObject.name}. Credits: {oObject.credit}\n"
        scr.addstr(msg)
        scr.refresh()
    elif (type(oObject) == mark):
        msg = f"Course ID: {oObject.courseID}. Course Name: {oObject.courseName}\n"
        scr.addstr(msg)
        scr.refresh()
        msg = f"Student ID: {oObject}. Student Name: {oObject.studentName}. Mark: {oObject.markPoint}. Credits: {oObject.creditPoint}\n"
        scr.addstr(msg)
        scr.refresh()

def addObjects(lList: list, oObject: object):
    lList.append(oObject)

def getObject(lList: list, iID: int):
    for obj in lList:
        if (((type(obj) == student) or (type(obj) == course)) and (obj.getID() == iID)):
            return obj
    return -1

def listObjects(lList: list, scr = stdscr):
    scr.clear()
    for obj in lList:
        if (type(obj) == student):
            outPrint(obj, scr)
        elif (type(obj) == course):
            outPrint(obj, scr)
        elif (type(obj) == mark):
            outPrint(obj, scr)
        else:
            return -1
    stdscr.getkey()

# Student Functions
def addStudents(lStudents: list, iAmount: int = 1, scr = stdscr):
    scr.clear()
    l = 0
    for i in range(0,iAmount):
        msg = "Enter Student ID: "
        scr.addstr(msg)
        scr.refresh()
        sID = stdscr.getstr(l, len(msg), 16).decode("utf-8")

        msg = "Enter Student Name: "
        scr.addstr(msg)
        scr.refresh()
        sName = stdscr.getstr(l + 1, len(msg), 100).decode("utf-8")

        msg = "Enter Student Date of Birth: "
        scr.addstr(msg)
        scr.refresh()
        sDoB = stdscr.getstr(l + 2, len(msg), 10).decode("utf-8")

        l += 3
        addObjects(lStudents, student(sID, sName, sDoB))

# Course Functions
def addCourses(lCourses: list, iAmount: int = 1, scr = stdscr):
    scr.clear()
    l = 0
    for i in range(0,iAmount):
        msg = "Enter Course ID: "
        scr.addstr(msg)
        scr.refresh()
        sID = stdscr.getstr(l, len(msg), 16).decode("utf-8")

        msg = "Enter Course Name: "
        scr.addstr(msg)
        scr.refresh()
        sName = stdscr.getstr(l + 1, len(msg), 100).decode("utf-8")

        msg = "Enter Course Credit: "
        scr.addstr(msg)
        scr.refresh()
        iCredits = int(stdscr.getstr(l + 2, len(msg), 1).decode("utf-8"))

        l += 3
        addObjects(lCourses, course(sID, sName, iCredits))

# Mark Functions
def addMarks(lStudents: list, lCourses: list, lMarks: list, iMode: int = 0, scr = stdscr):
    scr.clear()
    l = 0
    amount: int
    ID: str
    msg: str
    # Selection
    amount = len(lStudents)
    if (iMode == 2):
        msg = "Enter Student ID: "
        amount = len(lCourses)
    elif (iMode == 1):
        msg = "Enter Course ID: "
        amount = len(lStudents)

    if (iMode != 0):
        scr.addstr(msg)
        scr.refresh()
        ID = stdscr.getstr(l, len(msg), 16).decode("utf-8")
        l += 1

    # Input
    for i in range(0, amount):
        if (iMode == 2):
            msg = f"Enter student {ID} - course {lCourses[i].id} mark: "
            scr.addstr(msg)
            scr.refresh()
            Mark = float(stdscr.getstr(l, len(msg), 7).decode("utf-8"))
            lMarks.append(mark(Mark, getObject(lStudents, ID), lCourses[i]))
            l += 1
        elif (iMode == 1):
            msg = f"Enter course {ID} - student {lStudents[i].id} mark: "
            scr.addstr(msg)
            scr.refresh()
            Mark = float(stdscr.getstr(l, len(msg), 7).decode("utf-8"))
            lMarks.append(mark(Mark, lStudents[i], getObject(lCourses, ID)))
            l += 1
        else:
            for j in range(0, len(lCourses)):
                msg = f"Enter student {lStudents[i].id} - courses {lCourses[j].id} mark: "
                scr.addstr(msg)
                scr.refresh()
                Mark = float(stdscr.getstr(l, len(msg), 7).decode("utf-8"))
                lMarks.append(mark(Mark, lStudents[i], lCourses[j]))
        

def listMark(lMarks: list, sID: str = "", iMode: int = 0, scr = stdscr):
    scr.clear()
    for obj in lMarks:
        if (iMode == 2):
            if (obj.studentID == sID):
                outPrint(obj, scr)
        elif (iMode == 1):
            if (obj.courseID == sID):
                outPrint(obj, scr)
        else:
            outPrint(obj, scr)
    stdscr.getkey()

# GPA Related Functions
def getSumPoint(lMarks: list, sID: str, iMode = 0):
    p = 0.0
    for obj in lMarks:
        if obj.getStudentID() == sID:
            if (iMode):
                p += obj.getCredit()
            else:
                p += obj.getMark()/5*obj.getCredit()
    return p

def getGPA(lMarks: list, sID: str):
    return getSumPoint(lMarks, sID)/getSumPoint(lMarks, sID, 1)

def getGPAS(lMarks: list):
    ID = np.array([])
    GPA = np.array([])
    for obj in lMarks:
        if (obj.getStudentID() in ID) == False:
            ID = np.append(ID, obj.getStudentID())
            GPA = np.append(GPA, round(getGPA(lMarks, obj.getStudentID()), 3))
    GPAs = np.array([ID, GPA])
    return GPAs

def sortGPA(aGPAs: np.ndarray, ascend: int = 0):
    ID = aGPAs[0]
    GPA = aGPAs[1]
    sortedIndices = np.argsort(GPA)[::-1]    
    if (ascend):
        sortedIndices = np.argsort(GPA)
    ID = ID[sortedIndices]
    GPA = GPA[sortedIndices]
    return np.array([ID, GPA])

def sortStudentList(lStudents: list, aGPAs: np.ndarray):
    sortedList = []
    length = np.shape(aGPAs)[1]
    for i in range(0, length):
        IDString = str(aGPAs[0, i])
        for obj in lStudents:
            if (IDString == obj.getID()):
                addObjects(sortedList, obj)
    return sortedList;

def main(stdscr):
    curses.echo() # Show typed character
    sList = []
    cList = []
    mList = []
    gArray = np.ndarray
    enteredStudents = 0
    enteredCourses = 0
    enteredMarks = 0
    msg = ""
    c: int
    t: int
    while True:
            stdscr.clear()
            l = 0

            msg = f"Available options: \n"
            stdscr.addstr(msg)
            stdscr.refresh()
            l += 1
            if (enteredStudents and enteredCourses):
                if (enteredMarks):
                    msg = "1. Enter Student Informations \n2. Enter Course Informations \n3. Enter Marks \n4. List Students \n5. List Courses \n6. List Marks \n7. List Students by GPA \n0. Exit \n"
                    l += 8
                else:
                    msg = "1. Enter Student Informations \n2. Enter Course Informations \n3. Enter Marks \n4. List Students \n5. List Courses \n0. Exit \n"
                    l += 6
            else:
                msg = "1. Enter Student Informations \n2. Enter Course Informations \n0. Exit \n"
                l += 3
            stdscr.addstr(msg)
            stdscr.refresh()

            msg = "Enter a number to select: "
            stdscr.addstr(msg)
            stdscr.refresh()
            c = int(stdscr.getstr(l, len(msg), 1).decode("utf-8"))
            l = 0
            if (c == 0):
                curses.nocbreak()
                stdscr.keypad(False)
                stdscr.refresh()
                curses.endwin()
                return
            elif (c == 1):
                stdscr.clear()
                enteredStudents = 1
                msg = "Enter number of students: "
                stdscr.addstr(msg)
                stdscr.refresh()
                t = int(stdscr.getstr(l, len(msg), 5).decode("utf-8"))
                addStudents(sList, t)
            elif (c == 2):
                stdscr.clear()
                enteredCourses = 1
                msg = "Enter number of courses: "
                stdscr.addstr(msg)
                stdscr.refresh()
                t = int(stdscr.getstr(l, len(msg), 3).decode("utf-8"))
                addCourses(cList, t)
            elif (c == 3):
                stdscr.clear()
                if (enteredStudents and enteredCourses):
                    enteredMarks = 1
                    msg = "Mode: \n0. Enter mark for students in all courses \n1. Enter mark by course \n2. Enter mark by student \n"
                    stdscr.addstr(msg)
                    stdscr.refresh()
                    l += 4

                    msg = "Enter mode: "
                    stdscr.addstr(msg)
                    stdscr.refresh()
                    t = int(stdscr.getstr(l, len(msg), 1).decode("utf-8"))
                    addMarks(sList, cList, mList, t)
                else:
                    msg = "The option is unavailable\n"
                    stdscr.addstr(msg)
                    stdscr.refresh()
                    stdscr.getkey()
            elif (c == 4):
                stdscr.clear()
                if (enteredStudents):
                    listObjects(sList)
                else:
                    msg = "The option is unavailable\n"
                    stdscr.addstr(msg)
                    stdscr.refresh()
                    stdscr.getkey()
            elif (c == 5):
                stdscr.clear()
                if (enteredCourses):
                    listObjects(cList)
                else:
                    msg = "The option is unavailable\n"
                    stdscr.addstr(msg)
                    stdscr.refresh()
                    stdscr.getkey()
            elif (c == 6):
                stdscr.clear()
                if (enteredMarks):
                    msg = "Mode: \n0. List all \n1. List by course \n2. List by student \n"
                    stdscr.addstr(msg)
                    stdscr.refresh()
                    l += 3

                    msg = "Select mark listing mode: "
                    stdscr.addstr(msg)
                    stdscr.refresh()
                    l += 1
                    t = int(stdscr.getstr(l, len(msg), 1).decode("utf-8"))
                    if (t == 1):
                        msg = "Enter Student ID: "
                    elif (t == 2):
                        msg = "Enter Course ID: "
                    t2 = ""
                    if (t != 0):
                        stdscr.addstr(msg)
                        stdscr.refresh()
                        l += 1
                        t2 = int(stdscr.getstr(l, len(msg), 16).decode("utf-8"))
                    listMark(mList, t2, t)
                else:
                    msg = "The option is unavailable\n"
                    stdscr.addstr(msg)
                    stdscr.refresh()
                    stdscr.getkey()
            elif (c == 7):
                stdscr.clear()
                if (enteredMarks):
                    gArray = getGPAS(mList)
                    sList = sortStudentList(sList, sortGPA(gArray))
                    stdscr.clear()
                    for i in range(0, len(sList)):
                        msg = f"ID: {sList[i].id}. Name: {sList[i].name}. GPA: {gArray[1, i]}\n"
                        stdscr.addstr(msg)
                        stdscr.refresh()    
                    stdscr.getkey()
                else:
                    msg = "The option is unavailable\n"
                    stdscr.addstr(msg)
                    stdscr.refresh()
                    stdscr.getkey()
            else:
                stdscr.clear()
                msg = "The option is unavailable\n"
                stdscr.addstr(msg)
                stdscr.refresh()
                stdscr.getkey()

wrapper(main)
