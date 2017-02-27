class testClass(object):
    def __init__(self, name, age, zipcode):
        self.name    = name
        self.age     = age
        self.zipcode = zipcode

    def __eq__(self, other): return self == other

    def __str__(self): return str('<' + str(self.name) + ',' + str(self.age) + ',' + str(self.zipcode) + '>')

    def getName(self): return self.name
    
    def getAge(self): return self.age

    def getZipcode(self): return self.zipcode

    def __repr__(self): print(str('testClass\(' + str(self.getName) +','+ str(self.getAge) + ',' + str(self.getZipcode)))