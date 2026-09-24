# Initialization
sList = []
cList = []
mList = []
sNum = int(input("Enter number of students: "))
cNum = int(input("Enter number of courses: "))

# Patterns
def student_pattern_in(i):
    print()
    sID = int(input(f"Enter Student {i + 1} ID : "))
    sName = input(f"Enter Student {i + 1} Name : ")
    sDoB = input(f"Enter Student {i + 1} Date of Birth: ")
    return {'ID':sID, 'Name':sName, 'DoB':sDoB}

def course_pattern_in(i):
    print()
    cID = int(input(f"Enter Course {i + 1} ID: "))
    cName = input(f"Enter Course {i + 1} Name: ")
    return {'ID':cID, 'Name':cName}

# Setters
def setStudentInfo():
    for i in range(0,sNum):
        sList.append(student_pattern_in(i))

def setCourseInfo():
    for i in range(0,cNum):
        cList.append(course_pattern_in(i))

def setMarks():
    print("Select a Course")
    getCourses()
    print()
    cID = int(input(f"Enter Course ID: "))
    for i in range(0,sNum):
        sMark = float(input(f"Enter Student {sList[i].get('ID')} Mark: "))
        mList.append({"Course":cList[getCourseIndex(cID)], "Student":sList[i], "Mark":sMark})

# Getters
def getCourses():     # List Courses
    print()
    for i in range(0,cNum):
        print(f"Course ID: {cList[i].get('ID')}. Course Name: {cList[i].get('Name')}")

def getStudents():    # List Students
    print()
    for i in range(0,sNum):
        print(f"Student ID: {sList[i].get('ID')}. Student Name: {sList[i].get('Name')}. Date of Birth: {sList[i].get('DoB')}")

def getCourseIndex(n):
    for i in range (0,cNum):
        if (cList[i].get('ID') == n):
            return i
    return -1

def getStudentIndex(n):
    for i in range (0,cNum):
        if (sList[i].get('ID') == n):
            return i
    return -1

def getMarks():
    print()
    for i in range(0,sNum):
        print(f"Course ID: {mList[i].get('Course').get('ID')}. Course Name: {mList[i].get('Course').get('Name')}")
        print(f"Student ID: {mList[i].get('Student').get('ID')}. Student Name: {mList[i].get('Student').get('Name')}. Mark: {mList[i].get('Mark')}\n")

# Executing...
setStudentInfo()
setCourseInfo()
setMarks()
getMarks()

