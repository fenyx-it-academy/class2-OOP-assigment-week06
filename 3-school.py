class School:
    students = []
    mathematic_pass = {}
    physics_pass = {}
    turks_pass = {}
    sinifi_gecenler = []

    def __init__(self, tc, name, surname, mat, physics, turks):
        self.tc = tc
        self.name = name
        self.surname = surname
        self.mat = mat
        self.physics = physics
        self.turks = turks
        School.students.append(self)
        if int(self.mat) > 50:
            School.mathematic_pass[self.name] = self.mat
        if int(self.physics) > 50:
            School.physics_pass[self.name] = self.physics
        if int(self.turks) > 50:
            School.turks_pass[self.name] = self.turks
        if int(self.physics) > 50 and int(self.mat) > 50 and int(self.turks) > 50:
            School.sinifi_gecenler.append(self.name)

    @classmethod  # class method ile  matematikten gecen tum ogrencileri ekrana basiyoruz
    def mat_student(cls):
        print('matamatikten gecen ogrenciler')
        for i, j in cls.mathematic_pass.items():
            print(i, j)

    @classmethod  # class method ile  fizikten  gecen tum ogrencileri ekrana basiyoruz
    def physics_student(cls):
        for i, j in cls.physics_pass.items():
            print(i, j)

    @classmethod  # class method ile  turkceden gecen tum ogrencileri ekrana basiyoruz
    def turks_student(cls):
        for i, j in cls.turks_pass.items():
            print(i, j)

    @classmethod  # kimlerin sinifi gectigini buluyoruz
    def student_pass(cls):
        for i in cls.sinifi_gecenler:
            print(i)


# sinif_list dosyasindan her ogrenciyi cekip School clasiyla obje olusturuyoruz
with open("sinif_list.txt", "r", encoding="utf-8") as file:
    num = 1
    student = ''
    for line in file:
        line = line[:-1]
        line_list = line.split(" ")
        tc, name, surname, math, physics, turks = line_list
        student = School(tc, name, surname, math, physics, turks)

# a)okulda kac ogrencinin oldugunu gosteren
print(len(School.students))

# matematik dersinden gecen ogrencilerin ismini gosteren
# print(School.mat_student())

# fizik dersinden gecen ogrencilerin ismini gosteren
# print(School.physics_student())

# turkce dersinden gecen isimlerin ismini ve notlarini birlikte gosteren
#  print(School.turks_student())

# c)uc notun ortalamasinin 50 ustunde olanlarin isi sinifi gectigini dusunursek
# sinifi gecenlerin tum bilgilerini gosteren program
# print(School.student_pass())
