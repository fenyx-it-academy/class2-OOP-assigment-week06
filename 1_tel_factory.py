class Factory:
    def __init__(self, tel_id, brand, product_year, tel_no):
        self.tel_id = tel_id
        self.brand = brand
        self.product_year = product_year
        self.tel_no = tel_no

    def product_info(self):
        return (f'Tel Id: {self.tel_id}\n'
                f'Brand: {self.brand}\n'
                f'Product Year: {self.product_year}\n'
                f'Tel No: {self.tel_no}')


tel1 = Factory('1234567888', 'Samsung', 1990, '0613739591')
tel2 = Factory('7750283843', 'Xiaomi', 1995, '0682091809')
tel3 = Factory('9832183080', 'Iphone', 2000, '0698409843')
tel4 = Factory('8327770288', 'Nokia', 2004, '0698430398')
tel5 = Factory('8378973298', 'Motorola', 2007, '0643098439')

print(tel1.brand)
print(tel1.product_info())
