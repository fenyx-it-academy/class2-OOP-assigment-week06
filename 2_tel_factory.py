class TelFactory:
    telefons = []

    def __init__(self, brand, buy_date, price, person_list):
        self.buy_date = buy_date
        self.brand = brand
        self.price = price
        self.person_list = person_list
        TelFactory.telefons.append(self)

    def info(self):  # bir telefonun bilgisini veriyoruz
        return {
            'Telephone Merk': self.brand,
            'Buy Date': self.buy_date,
            'Product Price': self.price,
            'Contact Numbers': self.person_list
        }

    def persons(self):  # telefon rehberindeki kisileri ekrana basiyoruz
        for names, tel in self.person_list.items():
            print(names, ":", tel)

    def search(self, name):  # searh instance metodu ile rehberden kisi buluyoruz
        if name in self.person_list:
            print(f'{name} is find')
            return name + ':' + self.person_list[name]
        else:
            return 'this person is not in your list'

    def add(self, name, number):  # telefon rehberine kisi ekleme
        while True:
            if name in self.person_list:
                print(f'{name} is already your list')
                continue
            else:
                self.person_list[name] = number
                return f'{name} is added'

    def delete(self, name):  # herhangi bir telefonun rehberinden bir kisiyi siliyoruz
        if name in self.person_list:
            self.person_list.pop(name)
            return f'{name} is deleted'
        else:
            return 'this person is not in your list'

    @classmethod  # class method ile  uretilen tum telefon bilgileri ekrana basiliyor
    def tel_infos(cls):
        for i in cls.telefons:
            for j, k in cls.info(i).items():
                if j == 'Contact Numbers':
                    print(j, ':')
                    for a in k:
                        print(a, ':', k[a])
                else:
                    print(j, ':', k)

    @classmethod  # class method ile tum telefon fiyatlari kucukten buyuge dogru siralandi
    def prices(cls):
        prices = [k for i in cls.telefons for j, k in cls.info(i).items() if j == "Product Price"]
        return sorted(prices)


tel1 = TelFactory('Samsung', 1990, 800, {'ahmet': '0613739592', 'taha': '0613738571', 'mert': '0614734583'})
tel2 = TelFactory('Xiaomi', 1995, 2000, {'ali': '0679870980', 'yakup': '0600068754', 'murat': '0614734763'})
tel3 = TelFactory('Iphone', 2000, 500, {'yusuf': '0613123456', 'mukremin': '0672345612', 'salih': '0678456212'})

print(TelFactory.tel_infos())
# print(TelFactory.prices())
# print(tel1.info())
# print(tel1.search('ahmet'))
# print(tel1.add('mehmet', '0671356265'))
# print(tel1.persons())
# print(tel1.delete('taha'))
# print(tel1.persons())
