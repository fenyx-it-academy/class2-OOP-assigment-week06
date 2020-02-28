class School:  # We define a class named School

    # We define class attributes to record the info of all students.
    idns = []
    names = []
    surnames = []
    math_grades = []
    physics_grades = []
    turkish_grades = []
    averages = []
    counter = 0  # We define a counter to record total number of students.

    def __init__(self, idn, name, surname, math, physics, turkish):  # We define the demanded instance attributes.
        self.idn = idn
        self.name = name
        self.surname = surname
        self.math = math
        self.physics = physics
        self.turkish = turkish
        School.idns.append(self.idn)  # We add each instance attribute to the concerning list.
        School.names.append(self.name)
        School.surnames.append(self.surname)
        School.math_grades.append(self.math)
        School.physics_grades.append(self.physics)
        School.turkish_grades.append(self.turkish)
        average = (self.math+self.physics+self.turkish)/3  # We define a variable to calculate average grade.
        School.averages.append(average)  # We add grade average for each student to the concerning list.
        School.counter = School.counter + 1  # We add +1 to the counter for each student.

    @classmethod
    def total_students(cls):  # We define a class method to display total number of students.
        print(f"Total number of students: {School.counter}\n")

    @classmethod  # We define a class method to display students who passed Math.
    def math_pass(cls):
        print("Students passed Math\n")
        for i in range(len(School.idns)):
            if School.math_grades[i] >= 50:
                print(f"{School.names[i]} {School.surnames[i]}: {School.math_grades[i]}")

    @classmethod  # We define a class method to display students who passed Physics.
    def physics_pass(cls):
        print("\nStudents passed Physics\n")
        for i in range(len(School.idns)):
            if School.physics_grades[i] >= 50:
                print(f"{School.names[i]} {School.surnames[i]}: {School.physics_grades[i]}")

    @classmethod  # We define a class method to display students who passed Turkish.
    def turkish_pass(cls):
        print("\nStudents passed Turkish\n")
        for i in range(len(School.idns)):
            if School.turkish_grades[i] >= 50:
                print(f"{School.names[i]} {School.surnames[i]}: {School.turkish_grades[i]}")

    @classmethod  # We define a class method to display all information of the students who passed school.
    def school_pass(cls):
        print("\nStudents passed school\n")
        for i in range(len(School.idns)):
            if School.averages[i] > 50:
                print(f"""ID Number: {School.idns[i]}
Name: {School.names[i]}
Surname: {School.surnames[i]}
Math grade: {School.math_grades[i]}
Physics grade: {School.physics_grades[i]}
Turkish grade: {School.turkish_grades[i]}
Average grade: {School.averages[i]:.2f}\n""")


# We enter the necessary info for each object.
ahmet = School(12345, 'Ahmet', 'Bozkus', 70, 80, 90)
zehra = School(12349, 'Zehra', 'Yuce', 80, 85, 95)
mehmet = School(12346, 'Mehmet', 'Akca', 60, 70, 49)
ayse = School(12347, 'Ayse', 'Kara', 60, 49, 70)
fatma = School(12348, 'Fatma', 'Beyaz', 49, 75, 85)
ali = School(12350, 'Ali', 'Erbil', 50, 50, 49)
cansu = School(12351, 'Cansu', 'Celik', 49, 50, 50)
cihan = School(12352, 'Cihan', 'Kuscu', 50, 49, 50)

# Example outputs
School.total_students()
School.math_pass()
School.physics_pass()
School.turkish_pass()
School.school_pass()