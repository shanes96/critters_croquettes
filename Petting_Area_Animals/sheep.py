from datetime import date

class Sheep:
    def __init__(self , name , species , shift):
        self.name= name
        self.species= species
        self.shift = shift
        self.date_added= date.today()
        self.walking= True
        self.petting_area= True

sally = Sheep("Sally", "sheep" , "morning")
print(f'{sally.name} the {sally.species} is available during the {sally.shift} shift.')