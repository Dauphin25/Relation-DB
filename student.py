from school_database import c


class Student:
    def __init__(self, name, surname, grade, gpa):
        self.name = name
        self.surname = surname
        self.grade = grade
        self.gpa = gpa
        c.execute('''INSERT INTO students (name, surname, current_year, gpa)
                            VALUES (?, ?, ?, ?)''', (self.name, self.surname, self.grade, self.gpa))

    def __repr__(self):
        return "<Student {} {} in {} grade with {} gpa>".format(self.name, self.surname, self.grade, self.gpa)

    @classmethod
    def remove(cls, stu_id):
        c.execute("DELETE FROM students WHERE stu_id = {}".format(stu_id))

    @classmethod
    def get_all_students(cls):
        c.execute('''SELECT * FROM students''')
        students = c.fetchall()
        for stu in students:
            print(stu)

    @classmethod
    def good_students(cls):
        c.execute("SELECT * FROM students WHERE gpa > 3.5")
        good_students = c.fetchall()
        print("MY GOOD STUDENTS")
        for stu in good_students:
            print(stu)
        print("END OF MY GOOD STUDENTS")

    def get_id(self):
        c.execute('''SELECT stu_id FROM students 
                     WHERE name = ? AND surname = ? AND current_year = ? AND gpa = ?''',
                  (self.name, self.surname, self.grade, self.gpa))
        stu_id = c.fetchone()
        if stu_id:
            stu_id = stu_id[0]
            return stu_id

    def enroll(self, course):
        c.execute('''INSERT INTO student_subject VALUES (?, ?)''', (self.get_id(), course.get_id()))
