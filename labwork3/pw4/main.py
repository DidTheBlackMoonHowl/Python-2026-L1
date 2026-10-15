# Need a parrent package
# from . import domains
import domains
import inputCodes as In
import outputCodes as Out
import numpy as np
import curses
from curses import wrapper
stdscr = curses.initscr()

def main(stdscr):
    curses.echo()
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
            In.addStudents(sList, t)
        elif (c == 2):
            stdscr.clear()
            enteredCourses = 1
            msg = "Enter number of courses: "
            stdscr.addstr(msg)
            stdscr.refresh()
            t = int(stdscr.getstr(l, len(msg), 3).decode("utf-8"))
            In.addCourses(cList, t)
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
                In.addMarks(sList, cList, mList, t)
            else:
                msg = "The option is unavailable\n"
                stdscr.addstr(msg)
                stdscr.refresh()
                stdscr.getkey()
        elif (c == 4):
            stdscr.clear()
            if (enteredStudents):
                Out.listObjects(sList)
            else:
                msg = "The option is unavailable\n"
                stdscr.addstr(msg)
                stdscr.refresh()
                stdscr.getkey()
        elif (c == 5):
            stdscr.clear()
            if (enteredCourses):
                Out.listObjects(cList)
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
                    msg = "Enter Course ID: "
                elif (t == 2):
                    msg = "Enter Student ID: "
                t2 = ""
                if (t != 0):
                    stdscr.addstr(msg)
                    stdscr.refresh()
                    l += 1
                    t2 = stdscr.getstr(l, len(msg), 16).decode("utf-8")
                Out.listMark(mList, t2, t)
            else:
                msg = "The option is unavailable\n"
                stdscr.addstr(msg)
                stdscr.refresh()
                stdscr.getkey()
        elif (c == 7):
            stdscr.clear()
            if (enteredMarks):
                gArray = Out.getGPAS(mList)
                sList = Out.getSortedStudentList(sList, Out.getSortedGPAS(gArray))
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
