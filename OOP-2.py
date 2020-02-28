#1) tum telefon bilgilerini getirme (classmethod)
	#2) ayri ayri telefon bilgilerini getirme (instance method)
	#3) telefon fiyatlarini kucukten buyuge dogru siralama (class methot)
	#4) her bir telefona
	#	a) Rehberi goruntuleme (instance method)
    #   	b) rehberde kisi varmi yokmu aramasi yapma (instance method)
	#	c) rehbere kisi ekleme (eger ayni kisi varsa uyari vermeli ve tekrar sorgu ekranina donmeli)
    #	    (instance method) (yazacaginiz if else gibi sorgulama komutlarini instance methot icindede yazabilirsiniz)
	#	d) rehberden kisi silme ( eger silinmesini istedigimiz kisi yok ise uyari vermeli)(instance method)

class mobilphone:
    models=[]
    dates=[]
    prices=[]
    rehbers=[]
    def __init__(self,model,date,price,rehber):
        self.model=model
        self.date=date
        self.price=price
        self.rehber=dict(rehber)
        mobilphone.models.append(self.model)
        mobilphone.dates.append(self.date)
        mobilphone.prices.append(self.price)
        mobilphone.rehbers.append(self.rehber)

    def ozellik(self):
        return 'model= {} date= {} price= {} rehber= {}.'.format(self.model,self.date,self.price,self.rehber)

    @classmethod
    def price_sorted(cls):
        mobilphone.prices.sort()
        return mobilphone.prices

    def findPerson(self):
        self.contact = input("Please enter a name: ")
        if self.contact in self.rehber:
            print(self.contact,'is in contacts')
        else:
            print(self.contact,'is not in contacts')

    def addPerson(self):
        b=input('Please enter a name for saving in contacts: ')
        c=int(input('please enter phone numbers for saving in contacts: '))
        for i in self.rehber.keys():
            #print(i)
            if not b in i:
                d=dict([(b,c)])
                #print(d)
                self.rehber.update(d)
                print(self.rehber)
            else:
                print('{} is already in contacts'.format(b))
                continue

    def delPerson(self):
        self.contact = input('please a name for erasing in contacts: ')
        if self.contact in self.rehber:
            self.rehber.pop(self.contact)
            print(list(self.rehber))
        else:
            print('It is not in contacts')


    @classmethod# tum bilgiler ekrana yazdirilabilir class method ile
    def allphoneinformation(cls):
        a = len(mobilphone.models)
        for i in range(a):
            print("""model={} date={} price={} rehber={}""".format(mobilphone.models[i], mobilphone.dates[i], mobilphone.prices[i],mobilphone.rehbers[i]))
                            





phone1=mobilphone('iphone',2017,700,{'ali':5505050500, 'veli':654454564})
phone2=mobilphone('Samsung',2016,600,{'cem':7777777, 'can':888888})
phone3=mobilphone('Huawei',2015,500,{'sem':111111, 'kubi':222222})





mobilphone.allphoneinformation()#tum kullanici bilgileri ekrana yazdirilabilir
print(mobilphone.ozellik(phone1))#ayri ayri telefon bilgilerini getirme
print(mobilphone.price_sorted()) #telefon fiyatlarini kucukten buyuge siralama
mobilphone.findPerson(phone1)#rehberden numara sorgulanabilir
mobilphone.addPerson(phone2)#rehbere kisi eklenebilir
mobilphone.delPerson(phone3)#rehberden kisi silinebilir


