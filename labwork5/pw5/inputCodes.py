import os
import curses
import outputCodes as Out
from domains.studentClass import student
from domains.courseClass import course
from domains.markClass import mark

stdscr = curses.initscr()

def addObjects(lList: list, oObject: object):
    lList.append(oObject)

def readFromFile(file):
    os.makedirs("./datas", exist_ok=True)

    f = open(file, "r")
    f1 = f.readlines()
    t1 = []
    returnList = []
    
    for t2 in f1:
        t1.append(t2.replace("\n", ""))

    if (file == "./datas/students.txt"):
        for t2 in t1:
            t3 = t2.split(',')
            addObjects(returnList, student(t3[0], t3[1], t3[2]))

    elif (file == "./datas/courses.txt"):
        for t2 in t1:
            t3 = t2.split(',')
            addObjects(returnList, course(t3[0], t3[1], int(t3[2])))
                
    elif (file == "./datas/marks.txt"):
        for t2 in t1:
            t3 = t2.split(',')
            addObjects(returnList, mark(float(t3[0]), student(t3[1], t3[2], t3[3]), course(t3[4], t3[5], int(t3[6]))))
    else:
        return -1

    f.close()
    
    return returnList

def writeToFile(file: str, content):
    os.makedirs("./datas", exist_ok=True)

    # mode 'a' = write at the end
    f = open(file, "a")
    
    if (file == "./datas/students.txt"):
        content: student
        f.write(content.getID() + "," + content.getName() + "," + content.getDoB() + "\n")

    elif (file == "./datas/courses.txt"):
        content: course
        f.write(content.getID() + "," + content.getName() + "," + str(content.getPoint()) + "\n")

    elif (file == "./datas/marks.txt"):
        content: mark
        f.write(str(content.getMark()) + ",")
        f.write(content.getStudent().getID() + "," + content.getStudent().getName() + "," + content.getStudent().getDoB() + ",")
        f.write(content.getCourse().getID() + "," + content.getCourse().getName() + "," + str(content.getCourse().getPoint()) + "\n")

    else:
        f.write(content + "\n")

    f.close()

# Expected curses window for scr
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
        writeToFile("./datas/students.txt", student(sID, sName, sDoB))

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
        writeToFile("./datas/courses.txt", course(sID, sName, iCredits))

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
            writeToFile("./datas/marks.txt", mark(Mark, Out.getObject(lStudents, ID), lCourses[i]))
            l += 1
        elif (iMode == 1):
            msg = f"Enter course {ID} - student {lStudents[i].id} mark: "
            scr.addstr(msg)
            scr.refresh()
            Mark = float(stdscr.getstr(l, len(msg), 7).decode("utf-8"))
            writeToFile("./datas/marks.txt", mark(Mark, lStudents[i], Out.getObject(lCourses, ID)))
            l += 1
        else:
            for j in range(0, len(lCourses)):
                msg = f"Enter student {lStudents[i].id} - courses {lCourses[j].id} mark: "
                scr.addstr(msg)
                scr.refresh()
                Mark = float(stdscr.getstr(l, len(msg), 7).decode("utf-8"))
                writeToFile("./datas/marks.txt", mark(Mark, lStudents[i], lCourses[j]))
                l += 1

