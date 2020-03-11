class CellphoneFactory:
    id_number_list = []
    brand_list = []
    model_list = []
    year_of_production_list = []
    phone_number_list = []

    def __init__(self, id_number, brand, model, year_of_production, phone_number):
        self.id_number = id_number
        self.brand = brand
        self.model = model
        self.year_of_production = year_of_production
        self.phone_number = phone_number
        CellphoneFactory.id_number_list.append(self.id_number)
        CellphoneFactory.brand_list.append(self.brand)
        CellphoneFactory.model_list.append(self.model)
        CellphoneFactory.year_of_production_list.append(self.year_of_production)
        CellphoneFactory.phone_number_list.append(self.phone_number)

    @staticmethod
    def info():
        for i in range(1, 6):
            print(f'''\nID: {CellphoneFactory.id_number_list[i-1]}
Brand name: {CellphoneFactory.brand_list[i-1]}
Model name: {CellphoneFactory.model_list[i-1]}
Production year: {CellphoneFactory.year_of_production_list[i-1]}
Phone number: {CellphoneFactory.phone_number_list[i-1]}''')


phone1 = CellphoneFactory(1001, 'Apple', 'Iphone X', 2018, 5251234561)
phone2 = CellphoneFactory(1002, 'Samsung', 'S10', 2017, 5468954125)
phone3 = CellphoneFactory(1003, 'Huawei', 'P30', 2019, 6985987410)
phone4 = CellphoneFactory(1004, 'Nokia', '3310', 2000, 1568452123)
phone5 = CellphoneFactory(1005, 'Blackberry', 'Keyone', 2010, 5663214890)

# print(phone2.id_number)
# phone5.info()
