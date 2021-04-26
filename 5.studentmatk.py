import math
import numpy
import gzip, base64
from io import StringIO

studentList = []
courseList = []
markList = []

def inputStudent():
    global inputStudent
    inputStudent = int(input("Enter Number of Student: "))
def inputCourse():
    global inputCourse
    inputCourse = int(input("Enter Number of Course: "))
def inputRecord():
    global inputRecord
    inputRecord = int(input("Enter Number of Record: "))
def ifExistStudent(name):
    for student in studentList:
        if name == student.name:
            return True
def ifExistCourse(name):
    for course in courseList:
        if name == course.name:
            return True

def averageMark(name):
    avrMark = []

    for i in range(len(markList)):
        if name == markList[i].studentName:
            avrMark.append(markList[i].mark)
    arrMark = array(arrAvr)
    averageMark = average(arrMar)
    print("Average Mark of " + name + ": " + str(averageMark))

class Student():
    def __init__(self, id, name, dob):
        self.id = id
        self.name=name
        self.dob=dob

    def getStudentInfo(self):
        print("ID of student : " + self.id)
        print("Name of student : " + self.name)
        print("Dob of student : " + self.dob)

    def setStudentInfo(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

class Course():
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def getCourseInfo(self):
        self.id = id 
        self.name = name

    def setCourseInfo(self):
        print("ID course: " + self.id)
        print("Name course: " + self.name)

class Mark():
    def __init__(self, id, name):
        self.studentName= studentName
        self.courseName = courseName
        self.mark = mark

    def getMarkInfo(self):
        print("Student Name: " + self.studentName)
        print("Course Name: " + self.courseName)
        print("Mark: " + self.mark)

    def setMarkInfo(self, studentName, courseName, mark):
        self.studentName = studentName
        self.courseName = courseName
        self.mark = mark

def createStudentList():
    for i in range(inputStudent):
        studentList.append("s" + str(i))        

def setStudent():
    for i in range(inputStudent):
        print("---" + str(i+1) + "st Student" + "---")
        id_Student = input("Enter Student ID: ")
        name_Student = input("Enter Student Name: ")
        dob_Student = input("Enter Student DoB: ")
        studentList[i] = Student(id_Student, name_Student, dob_Student)

def printStudentList():
    print("\n")
    print("---The Student List--- ")
    for i in range(inputStudent):
        print("---" + str(i + 1) + "st Student" + "---")
        studentList[i].getStudentInfo()


def createcourseList():
    for i in range(inputCourse):
        courseList.append("s" + str(i))

def setCourse():
    for i in range(inputCourse):
        print("---" + str(i+1) + "st Course" + "---")
        id_Course = input("Enter Course ID: ")
        name_Course = input("Enter Course Name: ")
        courseList[i] = Course(id_Course, name_Course)



def printCourseList():
    print("\n")
    print("---The Course List--- ")
    for i in range(inputCourse):
        print("---" + str(i + 1) + "st Course" + "---")
        courseList[i].getCourseInfo()

def createMark():
    global checkNameStudent
    global checkNameCourse
    checkNameStudent = input("Choose Student: ")
    checkNameCourse = input("Choose Course: ")
    if (ifExistNameStudent(checkNameStudent) and ifExistNameCourse(checkNameCourse)):
        markList.append("record" + str(index+1))
        print("Index: " + str(index))
        #print("Apeend OK")
    else:
        print("Not exist Student or Course")

def setMarkInfo():

    global index
    mark = input("Mark: ")
    markList[index] = MarkTable(checkNameStudent, checkNameCourse, mark)
    index += 1


def printMarkList():
    print("\n")
    print("----------The Mark List---------- ")
    for i in range(len(markList)):
        print("---------" + str(i + 1) + "st Record" + "---------")
        markList[i].getMarkInfo()

def avrStudent():
    nameStd = input("Get Student's Average: ")
    averageMark(nameStd)

def handleFile():
    fileStudent = open("students.txt", "a")
    for student in studentList:
        fileStudent.write(student.id)
        fileStudent.write(student.name)
        fileStudent.write(student.dob)
fileStudent.close()

fileCourse = open("course.txt", "a")
for course in courseList:
    fileCourse.write(course.id)
    fileCourse.write(course.name)
fileCourse.close()

fileMark = open("marks.txt", "a")
for mark in markList:
    fileMark.write(mark.studentName)
    fileMark.write(mark.courseName)
    fileMark.write(str(mark.mark))
fileMark.close()

f1 = open("students.txt", "r")
print(f1.read())

f2 = open("courses.txt", "r")
    print(f2.read())

f3 = open("marks.txt", "r")
    print(f3.read())


index = 0
inputStudent()
createStudentList()
setStudent()
printStudentList()

print("\n")
inputCourse()
createcourseList()
setCourse()
printCourseList()

print("\n")
numberRecord()
for i in range(numberRecord):
    createMark()
    setMark()
printMarkList()
avrStudent()
handleFile()