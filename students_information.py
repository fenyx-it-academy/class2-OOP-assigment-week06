"""
Bir okul dusunelim bu okulda ogrencilerden olusan objeler olusturalim her ogrencinin tc,isim,soyisim,matematik
yil sonu not ortolamasi,fizik ders sonu not ortalamasi, turkce yil sonu not ortalamasi bilgileri olsun.

a)okulda kac ogrencinin oldugunu gosteren

b) her bir dersten gecme notunun 50 oldugunu dusunursek matematik dersinden
gecen ogrencilerin ismini gosteren fizik dersinden gecen ogrencilerin ismini gosteren turkce dersinden gecen isimlerin
ismini ve notlarini birlikte gosteren

c)uc notun ortalamasinin 50 ustunde olanlarin isi sinifi gectigini dusunursek
sinifi gecenlerin tum bilgilerini gosteren programi yaziniz.
"""

class School:
    idNumbers = []
    names = []
    surnames = []
    math_marks = []
    physics_marks = []
    turkish_marks = []
    averages = []
    counter = 0

    def __init__(self, id_number, name, surname, math_mark, physic_mark, turkish_mark):
        self.id_number = id_number
        self.name = name
        self.surname = surname
        self.math_mark = math_mark
        self.physics_mark = physic_mark
        self.turkish_mark = turkish_mark
        School.idNumbers.append(self.id_number)
        School.names.append(self.name)
        School.surnames.append(self.surname)
        School.math_marks.append(self.math_mark)
        School.physics_marks.append(self.physics_mark)
        School.turkish_marks.append(self.turkish_mark)
        average = (self.math_mark + self.physics_mark + self.turkish_mark) / 3
        School.averages.append(average)
        School.counter = School.counter + 1

    @classmethod
    def total_students(cls):
        print("Students : {}".format(School.counter))


    @classmethod
    def MathPassed(cls):
        print("--LIST OF PASSED MATHEMATIC--")
        for i in range(len(School.idNumbers)):
            if School.math_marks[i] >= 50:
                print(f"{School.names[i]} {School.surnames[i]}: {School.math_marks[i]}")


    @classmethod
    def PhysicsPassed(cls):
        print("--LIST OF PASSED PYHYSICS--")
        for i in range(len(School.idNumbers)):
            if School.physics_marks[i] >= 50:
                print(f"{School.names[i]} {School.surnames[i]}: {School.physics_marks[i]}")


    @classmethod
    def TurkishPassed(cls):
        print("--LIST OF PASSED TURKISH LANGUAGE--")
        for i in range(len(School.idNumbers)):
            if School.turkish_marks[i] >= 50:
                print(f"{School.names[i]} {School.surnames[i]}: {School.turkish_marks[i]}")


    @classmethod
    def SchoolPassed(cls):
        print("--LIST OF PASSED SCHOOL--")
        for i in range(len(School.idNumbers)):
            if School.averages[i] > 50:
                print("ID : {}, NAME : {} , SURNAME : {} , MATH. MARK : {} , PSYSICS MARK : {} , "
                        "TURKISH MARK : {} and AVARAGE : {}"
                            .format(School.idNumbers[i],School.names[i],School.surnames[i],School.math_marks[i],
                                    School.physics_marks[i],School.turkish_marks[i],School.averages[i]))

hakan = School(87654321,"hakan","guner",60,90,100)
print(hakan.averages)









