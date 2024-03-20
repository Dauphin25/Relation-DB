from school_database import c


class Teacher:
    def __init__(self, name, surname, experience_year):
        self.name = name
        self.surname = surname
        self.experience_year = experience_year
        c.execute('''INSERT INTO teachers (name, surname, years_of_experience)
                    VALUES (?, ?, ?)''', (self.name, self.surname, self.experience_year))

    def __repr__(self):
        return "<Teacher: {} {} teaching {} years>".format(self.name, self.surname, self.experience_year)

    @classmethod
    def remove(cls, teach_id):
        c.execute("DELETE FROM teachers WHERE teach_id = {}".format(teach_id))

    @classmethod
    def get_all_teachers(cls):
        c.execute('''SELECT * FROM teachers''')
        teachers = c.fetchall()
        for teacher in teachers:
            print(teacher)

    @classmethod
    def very_experianced_teachers(cls):
        c.execute("select * from teachers where  years_of_experience > 7")
        teachers = c.fetchall()
        print("MY EXPERIENCED TEACHERS")
        for teacher in teachers:
            print(teacher)
        print("END OF MY EXPERIENCED TEACHERS")

    def get_id(self):
        c.execute('''SELECT teach_id FROM teachers 
                     WHERE name = ? AND surname = ? AND years_of_experience = ?''',
                  (self.name, self.surname, self.experience_year))
        teach_id = c.fetchone()
        if teach_id:
            teach_id = teach_id[0]
            return teach_id
