"""Uc (obje) adet cep telefonuna (class) sahip oldugumuzu dusunelim. Cep telefonlarinin modeli,hangi tarihte aldigimiz
ve ne kadara aldigimiz bilgileri ile birlikte her telefona ait rehber bilgisi olsun (instance attribute) (rehber
bilgisini her objeye ait bir sozluk tanimlayarak olusturula bilinir). Daha sonra her cep telefonundaki rehberden
kisi bulma-search (instance methot) kisi ekleme (instance methot) ve kisi silme secenekleri olsun.
1) tum telefon bilgilerini getirme (classmethod)
2) ayri ayri telefon bilgilerini getirme (instance method)
3) telefon fiyatlarini kucukten buyuge dogru siralama (class methot)
4) her bir telefona
  a) Rehberi goruntuleme (instance method)
  b) rehberde kisi varmi yokmu aramasi yapma (instance method)
  c) rehbere kisi ekleme (eger ayni kisi varsa uyari vermeli ve tekrar sorgu ekranina donmeli)(instance method)
  (yazacaginiz if else gibi sorgulama komutlarini instance methot icindede yazabilirsiniz)
  d) rehberden kisi silme ( eger silinmesini istedigimiz kisi yok ise uyari vermeli)(instance method)"""
class Telephone:  #We define a class and we define 4 emptey list for usin classmethod
    prices=[]
    models=[]
    product_years=[]
    directories=[]

    def __init__(self,model,product_year,price,directory):
        self.model=model
        self.product_year = product_year
        self.price=price
        self.directory=directory
        self.directory={}
        Telephone.prices.append(self.price)   #we add price,models,etc.. of telephones
        Telephone.models.append(self.model)
        Telephone.product_years.append(self.product_year)
        Telephone.directories.append(self.directory)
    def infor_tel(self):   #We define a function for all imformation of telephone
        print(f'''
                Model: {self.model},
                Product Year: {self.product_year},
                Price:{self.price},
                All contact numbers: {self.directory}''')

    def directory_add(self,name,tel): #We define a fuction for adding a person
        self.directory[name]=tel

    def directory_remove(self,name):  #We define a fuction for removing a person
        if name in self.directory:
            self.directory.pop(name)
            print(f'{name} is deleting...')
        else:
            print(f'{name} is not in Contacts!')

    def directory_see(self):   #We define a function for showing directory
        for name, tel in self.directory.items():
            print(name,":",tel)
    @classmethod   #We define a fuction for sorting of price,We use class method
    def sortfiyat(cls):
        Telephone.prices.sort()
        print(Telephone.prices)

    @classmethod
    def allgeneralphones(cls):  #We define a function for phone features
        a=len(Telephone.prices)
        for i in range(a):
            print("""Model={}
                    Product Year={}
                    Fiyat={}
                    All contact numbers={}


       """.format(Telephone.models[i],Telephone.product_years[i],Telephone.prices[i],Telephone.directories[i]))

phone1=Telephone("X2",2017,"500 euro",directory={})   # We entered phone contents for Class
phone2=Telephone("S6",2020,"300 euro",directory={})   #throw the directory information to be created in dictionary form
phone3=Telephone("K5", 2018, "800 euro", directory={})

print("Please chose one telephone model: \nphone1 \nphone2\nphone3".lower())

chose_phone=input("Chose one telephone: ")  #User choose a phone
if chose_phone=="phone1":
    chose_phone=phone1
if chose_phone=="phone2":
    chose_phone=phone2
else:
    chose_phone=phone3
def menu():                                             # We define a menu
    print("""Menu:
    1. Show this Phone features(model,price,year etc.)
    2. Add new name and number
    3. Show this phone's directory
    4. Delete contact person from this phone
    5. Sort of the all prices of phones  
    6. All registered phone features
    7. Quit""")


while True:     #We set while loop ,In loop we ask menu again and again.and We want a choice from user
    menu()
    number=input("Choose the number you want to make: ")
    try:
        number=int(number)
        if number==1:                                      # all imformation af phone
            chose_phone.infor_tel()
        elif number==2:                                    # Add number
            name=input("Enter name:")
            tel=input("Enter number: ")
            chose_phone.directory_add(name,tel)
        elif number==3:                                    # show directory
            chose_phone.directory_see()
        elif number==4:                                    # Remove a person
            name=input("Enter name which you want to delete: ")
            chose_phone.directory_remove(name)
        elif number==5:                                    #Sort of phone price
            Telephone.sortfiyat()
        elif number==6:
            Telephone.allgeneralphones()                   #phone features
        elif number==7:
            print("Exiting from Menu")                     #Exit the program
            quit()

    except ValueError:
        print("Please enter 1,2,3,4,5,6,7")    #We definr try and excep if we enter a number except 1,2,3,4,5,6,7


