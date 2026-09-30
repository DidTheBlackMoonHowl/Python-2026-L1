sNum = 0
cNum = 0
cList = []
mList = []
sList = []

# Patterns
## Student no. N
def studentPattern(n):
    print()
    sID = int(input(f"Enter Student {n + 1} ID: "))
    sName = input(f"Enter Student {n + 1} Name: ")
    sDoB = input(f"Enter Student {n + 1} Date of Birth: ")
    return {'ID':sID, 'Name':sName, 'DoB':sDoB}

## Course no. N
def coursePattern(n):
    print()
    cID = int(input(f"Enter Course {n + 1} ID: "))
    cName = input(f"Enter Course {n + 1} Name: ")
    cCredit = int(input(f"Enter Course {n + 1} Credits: "))
    return {'ID':cID, 'Name':cName, 'Credits':cCredit}

# Setter
## List of Students
def setStudentInfo():
    for i in range(0,len(sList)):
        sList.append(studentPattern(i))

## List of Courses
def setCourseInfo():
    for i in range(0,cNum):
        cList.append(coursePattern(i))

# Set All Student's Mark of the Same Course
## Course ID
def setMarkCourse(cID):     # Fixed Course Element
    for i in range(0,len(sList)):
        Credit = 0
        Mark = float(input(f"Enter Student {sList[i].get('ID')} Mark: "))
        Credit = cList[getCourseIndex(cID)].get('Credits') 
        mList.append({"Course":cList[getCourseIndex(cID)], "Student":sList[i], "Mark":Mark, "Credits":Credit})  # Variable Student Elements

# Set All Course Marks for a Student
## Student ID
def setMarkStudent(sID):    # Fixed Student Element
    for i in range(0,len(cList)):
        Mark = float(input(f"Enter Course {cList[i].get('ID')} Mark: "))
        Credit = cList[i].get('Credits')                   # Variable Course Element
        mList.append({"Course":cList[i], "Student":sList[getStudentIndex(sID)], "Mark":Mark, "Credits":Credit})

# Set Mark for student sID in course cID
## Student ID, Course ID
def setMarkSpecific(sID, cID):
    Mark = float(input(f"Enter Student {sID} - Course {cID} Mark: "))
    Credit = cList[getCourseIndex(cID)].get('Credits')
    mList.append({"Course":cList[getCourseIndex(cID)], "Student":sList[getStudentIndex(sID)], "Mark":Mark, "Credits":Credit})

# Getter
## Course ID
def getCourseIndex(cID):
    for i in range (0,len(cList)):
        if (cList[i].get('ID') == cID):
            return i
    return -1

## Student ID
def getStudentIndex(sID):
    for i in range (0,len(sList)):
        if (sList[i].get('ID') == sID):
            return i
    return -1

## Student ID
def getCreditSum(sID):
    sCre = 0
    for i in range(0,len(mList)):
        if (mList[i].get('Student').get('ID') == sID):
            sCre += mList[i].get('Credits')
    return sCre

## Student ID
def getMarkSum(sID):
    sMark = 0
    for i in range(0,len(mList)):
        if (mList[i].get('Student').get('ID') == sID):
            sMark += mList[i].get('Mark')/5.0*mList[i].get('Credits')
    return sMark

## Student ID
def getGPA(sID):
    sMark = getMarkSum(sID)
    sCre = getCreditSum(sID)
    return sMark/sCre

# Listing
def listCourses():
    for i in range(0,len(cList)):
        print(f"Course ID: {cList[i].get('ID')}. Course Name: {cList[i].get('Name')}")

def listStudents():
    for i in range(0,len(sList)):
        print(f"Student ID: {sList[i].get('ID')}. Student Name: {sList[i].get('Name')}. Date of Birth: {sList[i].get('DoB')}")
        
def listMarks():
    print()
    for i in range(0,len(mList)):
        print(f"Course ID: {mList[i].get('Course').get('ID')}. Course Name: {mList[i].get('Course').get('Name')}")
        print(f"Student ID: {mList[i].get('Student').get('ID')}. Student Name: {mList[i].get('Student').get('Name')}. Mark: {mList[i].get('Mark')}\n")

## Student ID
def displayGPA(sID):
    print(f"Total Credits: {getCreditSum(sID)}. Total Mark: {getMarkSum(sID)}. GPA: {getGPA(sID)}")


# Base setup
sNum = int(input("Enter Number of Students: "))
cNum = int(input("Enter Number of Courses: "))
setStudentInfo()
setCourseInfo()
