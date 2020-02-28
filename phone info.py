class Mobile_factory:
    Phones = []

    def __init__(self, brand, year, price, contacts):
        self.year = year
        self.brand = brand
        self.price = price
        self.contacts = contacts
        Mobile_factory.Phones.append(self)

    def phone_info(self):  # Giving informations about a phone
        return {
            'Brand of Phone': self.brand,
            'Year of product': self.year,
            'Price': self.price,
            'Contact Numbers': self.contacts
        }

    def contact_info(self):  # showing contact infos
        for names, phoneList in self.contacts.items():
            print(names, ":", phoneList)

    def search(self, name):  # search a person by instance method
        if name in self.contacts:
            print(f'{name} is in your contact list')
            return name + ':' + self.contacts[name]
        else:
            return 'No result!'

    def add(self, name, number):  # Adding
        while True:
            if name in self.contacts:
                print(f'{name} is in your contact list!')
                break
            else:
                self.contacts[name] = number
                return f'{name} is saved'

    def delete(self, name):  # deleting
        if name in self.contacts:
            self.contacts.pop(name)
            return f'{name} is deleted'
        else:
            return 'No result!'

    @classmethod  # all infos by classmethod
    def all_infos(cls):
        for i in cls.Phones:
            for j, k in cls.phone_info(i).items():
                if j == 'Contact Numbers':
                    print(j, ':')
                    for a in k:
                        print(a, ':', k[a])
                else:
                    print(j, ':', k)

    @classmethod  # prices by classmethod
    def prices(cls):
        prices = [k for i in cls.Phones for j, k in cls.phone_info(i).items() if j == "Price of the product"]
        return sorted(prices)


Iphone=Mobile_factory('Iphone-11','2019','1000 Euro\n',{'Alex':'0623235232','Webo':'0623235233','Edu':'0623235234\n'})
Samsung=Mobile_factory('Samsung Note-10','2019','900 Euro\n',{'Van Hoojdonk':'0623235235','Kezman':'0623235235','Skertl':'0623235236\n'})
Huawei=Mobile_factory('Huawei-light','2019','750 Euro\n',{'Lugano':'0623235238','Gokhan':'062323524$\n',})
Nokia=Mobile_factory('Nokia-3310','2005','600 Euro\n',{'Luis Nani':'06232352343','Jailson':'0623235232\n'})
HTC=Mobile_factory('HTC-33','2013','500 Euro\n',{'Kruse':'0623235233','Ozan':'0623235223\n'})

Mobile_factory.all_infos();
Mobile_factory.prices();
Nokia.phone_info()
Iphone.search('Edu')
Samsung.add('Skertl', '0623235236')
Huawei.contact_info()
HTC.delete('Zack')
Iphone.contact_info()