from school_database import c


def get_all_student_subject():
    c.execute("SELECT * FROM student_subject")
    values = c.fetchall()
    for value in values:
        print(value)


def display_student_subject():
    c.execute('''SELECT students.name AS student_name, students.surname AS student_surname, 
                             students.current_year AS student_year, students.gpa AS student_gpa, 
                             subjects.title AS subject_title, subjects.duration AS subject_duration, 
                             subjects.credits AS subject_credits, 
                             teachers.name AS teacher_name, teachers.surname AS teacher_surname, 
                             teachers.years_of_experience AS teacher_experience
                      FROM student_subject
                      INNER JOIN students ON student_subject.student_id = students.stu_id
                      INNER JOIN subjects ON student_subject.subject_id = subjects.subject_id
                      INNER JOIN teachers ON subjects.teacher_id = teachers.teach_id''')

    # Fetch and print the results
    results = c.fetchall()
    for row in results:
        print(row)


def student_subject_gpa():
    c.execute('''SELECT subjects.title AS subject_title, subjects.duration AS subject_duration,
                           subjects.credits AS subject_credits,
                           students.name AS student_name, students.surname AS student_surname,
                        students.gpa AS student_gpa
                    FROM student_subject
                    JOIN subjects ON student_subject.subject_id = subjects.subject_id
                    JOIN students ON student_subject.student_id = students.stu_id;''')
    # Fetch and print the results
    results = c.fetchall()
    for row in results:
        print(row)


def order_students(order_by, order_with):
    temp_query = "SELECT * FROM students ORDER BY " + order_by + " " + order_with
    c.execute(temp_query)
    results = c.fetchall()
    print("ORDERDER STUDENT BY " + order_by + " WITH " + order_with)
    for row in results:
        print(row)
    print("END OF SORTING")
