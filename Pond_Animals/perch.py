from datetime import date

class Perch:
    def __init__(self , name , species):
        self.name= name,
        self.species= species,
        self.date_added= date.today()
        self.swimming= True
        self.pond= True

patrick = Perch("Patrick", "fish")

# perchclass= Perch()
# print(perchclass.name)