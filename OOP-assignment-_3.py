class School():

    idnums=[]
    names=[]
    surnames=[]
    math_avr=[]
    phys_avr = []
    turk_avr = []
    year_end_avr=[]
    meter=0

    def __init__(self,idnum,name,surname,math,phys,turk):

        self.idnum=idnum
        self.name=name
        self.surname=surname
        self.math=math
        self.phys=phys
        self.turk=turk

        School.idnums.append(self.idnum)
        School.names.append(self.name)
        School.surnames.append(self.surname)
        School.math_avr.append(self.math)
        School.phys_avr.append(self.phys)
        School.turk_avr.append(self.turk)
        School.year_end_avr.append((self.math + self.phys + self.turk)/3)
        School.meter += 1

    @classmethod
    def tot_students(cls):
        print(f"Total number of students: {School.meter}\n")

    @classmethod
    def lecture_success(cls):
        for i in School.math_avr:
            if i>=50:
                print(f"{School.names[School.math_avr.index(i)]} succeed Math. ")

        for i in School.phys_avr:
            if i>=50:
                print(f"{School.names[School.phys_avr.index(i)]} succeed Physic. ")

        for i in School.turk_avr:
            if i>=50:
                print(f"{School.names[School.turk_avr.index(i)]} succeed Turkish. ")

    @classmethod
    def term_success(cls):
        print("\nStudents passed school:\n")
        for i in School.year_end_avr:
            if i>=50:
                print(f"""
ID      : {School.idnums[School.year_end_avr.index(i)]}
NAME    : {School.names[School.year_end_avr.index(i)]}
SURNAME : {School.surnames[School.year_end_avr.index(i)]}""")

muzaffer = School(348, "Muzaffer", "Beton", 90, 95, 100)
muhsin = School(766, "Muhsin", "Direk", 30, 40, 50)
murtaza = School(542, "Murtaza", "Zil", 40, 45, 50)
murat = School(634, "Murat", "Mazgal", 45, 50, 55)
mustafa = School(965, "Mustafa", "Mezgit", 80, 20, 60)

School.tot_students()
School.lecture_success()
School.term_success()