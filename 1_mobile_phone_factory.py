"""
Suppose that, there is a mobile phone factory (class) and 5 different models (objects) produced in this factory.
The phone has some attributes such as id, brand, model, year of production and number (Instance Attributes).
Access whole information of any phone (instance method) by the code we have written, as well as the attributes of each phone one by one.

"""

# define a class 
class MobilePhoneFactory():
    
    # define instance attributes
    def __init__(self, pid, brand, model, year, pnumber):
        self.apid = pid
        self.abrand = brand
        self.amodel = model
        self.ayear = year
        self.apnumber = pnumber


    # instance method
    def PrintMPhoneInfo(self):
        return("""
        Id of phone = {},
        Brand of phone = {},
        Model of phone = {},
        Date of production = {},
        Number of phone = {}. 
        """.format(self.apid, self.abrand, self.amodel, self.ayear, self.apnumber))


# Instantiate 5 mobile phone objects
samsung = MobilePhoneFactory("12345", "Samsung", "Galaxy 5", "2015", "06 123 45 67")
mi = MobilePhoneFactory("67890", "Mi", "ReadGo", "2016", "07 456 12 23")
apple = MobilePhoneFactory("00000", "Iphone", "11Pro", "2019", "09 156 10 20")
huawei = MobilePhoneFactory("98765", "Huawei", "P30 Lite", "2020", "01 986 12 23")
nokia = MobilePhoneFactory("99999", "Nokia", "6300", "2006", "07 456 33 55")

# Access the instance attributes
print("1. object :", samsung.PrintMPhoneInfo())
print("2. object :", mi.PrintMPhoneInfo())
print("3. object :", apple.PrintMPhoneInfo())
print("4. object :", huawei.PrintMPhoneInfo())
print("5. object :", nokia.PrintMPhoneInfo())



# The End