from school_database import c


class Subject:
    def __init__(self, title, duration, credits, teacher):
        self.title = title
        self.duration = duration
        self.credits = credits
        self.teacher = teacher
        c.execute('''INSERT INTO subjects (title, duration, credits, teacher_id) VALUES (?, ?, ?, ?)''',
                  (self.title, self.duration, self.credits, self.teacher.get_id()))

    def __repr__(self):
        return "<Subject: {} lasts {} weeks, have {} credits and teaches {}>".format(self.title, self.duration,
                                                                                     self.credits, self.teacher.surname)

    @classmethod
    def delete_subject(cls, subject_id):
        c.execute('''DELETE FROM subjects WHERE subject_id = ?''', subject_id)

    @classmethod
    def get_all_subjects(cls):
        c.execute('''SELECT * FROM subjects''')
        subjects = c.fetchall()
        for subject in subjects:
            print(subject)

    @classmethod
    def long_subjects(cls):
        c.execute("SELECT * FROM subjects WHERE duration > 14")
        subjects = c.fetchall()
        print("MY LONG SUBJECTS")
        for subject in subjects:
            print(subject)
        print("END OF MY LONG SUBJECTS")

    def get_id(self):
        c.execute('''SELECT subject_id FROM subjects 
                     WHERE title = ? AND duration = ? AND credits = ? AND teacher_id = ?''',
                  (self.title, self.duration, self.credits, self.teacher.get_id()))
        subject_id = c.fetchone()
        if subject_id:
            subject_id = subject_id[0]
            return subject_id
