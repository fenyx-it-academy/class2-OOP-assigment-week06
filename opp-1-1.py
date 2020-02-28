class Manufactory():

    def __init__(self,tel_id,brand,model,production_year,tel_number):
#With the instance method we wrote, we can reach the information of any phone
        self.tel_id=tel_id
        self.brand=brand
        self.model=model
        self.production_year=production_year
        self.tel_number=tel_number

    def show_information(self):#we can access all the information of any phone
        print("Phone id:",self.tel_id)
        print("Phone brand:",self.brand)
        print("Phone model:",self.model)
        print("Phone's year of manufacture:",self.production_year)
        print("Telephone number:",self.tel_number)

#Five different models of the same phone brand
model1=Manufactory(1122232,'samsung',3210,2010,6203055)
model2=Manufactory(1122235,'samsung',3214,2013,6203053)
model3=Manufactory(1122236,'samsung',3216,2014,6203052)
model4=Manufactory(1122237,'samsung',3217,2015,6203051)
model5=Manufactory(1122238,'samsung',3230,2016,6203058)

print(model1.tel_id)
model2.show_information()