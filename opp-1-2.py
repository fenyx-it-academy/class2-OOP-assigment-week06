class Phone():#We add lists to our class as qualifications in line with the information requested from us.
    brands =[]
    datePurchased=[]
    prices = []

    def __init__(self,brand,date_purchased,price,tel_book):
        self.brand=brand
        self.date_purchased=date_purchased
        self.price=price
        self.tel_book = tel_book
        self.tel_book={}
        Phone.brands.append(self.brand)
        Phone.datePurchased.append(self.date_purchased)
        Phone.prices.append(self.price)

    @classmethod
    def phones_information(cls):#to bring all the phone information
        for i in range(len(Phone.brands)):
            print("""
            Phone brand:{}
            Date purchased:{}
            Phone price:{}""".format(Phone.brands[i], Phone.datePurchased[i],Phone.prices[i]))

    def phone_information(self):#To bring up separate phone information
        print("Phone brand:",self.brand)
        print("Phone date puchased:",self.date_purchased)
        print("Phone price:", self.price)
        print("Phone tel book:", self.tel_book)

    @classmethod
    def sorted_price(cls):  # We sorted the prices from small to large.
        Phone.prices.sort()
        print("Price sorted of phones:",Phone.prices)

    def tel_book_display(self):#we show the phone book
        print("Tel book:",self.tel_book)

    def search(self):#to find people from the phone book
        self.contact=input("Enter the person you want to learn the phone number:")#to search with the name of the person whose number we will ask
        if self.contact in self.tel_book:
            print("Telephone directory information of {}:{}".format(self.contact,self.tel_book[self.contact]))
        else:
            print("The person named {} is not in your tel book!".format(self.contact))

    def contact_add(self):#add contacts to tel book
        self.query=input("The name of the person you want to add to the tel book:")
        if self.query in self.tel_book:
            print("This person is already in the tel book.")

        elif self.query not in self.tel_book:
            x=input("Enter tel number:")
            self.tel_book[self.query]=x #With this method, we add numbers to our contacts.
            print(self.tel_book)

        self.person=input("write the person you want to delete from the tel_book:")
        if self.person not in self.tel_book:
            print("The person named {} you want to delete is not in your guide.".format(self.person))
        #So when we try to delete an item that is not in the dictionary,instead of showing us an error message,
        else:
            self.tel_book.pop(self.person)
            print(self.tel_book)

#our phones and directory information
samsung=Phone("samsung",2013,1000,'tel_book')
samsung.tel_book={'ayse':6789800,'fatma':6578908,'raziye':6789878}
ipone=Phone("ipone",2017,1500,'tel_book')
ipone.tel_book={'ayse':6789800,'fatma':6578908,'raziye':6789878}
nokia=Phone("nokia",2018,1200,'tel_book')
nokia.tel_book={'ayse':6789800,'fatma':6578908,'raziye':6789878}

samsung.tel_book_display()
Phone.sorted_price()
Phone.phones_information()
print(samsung.price)
samsung.phone_information()
print("-*"*20)#to prevent confusion
ipone.phone_information()
print("-*"*20)
nokia.phone_information()
print("-*"*20)
samsung.search()
samsung.contact_add()
