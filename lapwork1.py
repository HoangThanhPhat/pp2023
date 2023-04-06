# • Input functions:
#       • Input number of students in a class
#       • Input student information: id, name, DoB
#       • Input number of courses
#       • Input course information: id, name

# • Select a course, input marks for student in this course
# • Listing functions:
#       • List courses
#       • List students
#       • Show student marks for a given course

# input function 
# student = []
# def input_num_student():
#     return input("Enter the number of student")
# def input_student_info():
#     id = input("Enter student id")
#     name = input("Enter student's name: ")
#     dob  = input("Enter student's DoB: ")
#     return{
#         'id':id,
#         'name': name,
#         'dob':dob
#     }
def stu():
    student = {}
    num_student = int(input("Enter number of student: "))
    for i in range(num_student):
        id   = input("Enter student id: ")
        name = input("Enter student's name: ")
        dob  = input("Enter student's DoB: ")
        temp_stu = {'id': id, 'name': name, 'dob': dob}
        student[id] = temp_stu
    return student
Student = stu()
print(Student)
      
def cou():
    course ={}
    num_courses = int(input("Enter the number of courses: "))
    for i in range(num_courses):
        course_id           = input("Enter course ID: ")
        course_name         = input("Enter course's name: ")
        temp_cou            = {"course' id ": course_id, "course' name  ":course_name}
        course[course_id]   = temp_cou    
    return course
Course =cou()

#select a course, input marks for students in this course
def mark(Student) :
    marks = {}
    mark = {}
    course_numbers = int(input("Enter number course : "))
    for i in range(course_numbers) :
        course_id = input("Enter course' ID : ")
        for  id in Student.keys():
            mark_stu  = float(input(f"enter the mark for student {id} : "))
            marks[id] = mark_stu
        mark[course_id] = marks.copy()
    return mark
Mark = mark(Student)
print(Mark)
#Listing function

def list_students(Student) :
    print("Student have : ")
    print(Student.values())
list_students(Student)

def list_courses(Course)   :
    print("Courses have : ")   
    print(Course.values())
list_courses(Course)
    
def show_mark(Mark)        :
    course_id = input("Enter course' ID : ")
    if course_id in Mark :
        print(Mark[course_id])
    else :
        print('false')
show_mark(Mark)
        
         
    
    





