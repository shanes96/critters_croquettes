from datetime import date

class Goat:
    def __init__(self , name , species):
        self.name= name,
        self.species= species,
        self.date_added= date.today()
        self.walking= True
        self.petting_area= True
garry = Goat("Garry", "goat")