# Classes
# Student
class students:
    __studentList = []
    def __init__(self):
        self.list = self.__studentList

    def __str__(self):
        return "Students"

    def addStudent(self, student):
        self.list.append(student)
        self.__studentList[len(self.list) - 1].setIndex(len(self.list) - 1)

    def addStudents(self, iAmount):
        for i in range(0,iAmount):
            Index = len(self.list)
            print(f"Entry number {Index + 1}")
            ID = int(input("Enter Student ID: "))
            Name = input("Enter Student Name: ")
            DoB = input("Enter Student Birthday: ")
            self.list.append(self.student(ID, Name, DoB))
            self.__studentList[Index].setIndex(Index)
        print()
        
    def listStudents(self):
        for this in self.list:
            this.outPrint()
        print()

    def getStudent(self, ID):
        for this in self.list:
            if this.id == ID:
                return this
        return -1

    def getStudentByIndex(self, Index):
        return self.list[Index]
    
    class student:
        index = -1
        def __init__(self, iID, sName, sBirth):
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

        def setIndex(self, iIndex):
            self.index = iIndex

# Courses
class courses:
    __courseList = []
    
    def __init__(self):
        self.list = self.__courseList

    def __str__(self):
        return "Courses"

    def addCourse(self, course):
        self.list.append(course)
        self.__courseList[len(self.list) - 1].setIndex(len(self.list) - 1)

    def addCourses(self, iAmount):
        for i in range(0,iAmount):
            Index = len(self.list)
            print(f"Entry number {Index + 1}")
            ID = int(input("Enter Course ID: "))
            Name = input("Enter Course Name: ")
            Credit = input("Enter Course Credit: ")
            self.list.append(self.course(ID, Name, Credit))
            self.__courseList[Index].setIndex(Index)
        print()

    def listCourses(self):
        for this in self.list:
            this.outPrint()
        print()

    def getCourse(self, ID):
        for this in self.list:
            if this.id == ID:
                return this
        return -1
    
    def getCourseByIndex(self, Index):
        return self.list[Index]
            
    class course:
        index = -1
        def __init__(self, sID, sName, iCredit):
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

        def getIndex(self):
            return self.index

        def setIndex(self, iIndex):
            self.index = iIndex

# Marks
class marks:
    __markList = []

    def __init__(self):
        self.list = self.__markList

    def __str__(self):
        return "Marks"

    def addMark(self, mark):
        self.list.append(mark)

    def addMarks(self, students, courses, iMode):
        # iMode = 0: By Course. 1: By Student
        # Add marks by course: Add marks for all student in a course
        # Add marks by student: Add marks in all course for a student
        amount = len(students.list)
        ID = 0
        if (iMode):
            ID = int(input("Enter Student ID: "))
            amount = len(courses.list)
        else:
            ID = int(input("Enter Course ID: "))
        for i in range(0, amount):
            if (iMode):
                Mark = float(input(f"Enter Student {students.getStudent(ID)} -  Course {courses.getCourseByIndex(i)} Mark: "))
                self.list.append(self.mark(Mark, students.getStudent(ID), courses.getCourseByIndex(i)))
            else:
                Mark = float(input(f"Enter Student {students.getStudentByIndex(i)} -  Course {courses.getCourse(ID)} Mark: "))
                self.list.append(self.mark(Mark, students.getStudentByIndex(i), courses.getCourse(ID)))

    def listMarks(self):
        for this in self.list:
            this.outPrint()
        print()

    def listMarksMode(self, iMode, ID):
        # 1: By Courses
        # 2: By Students
        # Else: All
        for this in self.list:
            if (iMode == 1):
                if this.courseID == ID:
                    this.outPrint()
            elif (iMode == 2):
                if this.studentID == ID:
                    this.outPrint()
            else:
                this.outPrint()
        print()

    class mark:
        def __init__(self, fMark, student, course):
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

#Temp
sList = students()
cList = courses()
mList = marks()
sList.addStudent(students.student(2510332, "Hoang", "26 08 2007"))
sList.addStudent(students.student(2511337, "Hoang", "11 07 2007"))
cList.addCourse(courses.course(1, "APP", 4))
cList.addCourse(courses.course(2, "OOP", 3))
