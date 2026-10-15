import numpy as np
import inputCodes as In
from domains.studentClass import student
from domains.courseClass import course
from domains.markClass import mark
import curses
stdscr = curses.initscr()

def getObject(lList: list, iID: int):
    for obj in lList:
        if (((type(obj) == student) or (type(obj) == course)) and (obj.getID() == iID)):
            return obj
    return -1

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

def getSortedGPAS(aGPAs: np.ndarray, ascend: int = 0):
    ID = aGPAs[0]
    GPA = aGPAs[1]
    sortedIndices = np.argsort(GPA)[::-1]    
    if (ascend):
        sortedIndices = np.argsort(GPA)
    ID = ID[sortedIndices]
    GPA = GPA[sortedIndices]
    return np.array([ID, GPA])

def getSortedStudentList(lStudents: list, aGPAs: np.ndarray):
    sortedList = []
    length = np.shape(aGPAs)[1]
    for i in range(0, length):
        IDString = str(aGPAs[0, i])
        for obj in lStudents:
            if (IDString == obj.getID()):
                In.addObjects(sortedList, obj)
    return sortedList;

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
        msg = f"Student ID: {oObject.studentID}. Student Name: {oObject.studentName}. Mark: {oObject.markPoint}. Credits: {oObject.creditPoint}\n"
        scr.addstr(msg)
        scr.refresh()

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
    scr.getkey()

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
    scr.getkey()
