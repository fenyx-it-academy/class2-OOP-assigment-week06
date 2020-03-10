class Phone:
    Brand = []
    Date_of_purchase = []
    Price = []
    Price_phone_list = []
    Price_list = []
    Person_number_list = []

    def __init__(self, brand, date_of_purchase, price, person_number_list):
        self.brand = brand
        self.date_of_purchase = date_of_purchase
        self.price = price
        self.person_number_list = person_number_list
        Phone.Brand.append(self.brand)
        Phone.Date_of_purchase.append(self.date_of_purchase)
        Phone.Price.append(self.price)
        Phone.Person_number_list.append(self.person_number_list)

    def phone_book(self):
        print("Phone book :" + str(self.person_number_list))

    def find_person(self, x):
        if x in self.person_number_list:
            print(f"""{x} phone number is {self.person_number_list[x]}""")
        else:
            print("Not Found !!!")

    def add_person(self, x, y):
        while True:
            if x in self.person_number_list and self.person_number_list[x] == y:
                print("Already exist.")
                break
            elif x in self.person_number_list and self.person_number_list[x] != y:
                print("Please enter different name!")
                break
            else:
                self.person_number_list[x] = y
                print("Person added..")
                print("Phone book :" + str(self.person_number_list))
                break

    def delete_person(self, x):
        if x in self.person_number_list:
            print(x, self.person_number_list.pop(x), "deleted!!")
            print("Phone book :" + str(self.person_number_list))
        else:
            print("The person you want to delete is not found!")

    def phone_information(self):
        print(f"""Brands : {self.brand}
Date of purchase : {self.date_of_purchase}
Price : {self.price}
Person_number_list : {self.person_number_list}""")

    @classmethod
    def information(cls):
        for i in range(len(Phone.Brand)):
            print(f"""Brands : {Phone.Brand[i]}
Date of purchase : {Phone.Date_of_purchase[i]}
Price : {Phone.Price[i]}
Person_number_list : {Phone.Person_number_list[i]}""")

    @classmethod
    def sorted_price(cls):
        Phone.Price_list = list(sorted(Phone.Price))
        for i in Phone.Price_list:
            Phone.Price_phone_list.append(Phone.Brand[Phone.Price.index(i)])
        print(*zip(Phone.Price_phone_list, Phone.Price_list), sep="\n")


phone1 = Phone("Nokia", "12.12.2008", 2000, {"Ali" : "08367628327", "Veli" : "07645438723"})
phone2 = Phone("Apple", "11.11.2000", 3400, {"Ayse" : "08937382345", "Betul" : "06474323899"})
phone3 = Phone("Samsung", "05.05.2004", 2900, {"Hasan" : "09453215635", "Kubra" : "08463723435"})

# phone3.phone_book() # 3. telefonun rehberi goruntuleniyor.

# phone2.find_person("Ayse")   # telefon 2 rehberde Ayse adli kisi var ve buluyor.
# phone2.find_person("Hasan")  #telefon 2 nin rehberinde Hasan yok bulamiyor

# phone1.add_person("Ali","08367628327") # rehbere eklenecek kisi ve numarasi var.uyari veriyor
# phone1.add_person("Ali","06573458723") # rehbere eklenecek isim var numara farkli . farkli bir isim isteniyor
# phone1.add_person("Ali2","06573458723") # rehbere eklenecek isim ve numara farkli ekleme basarili

# phone2.delete_person("Ayse") # Ayse rehberde var ve siliyor. rehberin son hali gosteriliyor
# phone2.delete_person("Hasan") #rehberde olmayan kisi silinemez.

# Phone.information() # tum telefonlar ve bilgileri classmethod ile gosteriliyor.

# Phone.sorted_price() #telefon fiyatlari kucukten buyuge siralandi..
