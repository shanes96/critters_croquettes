from datetime import date

class Pony:
    def __init__(self , name , species):
        self.name= name,
        self.species= species,
        self.date_added= date.today()
        self.walking= True
        self.petting_area= True

pete = Pony("Pete", "pony")