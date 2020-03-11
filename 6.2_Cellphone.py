class Cellphone:
    model_list = []
    buy_date_list = []
    buying_price_list = []
    contacts_list = []

    def __init__(self, model, buy_date, buying_price, contacts):
        self.model = model
        self.buy_date = buy_date
        self.buying_price = buying_price
        self.contacts = contacts
        Cellphone.model_list.append(self.model)
        Cellphone.buy_date_list.append(self.buy_date)
        Cellphone.buying_price_list.append(self.buying_price)
        Cellphone.contacts_list.append(self.contacts)

    @classmethod
    def all_phone_info(cls):
        for i in range(len(Cellphone.model_list)):
            print(f'''Model Name: {Cellphone.model_list[i]}
Date of purchase: {Cellphone.buy_date_list[i]}
Buying price: {Cellphone.buying_price_list[i]}
Contacts: {Cellphone.contacts_list[i]}\n''')

    def phone_info(self):
        print(f'''Model Name: {self.model}
Date of purchase: {self.buy_date}
Buying price: {self.buying_price}
Contacts: {self.contacts}\n''')

    @classmethod
    def sort_phones_increasingly(cls):
        Cellphone.sorted_price_list = sorted(Cellphone.buying_price_list)
        for i in range(len(Cellphone.sorted_price_list)):
            print(f'''Model Name: {Cellphone.model_list[Cellphone.buying_price_list.index(Cellphone.sorted_price_list[i])]}
            Buying Price: {Cellphone.sorted_price_list[i]}''')

    def view_contacts(self):
        print(f'Contacts: {self.contacts}')

    def search_contact(self, name):
        if name.capitalize() in self.contacts:
            print(f'There is a person in contacts called {name}')
        else:
            print('No such a person')

    def add_contact(self, name, phone_number):
        if name.capitalize() in self.contacts.keys():
            print('The contact already exists')
        else:
            self.contacts[name.capitalize()] = phone_number

    def delete_contact(self, name):
        if name.capitalize() in self.contacts.keys():
            print(name.capitalize(), ':', self.contacts.pop(name.capitalize()), 'is deleted')
        else:
            print('The person does not exist')


phone1 = Cellphone('Iphone X', '18.10.2017', '1250', {'John': '069887541', 'Mary': '068527458', 'Tom': '062365412'})
phone2 = Cellphone('Galaxy Note10', '01.12.2018', '1175', {'Joe': '061457896', 'Alex': '069857412', 'Sue': '066541258'})
phone3 = Cellphone('Huawei P30', '28.02.2019', '1050', {'Daniel': '068521422', 'Kate': '065236655', 'Lia': '069857789'})

# Cellphone.all_phone_info()
# phone3.phone_info()
# Cellphone.sort_phones_increasingly()
# phone2.view_contacts()
# phone1.search_contact('john')
# phone1.add_contact('john', '062351255')
# phone1.add_contact('dave', '062351255')
# phone1.phone_info()
# phone2.delete_contact('kate')
# phone2.delete_contact('alex')
# phone2.phone_info()
