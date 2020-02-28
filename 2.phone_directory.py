

# define a class 
class PhoneDirectory():

    # Class Attributes
    model_list = []
    year_list = []
    cost_list = []
    directory_list = []
    
    # define instance attributes
    def __init__(self, model, year, cost, directory):
        self.amodel = model
        self.ayear = year
        self.acost = cost
        self.adirectory = directory
        self.adirectory = {}
        
        PhoneDirectory.model_list.append(self.amodel)
        PhoneDirectory.year_list.append(self.ayear)
        PhoneDirectory.cost_list.append(cost)
        PhoneDirectory.directory_list.append(self.adirectory)


    # instance method add name and number to choosen phone contacts
    def DirectoryInput(self, name, number):
        self.adirectory[name] = number
        
    # instance method delete name and number if name is in choosen phone contacts
    def DeleteContacts(self, name):
        if name in self.adirectory:
            self.adirectory.pop(name)
            print("{} is deleted in {} phone Contacts ".format(name,self.amodel))
        else:
            print("{} is NOT deleted in {} phone Contacts ".format(name,self.amodel))

    # instance method display name and number in choosen phone contacts
    def ShowDirectoryDictionary(self):
        for name, number in self.adirectory.items():
            print("name : {} and number : {} ".format(name, number))

    # instance method search name if it is in choosen phone contacts
    def SearchNameInContacts(self, name):
        if name in self.adirectory.keys():
            print("YES! {} is in {} phone Contacts ".format(name,self.amodel))    
        else:
            print("NO! {} is not in {} phone Contacts ".format(name,self.amodel))
               
    # instance method
    def PrintMPhoneInfo(self):
        return("""
        Model of phone = {},
        Date of purchasing = {},
        Cost of phone = {},
        Directory = {}. 
        """.format(self.amodel, self.ayear, self.acost, self.adirectory))  

    # class method for sorting coasts
    @classmethod
    def cost_sorted(cls):
        cls.cost_list.sort()
        return cls.cost_list

    # class method for getting phone information
    @classmethod
    def GetPhoneInfo(cls):
        a = len(PhoneDirectory.model_list)
        for i in range(a):
            print("""
        Model of phone = {},
        Date of purchasing = {},
        Cost of phone = {},
        Directory = {}. 
        """.format(PhoneDirectory.model_list[i], PhoneDirectory.year_list[i], PhoneDirectory.cost_list[i], PhoneDirectory.directory_list[i]))  



def phone_choose_function():
    # Instantiate 3 mobile phone objects
    mobile_one = PhoneDirectory("Samsung", "2016", 1500, directory = {})
    mobile_two = PhoneDirectory("Nokia", "2007", 150, directory = {})
    mobile_three = PhoneDirectory("Iphone", "2019", 3000, directory = {})

    phone_choose_input = (input(""" 
1- To get whole phones info
2- To sort cost of phones
3- To access Samsung Phone Contacts,
4- To access Nokia Phone Contacts, 
5- To access Iphone Phone Contacts.
Please, enter your choice : """))
    
    if phone_choose_input == "3" :
        first_choose = mobile_one
        return first_choose

    elif phone_choose_input == "4" :
        first_choose = mobile_two
        return first_choose

    elif phone_choose_input == "5" :
        first_choose = mobile_three
        return first_choose
    
    elif phone_choose_input == "2" :      # Access the class method for getting whole phones info
        PhoneDirectory.GetPhoneInfo()
        return phone_choose_input

    elif phone_choose_input == "1" :      # Access the class method for sorting coast
        print("\nsorting cost of phones", PhoneDirectory.cost_sorted() )    
        return phone_choose_input
    else:
        print("\nPlease enter valid number!! ")
        return "1"


def what_you_want_function():
    what_you_want_input = input("""
    1= Add new name and number to The Contacts
    2= Display The Contacts
    3= Search a name in The Contacts
    4= Delete a person in The Contacts
    5= Info of chosen phone
    6= Quit the program
      
    Please, enter your choice : """)
    return what_you_want_input


first_choose = phone_choose_function()

if first_choose == "1" or first_choose == "2":
    whhl_cont = False
else:    
    whhl_cont = True

while whhl_cont == True:
    
    second_choose = what_you_want_function()

    if second_choose == "1" :
        name_surname_input = input("\n\tName of person : ")
        number_input = input("\tPhone number : ")
        first_choose.DirectoryInput(name_surname_input, number_input)
    elif second_choose == "2" :
        first_choose.ShowDirectoryDictionary()
    elif second_choose == "3" :
        name_input = input("\tThe name you called in the contacts: ")
        first_choose.SearchNameInContacts(name_input)
    elif second_choose == "4":
        del_input = input("\tThe name you are going to delete in the contacts: ")
        first_choose.DeleteContacts(del_input)  
    elif second_choose == "5":                    # Access the instance attributes for info of chosen phone 
        print(first_choose.PrintMPhoneInfo())
    elif second_choose == "6":
        print("\nYou Quited The Program!!")
        whhl_cont = False  
    else:
        print("\nPlease enter valid number!! ")      


        
 # The End       
    