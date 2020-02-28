class TelFactory():

    brand="Nokia" # This is a class attribute.

    def __init__(self, id, model, year, number): # These are instance attributes.

        self.id=id
        self.model=model
        self.year=year
        self.number=number

    def qualities(self): # This is an instance methode.
        return f""" 
BRAND   : {TelFactory.brand}
ID      : {self.id}
MODEL   : {self.model}
YEAR    : {self.year}
NUMBER  : {self.number} \n"""

nokia3310=TelFactory("123987","3310","2002","05321111111")
nokia1100=TelFactory("123654","1100","2003","05322222222")
nokia6600=TelFactory("123486","6600","2005","05323333333")
nokia7610=TelFactory("123578","7610","2006","05324444444")
nokia8110=TelFactory("123613","8110","2007","05325555555") #These are objects.

print(nokia3310.qualities())
print(nokia6600.year)
print(nokia7610.id)
print(TelFactory.brand)