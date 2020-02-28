class MobilePhone():

    model=[]
    year=[]
    price=[]

    def __init__(self, model,year,price,phonebook={}):

        self.model=model
        self.year=year
        self.price=price
        self.phonebook=phonebook
        MobilePhone.model.append(self.model)
        MobilePhone.year.append(self.year)
        MobilePhone.price.append(self.price)


    def phone_data(self): # ayrı ayrı telefon bilgisi gösterme. instance method.
        print(f"""
MODEL   :{self.model}
YEAR    :{self.year}
PRICE   :{self.price}\n""")


    def show_phonebook(self): #rehberi görüntüleme. instance method.
        print(self.phonebook)


    def search_name(self): #rehberde kişi sorgulama. instance method.
        name = input("Enter a name you want to search: ").upper()
        if name in self.phonebook:
            print(f"{name} is in your phonebook")
        else:
            print(f"{name} is not in your phonebook")


    def add_person(self): #rehbere kişi ekleme. instance method.
        self.show_phonebook()
        while True:
            name=input("Enter a name you want to add: ").upper()
            if name not in self.phonebook:
                number = input("Enter the number: ")
                self.phonebook[name]=number
                print("The person is added.")
                self.show_phonebook()
                break
            else:
                print(f"{name} is already in the phonebook.")
                again=input("Do you want to add different person? Y/N: ").upper()
                if again=="N":
                    break

    def remove_person(self): #rehberden kişi silme. instance method.
        self.show_phonebook()
        name=input("Enter the name you want to remove: ").upper()
        if name in self.phonebook:
            del self.phonebook[name]
            print(f"{name} is removed from the phonebook")
            self.show_phonebook()
        else:
            print(f"There is no {name} in the phonebook ")


    @classmethod
    def sorted_price(cls): #telefon fiyatlarını küçükten büyüğe sıralama. class method.
        MobilePhone.price.sort()
        print(MobilePhone.price)


    @classmethod
    def all_phones(cls): #tüm telefonların bilgisini gösterme. class method.
        for i in range(len(MobilePhone.model)):
            print(f"""
MODEL   :{MobilePhone.model[i]}
YEAR    :{MobilePhone.year[i]}
PRICE   :{MobilePhone.price[i]}\n""")


siemens=MobilePhone("C45",2001,200,{"AHMET":"06123456", "ABDULLAH":"063528779"}) #
sony=MobilePhone("Xperia",2018,750,{"MUSTAFA":"0665897", "MAHMUT":"065631124"})
samsung=MobilePhone("Note5",2015,400,{"JACK":"06488221", "JOHN":"066633454"})


# MobilePhone.all_phones()
# samsung.phone_data()
# MobilePhone.sorted_price()
# siemens.show_phonebook()
# siemens.add_person()
# sony.remove_person()
# samsung.search_name()