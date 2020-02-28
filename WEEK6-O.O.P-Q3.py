"""Bir okul dusunelim bu okulda ogrencilerden olusan objeler olusturalim her ogrencinin tc,isim,soyisim,matematik yil
sonu not ortolamasi,fizik ders sonu not ortalamasi, turkce yil sonu not ortalamasi bilgileri olsun.

a)okulda kac ogrencinin oldugunu gosteren b) her bir dersten gecme notunun 50 oldugunu dusunursek matematik dersinden
gecen ogrencilerin ismini gosteren fizik dersinden gecen ogrencilerin ismini gosteren turkce dersinden gecen isimlerin
ismini ve notlarini birlikte gosteren c)uc notun ortalamasinin 50 ustunde olanlarin isi sinifi gectigini dusunursek
sinifi gecenlerin tum bilgilerini gosteren programi yaziniz."""

class Students():      #We define a class and define 6 empty list for using class method
        sayac = 0
        mathlist = []
        physicslist = []
        turkishlist = []
        namelist = []
        surnamelist = []
#We define init func for using class
        def __init__(self, id_no, name, surname, mathscore, physicsscore, turkishscore):
            self.id_no = id_no
            self.name = name
            self.surname = surname
            self.mathscore = mathscore
            self.physicsscore = physicsscore
            self.turkishscore = turkishscore
            Students.sayac = Students.sayac + 1
            Students.mathlist.append(self.mathscore)
            Students.physicslist.append(self.physicsscore)
            Students.turkishlist.append(self.turkishscore)
            Students.namelist.append(self.name)
            Students.surnamelist.append(self.surname)

        @classmethod                #Define mathpass function as class method.if >=50 we print
        def mathpass(cls):
            for i in range(len(Students.mathlist)):
                if int(Students.mathlist[i])>= 50:
                    print("Students pass math:",Students.namelist[i], Students.mathlist[i])

        @classmethod
        def physicspass(cls):         #Define physicspass function as class method. if >=50 we print
            for j in range(len(Students.physicslist)):
                if int(Students.physicslist[j]) >= 50:
                    print("Students pass physics:",Students.namelist[j], Students.physicslist[j])

        @classmethod
        def turkishpass(cls):        #Define turkishpass function as class method .if >=50 we print
            for k in range(len(Students.turkishlist)):
                if int(Students.turkishlist[k]) >= 50:
                    print("Students pass turkish:",Students.namelist[k], Students.turkishlist[k])

        @classmethod  #Define succesfulpass function as class method .if average >=50 we print all imformation stdnts
        def succesfulpass(cls):
            for m in range(len(Students.turkishlist)):
                if (int(Students.mathlist[m])+int(Students.physicslist[m])+int(Students.turkishlist[m]))/3>=50:
                    print("""SUCCESFUL STUDENTS IMFORMATION:
                    Name:{}
                    Surname:{}
                    MathScore:{}
                    PhysicsScore:{}
                    TurkishScore:{}
                    """.format(Students.namelist[m],Students.surnamelist[m],Students.mathlist[m],
                               Students.physicslist[m],Students.turkishlist[m]))



ali=Students("20034578912","Ali","Kaya",65,45,76)          # We entered imformation of students
kadir=Students("27834578456","Kadir","Sevinc",35,40,56)
simge=Students("29034578005","Simge","cicek",90,60,40)
print("There are",Students.sayac,"students in the class")  #number of student
Students.mathpass()        #Math pass
Students.physicspass()     #physics pass
Students.turkishpass()     #Turkish pass
Students.succesfulpass()   #Succesful student printing