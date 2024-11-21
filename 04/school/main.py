from course import Course
from teacher import Teacher
from student import Student
from grade import Grade

teacher1 = Teacher(1, "James Herbert", "IT")
course1 = Course(1, "IT Science", teacher1)
student1 = Student(1, "Bill Gardner", 4)
grade_it = Grade(student1, course1, 5)

print(f"{teacher1.name} is teachig {student1.name} {course1.name}. {student1.name} grade is {grade_it.grade} ")