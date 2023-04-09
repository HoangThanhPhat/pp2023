import math
import numpy 

class student:
    def __init__(self,stu_id, stu_name, stu_dob):
        self.stu_id = stu_id
        self.stu_name =stu_name
        self.stu_dob = stu_dob
        self.marks = {}

    def accept(self, students):
        stu_id=input('enter the ID of student :')
        stu_name=input('enter the name of student :')
        stu_dob=input('enter ther dob of student :')
        stu=student(stu_id,stu_name,stu_dob)
        students.append(stu)
        return students

    def getmark(self, stu):
        marks = stu.marks
        cour_id = input('enter course ID for get mark: ')
        mark = float(input(f'enter student mark: '))
        marks[cour_id] = mark
        stu.marks = marks

    def display(self, stu):
        print("Name : ", stu.stu_name)
        print("ID : ", stu.stu_id)
        print("DOB : ", stu.stu_dob)
        print("Marks : ", stu.marks)
        
    def getid(self, stu):
        return stu.stu_id
class course:
    def __init__(self,cour_id,cour_name): 
        self.cour_id       =cour_id
        self.cour_name     =cour_name
        self.mark_course   ={}
    def get_courseid(self):
        return self.cour_id
    def accept(self):
        cour_id=input('enter the id of course :')
        cour_name=input('enter the name of course :')
        cou=course(cour_id,cour_name)
        courses.append(cou)
        return courses
    def display(self,cou):
        print("Name of course:",cou.cour_name)
        print("ID of course :",cou.cour_id)
    def getcou(self,cou):
        return cou.cour_id
    
        
# main   
students=[]
stu = student(0,0,0)
num_stu=int(input('enter the number of student:'))
for x in range (num_stu):
    stu.accept(students)

courses=[]
cou=course(0,0)
num_cour=int(input('enter the number of course :'))
for i in range (num_cour):
    cou.accept()

    
for i in range (students.__len__()):
    stu_id = stu.getid(students[i])
    print(f"enter mark for student {stu_id} ")
    for j in range (courses.__len__()):
        stu.getmark(students[i])

    
     
# list of student and course
print("\n")
print("\nList of Students\n")
for i in range(students.__len__()):
    stu.display(students[i])  

print("\n")
print('\nlist of course :\n')
for i in range (courses.__len__()):
    cou.display(courses[i])


    
    
    
# marks={}
# marks_cour = {}
# GPA_student = {}
# for x in range(students.__len__()):
#     stu_id=input('enter the id of student to the scores:')
#     for x in range (courses.__len__()):
#         cour_id=cou.get_id(courses[x])
#         mar = float(input(f'enter the mark for course {cour_id}:'))
#         mark =math.floor(mar)
#         marks_cour[cour_id]=mark
#         GPA_student[stu_id]
#         marks[stu_id] =marks_cour.copy()



    