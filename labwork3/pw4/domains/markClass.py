# import from current directory. Need a parent package
# for importing classes in student, here is an example
# from .student import student
from .studentClass import student
from .courseClass import course

import math

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
