# """Bir cep telefonu fabrikasi (class) oldugunu ve bu fabrikada uretilmis 5 farkli model (obje) uretildigini
# dusunelim. Telefonun id,marka, model, uretim yili, tel nosu gibi ozelliklere sahip olsun (Instance Attributes).
# Yazdigimiz kod ile herbir telefonun ozelliklerine tek tek ulasabildigimiz gibi herhangi bir telefonun tum
# bilgilerinede (instance methot) ulasabilelim."""
class Phone():   #Define Phone() calass
    def __init__(self,id, brand, model, year_of_manufacture, phone_number):  #We define def init function
        self.id = id
        self.brand=brand
        self.model = model
        self.year_of_manufacture =year_of_manufacture
        self.phone_number = phone_number
    def generalImformation(self):  #All imformation of tlephones,We define function
        print("""id:{}
                brand:{}
                model:{}
                year_of_manufacture:
                phone_number:""".format(self.id,self.brand,self.model,self.year_of_manufacture,self.phone_number))
samsung1=Phone("12345","samsung","s7","2018","5452346778")  #We insert 3 telephones
samsung2=Phone("13579","samsung","A50","2019","5552646798")
samsung3=Phone("90065","samsung","Note10","2020","5542000900")

print(samsung1.id)   #We can ask any imformation of telephone
print(samsung2.brand)
print(samsung3.model)

samsung1.generalImformation() #We can ask all imformation of telephones
samsung2.generalImformation()
samsung3.generalImformation()





