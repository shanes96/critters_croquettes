from datetime import date

class Sheep:
    def __init__(self , name , species):
        self.name= name,
        self.species= species,
        self.date_added= date.today()
        self.walking= True
        self.petting_area= True

sally = Sheep("Sally", "sheep")