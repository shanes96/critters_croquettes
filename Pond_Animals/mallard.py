from datetime import date

class Mallard:
    def __init__(self , name , species):
        self.name= name,
        self.species= species,
        self.date_added= date.today()
        self.swimming= True
        self.pond= True

maggie= Mallard("Maggie", "fish")

# mallardclass= Mallard()
# print(mallardclass.name)