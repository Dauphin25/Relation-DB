from student import Student
from teacher import Teacher
from subject import Subject
import queries
import random


if __name__ == '__main__':

    # creating students
    stu1 = Student('meko', 'mokverashvili', 12, 3.9)
    stu2 = Student('mary', 'stuart', 9, 3.4)
    stu3 = Student('marie', 'antoinette', 11, 2.9)
    stu4 = Student('anna', 'karenina', 11, 3.4)
    stu5 = Student('lucrezia', 'borgia', 9, 2.2)
    stu6 = Student('lorenzo', 'de medici', 12, 4.0)
    stu7 = Student('nicolas', 'romanov', 12, 3.6)
    students = [stu1, stu2, stu3, stu4, stu5, stu6, stu7]

    # demonstrating student functions
    Student.good_students()
    queries.order_students('gpa', 'DESC')

    # creating teachers
    teacher1 = Teacher('aristotle', 'greek', 5)
    teacher2 = Teacher('albert', 'Einstein', 12)
    teacher3 = Teacher('tsotne', 'Magnificent', 8)
    teachers = [teacher1, teacher2, teacher3]

    # demonstrating teacher functions
    Teacher.get_all_teachers()
    Teacher.very_experianced_teachers()

    # creating subjects
    calculus = Subject('calculus 1', 13, 5, teacher2)
    history = Subject('history', 16, 4, teacher1)
    tbc_python = Subject('tbc_python', 12, 10, teacher3)
    subjects = [calculus, history, tbc_python]

    # demonstrating subject functions
    Subject.get_all_subjects()
    Subject.long_subjects()

    # enrolling student in subjects
    for student in students:
        temp_subjects = subjects.copy()
        for _ in range(2):
            random.shuffle(temp_subjects)
            random_subject = temp_subjects.pop()
            student.enroll(random_subject)

    # demonstrating join queries
    queries.get_all_student_subject()
    queries.student_subject_gpa()
    queries.display_student_subject()
