import curses
from domains.studentClass import student
from domains.courseClass import course
from domains.markClass import mark

stdscr = curses.initscr()

def addObjects(lList: list, oObject: object):
    lList.append(oObject)

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
        addObjects(lStudents, student(sID, sName, sDoB))

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
                l += 1
