
class mobile_factory():
    
    def __init__(self,brand,id, product, year, number):
        self.brand=brand
        self.id=id
        self.product=product
        self.year=year
        self.number=number
        
    
    def general_info(self):
        print('''
    Brand of phone          : {}
    Id of phone             : {}
    Product                 : {}
    Year of product         : {}
    Phone Number of Product : {}
    '''.format(self.brand,self.id,self.product,self.year,self.number))

Iphone=mobile_factory('Iphone','2333','Iphone-11','2019','0623235232')
Samsung=mobile_factory('Samsung','1223','Note-10','2019','0633231244')
Huawei=mobile_factory('Huawei','9923','light','2019','0632235433')
Nokia=mobile_factory('Nokia','3333','Nokia-3310','2005','0645343233')
HTC=mobile_factory('HTC','9933','HTC-33','2013','0644433002')

Iphone.general_info()

