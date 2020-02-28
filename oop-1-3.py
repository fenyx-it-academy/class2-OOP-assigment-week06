class School():
#We started to write our program by creating lists under the class related to those requested from us.
    students_id=[]
    students=[]
    mathematics = []
    physics = []
    turkish = []
    averages =[]

    def __init__(self,student_id,name_surname,mathematics_grade,physics_grade,turkish_grade):
    #we create our example and add the ones that will be added to the lists as the attributes of our example.
        self.student_id=student_id
        self.name_surname=name_surname
        self.mathematics_grade=mathematics_grade
        self.physics_grade=physics_grade
        self.turkish_grade=turkish_grade
        School.students_id.append(student_id)
        School.students.append(name_surname)
        School.mathematics.append(mathematics_grade)
        School.physics.append(physics_grade)
        School.turkish.append(turkish_grade)
        average=(self.mathematics_grade+self.physics_grade+self.turkish_grade)/3
        School.averages.append(average)

    @classmethod
    def sum_students(cls):#we find out how many students are at school
        cls.x=School.students
        print("Total number of students:",len(cls.x))#we wanted to find out how many people were in the class by finding the length of the list

    @classmethod
    def succesful_mathematics(cls):#we find the successful ones in math class
        print("Students who are successful in mathematics:\n")
        for x in range(len(School.students)):#We find the number of rows with x and
            if School.mathematics[x] >= 50:# we determine that the person in the which row was successful
               print("{}:{}".format(School.students[x],School.mathematics[x]))

    @classmethod
    def succesful_physics(cls):#we find the successful ones in physics class
        print("Students who are successful in physics:\n")
        for x in range(len(School.students)):
            if School.physics[x] >= 50:
                print("{}:{}".format(School.students[x], School.physics [x]))

    @classmethod
    def succesful_turkish(cls):#we find the successful ones in turkish class
        print("Students who are successful in turkish:\n")
        for x in range(len(School.students)):
            if School.turkish[x] >= 50:
                print("{}:{}".format(School.students[x], School.turkish[x]))

    @classmethod
    def average_of_all(cls):
        print("Student information that deserves to pass the class\n")
        for x in range(len(School.students)):
            if School.averages[x]>50:
                print("""
                Student id:{}
                Name and Surname:{}
                Mathematics Grade:{}
                Physics Grade:{}
                Turkish Grade:{}
                Average of all:{}""".format(School.students_id[x],School.students[x],School.mathematics[x],School.physics[x],School.turkish[x],School.averages[x]))

#student information
ali=School(32887507543,'ali ak',90,70,80)
ayse=School(32887507544,'ayse yildiz',95,50,75)
fatma=School(32887507542,'fatma kara',84,90,45)
hasan=School(32887507549,'hasan akdiz',47,90,35)
boris=School(32887507523,'boris ay',25,78,65)
mehmet=School(32887507556,'mehmet efe',55,67,75)
burak=School(32887507578,'burak ak',95,90,85)
zeliha=School(32887507590,'zeliha kay',35,50,45)
aynur=School(32887507567,'aynur yilmaz',75,40,35)
alican=School(32887507514,'alican can',25,80,95)


School.succesful_mathematics()
print("-*"*20)#to prevent confusion to put together stars
School.succesful_physics()
print("-*"*20)
School.succesful_turkish()
print("-*"*20)
School.average_of_all()
print("-*"*20)
ali.sum_students()
print("-*"*20)