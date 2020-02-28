
# define a class 
class SchoolStudent():

    # Class Attributes
    student_number = 0
    PASSING_GRADE = 50
    grade_math_list = []
    grade_physic_list = []
    grade_turkish_dict = {}
    class_grade_list = []


    # define instance attributes
    def __init__(self, tc, name, surname, math, physic, turkish):
        self.atc = int(tc)
        self.aname = name
        self.asurname =surname
        self.amath = int(math)
        self.aphysic = int(physic)
        self.aturkish = int(turkish)
        SchoolStudent.student_number = SchoolStudent.student_number + 1
        if self.amath >= SchoolStudent.PASSING_GRADE:
            SchoolStudent.grade_math_list.append(self.aname) 
        if self.aphysic >= SchoolStudent.PASSING_GRADE:
            SchoolStudent.grade_physic_list.append(self.aname)
        if self.aturkish >= SchoolStudent.PASSING_GRADE:
            SchoolStudent.grade_turkish_dict[self.aname] = self.aturkish   
             
        if self.amath >= SchoolStudent.PASSING_GRADE and self.aturkish >= SchoolStudent.PASSING_GRADE and self.aturkish >= SchoolStudent.PASSING_GRADE:
            SchoolStudent.class_grade_list.append([self.GetGradedStudentInfo()])
       

    # instance method
    def GetGradedStudentInfo(self):
        return("Tc Number = {}, Name = {}, Surname = {}, Math = {}, Physic = {}, Turkish = {} ".format(self.atc, self.aname, self.asurname, self.amath, self.aphysic, self.aturkish))


# Instantiate 6 student objects
student1 = SchoolStudent(12345678902, "Ali", "Yildiz", 45, 55, 75)
student2 = SchoolStudent(55555678902, "Veli", "Ay", 90, 99, 66)
student3 = SchoolStudent(12785678902, "Hans", "Hengelo", 77, 20, 10)
student4 = SchoolStudent(12005678902, "Carin", "Mars", 40, 49, 77)
student5 = SchoolStudent(12115678902, "Venus", "Sun", 57, 58, 90)
student6 = SchoolStudent(12345678643, "Deli", "Dag", 90, 88, 75)


# print count of students
print("\nThere are {} students in the school".format(SchoolStudent.student_number))

print(50 * '=')
# print name of achieved students in  math

for i in SchoolStudent.grade_math_list:
    print("The name of studets who is achieved in the math lesson ; {}".format(i))
print(50 * '=')

# print name of achieved students in  physic
for j in SchoolStudent.grade_physic_list:
    print("The name of studets who is achieved in the physic lesson ; {}".format(j))
print(50 * '=')

# print name of achieved students in turkish lesson and achieved grade
for k, v in SchoolStudent.grade_turkish_dict.items():
    print("{} achieved in the turkish lesson with {} grade. ".format(k,v))   
print(50 * '=')

# to continue next class who could achieve in whole the lessons
for g in SchoolStudent.class_grade_list:
    print("Information of succesfull students : ", g)



    # the End