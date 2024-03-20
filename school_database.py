import sqlite3

conn = sqlite3.connect('school.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS teachers (
                teach_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                surname TEXT NOT NULL,
                years_of_experience REAL
            )''')

c.execute('''CREATE TABLE IF NOT EXISTS students (
                stu_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                surname TEXT NOT NULL,
                current_year INTEGER,
                gpa DOUBLE
            )''')

c.execute('''CREATE TABLE IF NOT EXISTS subjects (
                subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                duration REAL,
                credits INTEGER,
                teacher_id INTEGER,
                FOREIGN KEY (teacher_id) REFERENCES teachers(teach_id)
            )''')

c.execute('''CREATE TABLE IF NOT EXISTS student_subject (
                student_id INTEGER,
                subject_id INTEGER,
                FOREIGN KEY (student_id) REFERENCES students(stu_id),
                FOREIGN KEY (subject_id) REFERENCES subjects(teach_id),
                PRIMARY KEY (student_id, subject_id)
            )''')