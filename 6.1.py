class Phone:
    Brand = []
    Id_phone = []
    Date_of_production = []
    Number = []

    def __init__(self, brand, id_phone, date_of_production, number):
        self.brand = brand
        self.id_phone = id_phone
        self.date_of_production = date_of_production
        self.number = number
        Phone.Brand.append(self.brand)
        Phone.Id_phone.append(self.id_phone)
        Phone.Date_of_production.append(self.date_of_production)
        Phone.Number.append(self.number)


    def information_phone(self):
        print(f"""
Brand : {self.brand}
ID : {self.id_phone}
Date Of Production : {self.date_of_production}
Phone Number : {self.number}""")


Phone1 = Phone("Samsung", "12334553540921", "01.01.2020", "+2637729875932")
Phone2 = Phone("Apple", "1233356820860", "01.02.2020", "+26377562365932")
Phone3 = Phone("Motorola", "4526803820860", "15.02.2020", "+2638958960232")
Phone4 = Phone("Sony", "7534646520860", "26.02.2020", "+26377875976572")
Phone5 = Phone("Huawei", "527492230860", "18.02.2020", "+26359830043202")

#Phone1.information_phone() # instance method ile 1 telefon bilgileri tumu gosteriliyor.

#print(Phone5.brand) # bir telefonun tek bir ozelligine ulasilabiliyor.
#print(Phone3.number)
