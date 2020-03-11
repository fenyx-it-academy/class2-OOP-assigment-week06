# 3) Bir okul dusunelim bu okulda ogrencilerden olusan objeler olusturalim her ogrencinin tc,isim,soyisim,
# matematik yil sonu not ortolamasi,fizik ders sonu not ortalamasi, turkce yil sonu not ortalamasi bilgileri olsun.
#
# 	a)okulda kac ogrencinin oldugunu gosteren
# 	b) her bir dersten gecme notunun 50 oldugunu dusunursek
# 		matematik dersinden gecen ogrencilerin ismini gosteren
# 		fizik dersinden gecen ogrencilerin ismini gosteren
# 		turkce dersinden gecen ogrencilerin ismini ve notlarini birlikte gosteren
# 	c)uc notun ortalamasinin 50 ustunde olanlarin ise sinifi gectigini dusunursek sinifi gecenlerin
# tum bilgilerini gosteren programi yaziniz.


class School:
    number_of_students = 0
    idnumbers = []
    names = []
    surnames = []
    av_math_grades = {}
    av_physics_grades = {}
    av_turkish_grades = {}
    av_grades = []

    def __init__(self, idnumber, name, surname, av_math_grade, av_physics_grade, av_turkish_grade):
        self.idnumber = idnumber
        self.name = name
        self.surname = surname
        self.av_math_grade = av_math_grade
        self.av_physics_grade = av_physics_grade
        self.av_turkish_grade = av_turkish_grade
        School.number_of_students += 1
        if self.av_math_grade >= 50:
            School.av_math_grades[self.name] = self.av_math_grade
        if self.av_physics_grade >= 50:
            School.av_physics_grades[self.name] = self.av_physics_grade
        if self.av_turkish_grade >= 50:
            School.av_turkish_grades[self.name] = self.av_turkish_grade
        if (self.av_math_grade + self.av_physics_grade + self.av_turkish_grade)/3 >= 50:
            self.pass_grade = round((self.av_math_grade + self.av_physics_grade + self.av_turkish_grade)/3, 2)
            School.av_grades.append([self.idnumber, self.name, self.surname, self.av_math_grade, self.av_physics_grade, self.av_turkish_grade, self.pass_grade])

    @classmethod
    def students_pass(cls):
        print('Succeded in Math Course:')
        for i in School.av_math_grades:
            print(i, ':', School.av_math_grades[i])
        print('Succeded in Physics Course:')
        for i in School.av_physics_grades:
            print(i, ':', School.av_physics_grades[i])
        print('Succeded in Turkish Course:')
        for i in School.av_turkish_grades:
            print(i, ':', School.av_turkish_grades[i])

    @classmethod
    def class_pass(cls):
        print('Succeded in all Courses:\n')
        for i in School.av_grades:
            print(f'''ID: {i[0]} \nName: {i[1]} \nSurname: {i[2]} \nMath Grade: {i[3]} \nPhysics Grade: {i[4]} \nTurkish Grade: {i[5]} \nGraduation Grade: {i[6]}\n''')


student1 = School(23658495845, 'Dave', 'Smith', 60, 40, 70)
student2 = School(43256598412, 'Mary', 'Jones', 70, 30, 40)
student3 = School(25695481523, 'Jane', 'Williams', 45, 90, 60)

# print(School.number_of_students)
# School.students_pass()
# School.class_pass()
