class Phone:  # We define a class named Phone

    models = []  # We define a class attribute named models to record all models.
    years = []  # We define a class attribute named years all years.
    amounts = []  # We define a class attribute named all amounts.

    def __init__(self, model, year, amount, contacts):  # We define the demanded instance attributes.
        self.model = model
        self.year = year
        self.amount = amount
        self.contacts = contacts
        Phone.models.append(self.model)  # We add each instance attribute to related class attribute.
        Phone.years.append(self.year)
        Phone.amounts.append(self.amount)

    @classmethod  # We define a class method to access general info of all phones.
    def general_info(cls):
        print("General Information\n")
        for i in range(len(Phone.models)):
            print(f"Model: {Phone.models[i]}\nYear: {Phone.years[i]}\nAmount: {Phone.amounts[i]}\n")

    @classmethod  # We define a class method to access all amounts paid as sorted.
    def amounts_sorted(cls):
        Phone.amounts.sort()
        return f"Amounts Sorted: {Phone.amounts}\n"

    def phone_info(self):  # We define an instance method to display info of each phone.
        return f"""Phone Information\nIdentity: {self.model}\nBrand: {self.year}\nModel: {self.amount}
Contacts: {self.contacts}"""

    def contact_display(self):  # We define an instance method to display contact info of each phone.
        return self.contacts

    def contact_search(self):  # We define an instance method to search the contacts.
        name = input("Please enter the name and surname of the contact for search: ")
        if name in self.contacts.keys():
            return f"{name}: {self.contacts.get(name)}"
        else:
            return "Contact cannot be found in the list."

    def contact_add(self):  # We define an instance method to add a contact.
        name = input("Please enter the name and surname of the contact to add a contact: ")
        number = input("Please enter the phone number: ")
        if name in self.contacts.keys():
            return "The contact is already in the list."
        else:
            self.contacts[name] = number
            return self.contacts

    def contact_remove(self):  # We define an instance method to remove a contact.
        name = input("Please enter the name and surname of the contact to remove a contact: ")
        if name in self.contacts.keys():
            self.contacts.pop(name)
            return self.contacts
        else:
            return "The contact cannot be found in the list."


# We enter the necessary info for each object.
samsung = Phone("Samsung Galaxy S7", 2018, 400, {'Ozan Tufan': 12345, 'Emre Belozoglu': 54321})
lg = Phone("LG G7", 2017, 250, {'Selcuk Inan': 678910, 'Emre Akbaba': 109876})
iphone = Phone("Iphone X", 2019, 600, {'Burak Yilmaz': 111213, 'Necip Uysal': 131211})

# Example outputs
Phone.general_info()
print(samsung.phone_info())
print(Phone.amounts_sorted())
print(samsung.contact_display())
print(samsung.contact_search())
print(samsung.contact_add())
print(samsung.contact_remove())