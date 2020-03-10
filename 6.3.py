class School:
    Name = []
    Surname = []
    Student_number = []
    Math_score = []
    Physics_score = []
    Turkish_score = []
    counter = 0
    Math_score_high = []
    Physics_score_high = []
    Turkish_score_high = []
    High_score_board = []

    def __init__(self, name, surname, student_number, math_score, physics_score, turkish_score):
        self.name = name
        self.surname = surname
        self.student_number = student_number
        self.math_score = math_score
        self.physics_score = physics_score
        self.turkish_score = turkish_score
        School.Name.append(self.name)
        School.Surname.append(self.surname)
        School.Student_number.append(self.student_number)
        School.Math_score.append(self.math_score)
        School.Physics_score.append(self.physics_score)
        School.Turkish_score.append(self.turkish_score)
        School.counter += 1

    @classmethod
    def total_student(cls):
        print(f"""Total student {School.counter}""")

    @classmethod
    def lesson_high_score(cls):
        for i in School.Math_score:
            if i > 50:
                a = School.Math_score.index(i)
                School.Math_score_high.append(School.Name[a])
        print("""Have a high score in math {}""".format(School.Math_score_high))
        for i in School.Physics_score:
            if i > 50:
                a = School.Physics_score.index(i)
                School.Physics_score_high.append(School.Name[a])
        print("""Have a high score in Physics {}""".format(School.Physics_score_high))
        for i in School.Turkish_score:
            if i > 50:
                a = School.Turkish_score.index(i)
                School.Turkish_score_high.append(School.Name[a])
        print("""Have a high score in Turkish {}""".format(School.Turkish_score_high))

    @classmethod
    def high_score_board(cls):
        for i in range(School.counter):
            if ((School.Math_score[i]+School.Physics_score[i]+School.Turkish_score[i])/3) > 50:
                School.High_score_board.append(School.Name[i])
        print("""Have a high score in all lesson {}""".format(School.High_score_board))


student1 = School("Ayse", "Kaya", "24", 70, 30, 45)
student2 = School("Betul", "Yilmaz", "17", 40, 60, 35)
student3 = School("Sena", "Bulut", "10", 80, 40, 60)

# School.lesson_high_score() #Ayri ayri derslerden gecen ogrenci isimleri

# School.high_score_board() #en basarili ogrenci

# School.total_student() #okulda kac ogrenci oldugunu gosteriyor
