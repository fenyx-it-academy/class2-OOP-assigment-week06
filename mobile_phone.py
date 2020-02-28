""""
Bir cep telefonu fabrikasi (class) oldugunu ve bu fabrikada uretilmis 5 farkli model (obje) uretildigini dusunelim.
Telefonun id,marka, model, uretim yili, tel nosu gibi ozelliklere sahip olsun (Instance Attributes).
Yazdigimiz kod ile herbir telefonun ozelliklerine tek tek ulasabildigimiz gibi herhangi bir telefonun
tum bilgilerinede (instance methot) ulasabilelim.
"""

class factory_of_mobile():
    def __init__(self, idd, brand, model, year, tel_number):
        self.idd = idd
        self.brand = brand
        self.model = model
        self.year = year
        self.tel_number = tel_number

    def general_info(self):
       return "ID : {}, BRAND : {}, MODEL : {}, YEAR OF PRODUCTION : {}, TELEPHONE NUMBER   : {} ".format(self.idd,
                self.brand,self.model,self.year,self.tel_number)


phone1 = factory_of_mobile(12415235425,"iphone","asd",1990, "05004353233" )
print(phone1.general_info())