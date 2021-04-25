studentInput = int(input("Enter number of student: "));
print("There are: ", studentInput, "students")
studentArr = {}

def inputinfo(id, name, dob):
    studentArr[id] = [name, dob]
for i in range(studentInput):
    print(i+1, "st Student")
    a = input("ID :")
    b = input("Name: ")
    c = input("Dob: ")
    inputinfo(a, b, c)


courseInput = int(input("Enter course number: "))
print(f"There are {courseInput} courses")
courseArr = {}
def inputcourse(id, name):
    courseArr[id] = name
for i in range(courseInput):
    print(i+1, "st course")
    a = input("Id: ")
    b = input("Name: ")
    inputcourse(a, b)


idSum = input("Enter Student Id to input Mark: ")
while True:
    if idSum not in studentArr:
        idSum = input("Enter Student Id Again : ")
    else:
        break

courseSum = input("Name of Course: ")
while True:
    if courseSum not in courseArr.values():
        courseSum = input("Enter Course Again: ")
    else:
        break

markInput = input("Mark: ")
markArr = {}
def inputmark(idStudent, course, mark):
    markArr[idStudent] = {course: mark}
markInput(idSum , courseSum, markInput)


print("Press 1, 2, 3 to see the Data")
print("1: Student list")
print("2: Course list")
print("3: Mark")


choices = int(input("Select: "))
if choices == 1:
    print(studentArr)
elif choices == 2:
    print(courseArr)
elif choices == 3:
    print(markArr)