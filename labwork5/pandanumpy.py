# Should be run inside IDLE
import os
import pandas as pd
from pw5.domains.studentClass import student
from pw5.domains.courseClass import course
from pw5.domains.markClass import mark

pathParent = ["./pw5/datas", "./exportedCSV"]
pathIn = ["./pw5/datas/students.txt", "./pw5/datas/courses.txt", "./pw5/datas/marks.txt"]
pathOut = ["./exportedCSV/students.csv", "./exportedCSV/courses.csv", "./exportedCSV/marks.csv"]

def readF(fPath):
    os.makedirs(pathParent[0], exist_ok=True)
    f = open(fPath, "r")
    f1 = f.readlines()
    t1 = []
    returnList = []

    for i in f1:
        t1.append(i.replace("\n", ""))

    if (fPath == pathIn[0]):
        for t2 in t1:
            t3 = t2.split(',')
            returnList.append(student(t3[0], t3[1], t3[2]))
    elif (fPath == pathIn[1]):
        for t2 in t1:
            t3 = t2.split(',')
            returnList.append(course(t3[0], t3[1], int(t3[2])))
    elif (fPath == pathIn[2]):
        for t2 in t1:
            t3 = t2.split(',')
            returnList.append(mark(float(t3[0]), student(t3[1], t3[2], t3[3]), course(t3[4], t3[5], int(t3[6]))))
    else:
        return -1
    
    f.close()

    return returnList


def writeF(fPath, content):
    os.makedirs(pathParent[0], exist_ok=True)
    os.makedirs(pathParent[1], exist_ok=True)
    
    f = open(fPath, "a")

    if (fPath == pathOut[0]):
        if (type(content) == student):
            f.write(content.getID() + "," + content.getName() + "," + content.getDoB() + "\n")
        else:
            f.write(content + "\n")

    elif (fPath == pathOut[1]):
        if (type(content) == course):
            f.write(content.getID() + "," + content.getName() + "," + str(content.getPoint()) + "\n")
        else:
            f.write(content + "\n")

    elif (fPath == pathOut[2]):
        if(type(content) == mark):
            f.write(str(content.getMark()) + ",")
            f.write(content.getStudent().getID() + "," + content.getStudent().getName() + "," + content.getStudent().getDoB() + ",")
            f.write(content.getCourse().getID() + "," + content.getCourse().getName() + "," + str(content.getCourse().getPoint()) + "\n")
        else:
            f.write(content + "\n")
            
    else:
        f.write(content + "\n")

    f.close()

def export():
    # Read .txt if exist
    studentList = []
    if os.path.exists(pathIn[0]):
        studentList = readF(pathIn[0])
        
    courseList = []
    if os.path.exists(pathIn[1]):
        courseList = readF(pathIn[1])

    markList = []
    if os.path.exists(pathIn[2]):
        markList = readF(pathIn[2])

    # Remove old .csv
    if os.path.exists(pathOut[0]):
        os.remove(pathOut[0])
    if os.path.exists(pathOut[1]):
        os.remove(pathOut[1])
    if os.path.exists(pathOut[2]):
        os.remove(pathOut[2])

    # First row. To define colums
    writeF(pathOut[0], "id,name,dob")
    writeF(pathOut[1], "id,name,credits")
    writeF(pathOut[2], "mark,student_id,student_name,student_dob,course_id,course_name,course_credits")

    # Write datas
    for i in studentList:
        writeF(pathOut[0], i)
    for i in courseList:
        writeF(pathOut[1], i)
    for i in markList:
        writeF(pathOut[2], i)

# def query(dataframe: pd.DataFrame, cond):
def query(dataframe):
    # Eg: name != "Mr. Unwanted"
    cond = input("Enter query condition: ")
    result = dataframe.query(cond)
    if result is not None:
        print("Query result: ")
        print(result)

def main():
    export()
    
    studentDF = pd.read_csv(pathOut[0])
    courseDF = pd.read_csv(pathOut[1])
    markDF = pd.read_csv(pathOut[2])
    
    print(courseDF.head(), "\n")
    print(studentDF.head(), "\n")
    print(markDF.head(), "\n")

    query(studentDF)

main()
