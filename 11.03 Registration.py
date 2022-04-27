class Student():
    def __init__(self, firstname="", lastname="", tnumber=""):
        self.First=firstname
        self.Last=lastname
        self.ID=tnumber
        self.CourseList = []

class StudentList():
    def __init__(self):
        self.StudentList = []
    def add_student(self, firstname, lastname, tnumber):
        student = Student(firstname, lastname, tnumber)
        self.StudentList.append(student)
    def find_student(self, studenttofind):
        for i in range(len(mystudentlist.StudentList)):
            if mystudentlist.StudentList[i].ID == studenttofind:
                return i
        return -1
    def print_student_list(self):
        print("{:<14s}{:<14s}{:<14s}".format("First Name", "Last Name", "T Number"))
        for i in range(len(self.StudentList)):
            print("{:<14s}{:<14s}{:<14s}".format(str(self.StudentList[i].First), str(self.StudentList[i].Last), str(self.StudentList[i].ID)))
            for j in range(len(self.StudentList[i].CourseList)):
                print(mystudentlist.Studentlist[i].CourseList[J])
    def add_student_from_file(self, filename):
        file = open(filename)
        student = file.readline()
        while student != '':
            y = student.split(',')
            self.add_student(y[0].split(), y[1].split(), y[2].split())
            student = file.readline()

class Course():
    def __init__(self, department, number, name, room, meetingtimes):
        self.Dept=department
        self.Number=number
        self.Name=name
        self.Room=room
        self.MeetingTimes=meetingtimes

class CourseList():
    def __init__(self):
        self.CourseList = []
    def add_course(self, department, number, name, room, meetingtimes):
        course = Course(department, number, name, room, meetingtimes)
        self.CourseList.append(course)
    def find_course(self, departmenttofind, numbertofind):
        for i in range(len(mycourselist.CourseList)):
            if mycourselist.CourseList[i].Dept == departmenttofind and mycourselist.CourseList[i].Number == numbertofind:
                return i
        return -1
    def add_course_from_file(self, filename):
        c = open(filename)
        x = c.readline()
        while x != '':
            a = x.split(",")
            self.add_course(str(a[0]).strip(), str(a[1]).strip(), str(a[2]).strip(), str(a[3]).strip(), str(a[4]).strip())
            x = c.readline()

mycourselist = CourseList()
mycourselist.add_course_from_file("11.03 Courses.txt")
mystudentlist = StudentList()
mystudentlist.add_student_from_file("11.03 Students.txt")
registrationfile = open("11.03 Registration.txt")
registration = registrationfile.readline()
while registration != '':
    register = registration.split(',')
    mystudentlist.StudentList[mystudentlist.find_student(register[0])].CourseList.append(mycourselist.CourseList[mycourselist.find_course(register[1], register[2])])
    registration = registrationfile.readline()
mystudentlist.print_student_list()