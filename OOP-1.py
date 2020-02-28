# Bir cep telefonu fabrikasi (class) oldugunu ve bu fabrikada uretilmis 5 farkli model (obje) uretildigini dusunelim.
# Telefonun id,marka, model, uretim yili, tel nosu gibi ozelliklere sahip olsun (Instance Attributes).
# Yazdigimiz kod ile herbir telefonun ozelliklerine tek tek ulasabildigimiz gibi herhangi bir telefonun
# tum bilgilerinede (instance methot) ulasabilelim.

class mobilephone:
    def __init__(self,id,marka,model,productyear,number):
        self.id= id
        self.marka= marka
        self.model=model
        self.productyear=productyear
        self.number=number

    def featurePhone(self):
        return 'id={} marka={} model={} productyear={} number={}'.format(self.id,self.marka,self.model,self.productyear,self.number)

phone1=mobilephone('1','iphone','6S',2017,5052123565)
phone2=mobilephone('2','Samsung','A5',2016,5334445566)
phone3=mobilephone('3','Huawei','E',2015,5447778899)
phone4=mobilephone('4','Sony','Ericsson',2014,5361112244)
phone5=mobilephone('5','Nokia','Lumia',2013,5542229988)

print(phone1.number)#istedigimiz telefonun istedigimiz ozelligini bu sekilde ulasabiliriz
print(mobilephone.featurePhone(phone2))#herhangi bir telefonun tum bilgilerine ulasabiliriz






