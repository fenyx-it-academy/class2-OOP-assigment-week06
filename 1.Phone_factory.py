class Factory:  # We define a class named Factory.

    def __init__(self, identity, brand, model, year, number):  # We define the demanded instance attributes.
        self.identity = identity
        self.brand = brand
        self.model = model
        self.year = year
        self.number = number

    def info(self):  # We define a function to access all of the information for each instance.
        return f"""Phone Information
Identity: {self.identity}
Brand: {self.brand}
Model: {self.model}
Production year: {self.year}
Phone number: {self.number}"""


samsung = Factory(12345, 'Samsung', 'Galaxy S10', 2018, 505123450)  # We enter the necessary info of each object.
lg = Factory(12346, 'LG', 'G7', 2019, 505123451)
iphone = Factory(12347, 'Iphone', '7', 2017, 505123452)
huawei = Factory(12348, 'Huawei', 'P30', 2018, 505123453)
nokia = Factory(12349, 'Nokia', '5.1 Plus', 2019, 505123454)

# Example outputs
print(lg.model)
print(samsung.info())