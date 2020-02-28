""""
Uc (obje) adet cep telefonuna (class) sahip oldugumuzu dusunelim. Cep telefonlarinin modeli,hangi tarihte aldigimiz
ve ne kadara aldigimiz bilgileri ile birlikte her telefona ait rehber bilgisi olsun (instance attribute)
(rehber bilgisini her objeye ait bir sozluk tanimlayarak olusturula bilinir). Daha sonra her cep telefonundaki
rehberden kisi bulma-search (instance methot) kisi ekleme (instance methot) ve kisi silme secenekleri olsun.

yazacagimiz kod ile

1) tum telefon bilgilerini getirme (classmethod)
2) ayri ayri telefon bilgilerini getirme (instance method)
3) telefon fiyatlarini kucukten buyuge dogru siralama (class methot)
4) her bir telefona

	a) Rehberi goruntuleme (instance method)

    b) rehberde kisi varmi yokmu aramasi yapma (instance method)

	c) rehbere kisi ekleme (eger ayni kisi varsa uyari vermeli ve tekrar sorgu ekranina donmeli)(instance method)
(yazacaginiz if else gibi sorgulama komutlarini instance methot icindede yazabilirsiniz)

	d) rehberden kisi silme ( eger silinmesini istedigimiz kisi yok ise uyari vermeli)(instance method)
"""
class MobilePhone:

    model1 = []
    year1 = []
    amount1 = []

    def __init__(self, model, year, amount, phone_book):
        self.model = model
        self.year = year
        self.amount = amount
        self.phone_book = phone_book
        MobilePhone.model1.append(self.model)
        MobilePhone.year1.append(self.year)
        MobilePhone.amount1.append(self.amount)

    @classmethod
    def general_info(cls):
        print("--General Information--")
        for i in range(len(MobilePhone.model1)):
            print("Model : {}, Year : {}, Amount : {}".format(MobilePhone.model1, MobilePhone.year1, MobilePhone.amount1))


    @classmethod
    def sort_of_amounts(cls):
        return MobilePhone.amount1.sort()


    def phone_info(self):
        return "ID : {} , BRAND : {} , AMOUNT : {} , CONTACTS : {}".format(self.model, self.year, self.amount, self.phone_book)


    def DisplayPhoneBook(self):
        return self.phone_book


    def SearchPerson(self):
        name = input("Please enter the name and surname for search ")

        if name in self.phone_book.keys():
            return "{} --> phone number : {} ".format(name, self.phone_book.get(name))
        else:
            return "Contact not found. "


    def AddPerson(self):
        name = input("Please enter the name and surname for add a contact: ")
        number = input("Please enter the phone number: ")

        if name in self.phone_book.keys():
            return "There is already this contact."
        else:
            self.phone_book[name] = number
            return self.phone_book


    def DeletePerson(self):
        name = input("Enter the name and surname for to remove a contact: ")

        if name in self.phone_book.keys():
            self.phone_book.pop(name)
            return self.phone_book
        else:
            return "The contact not found."

phone1 = MobilePhone("iphone xyz",2019,1000,{"hakan guner" : 12312313123})
print(phone1.model)
print(phone1.SearchPerson())