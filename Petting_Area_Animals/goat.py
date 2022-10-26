from datetime import date

class Goat:
    def __init__(self , name , species , shift):
        self.name= name
        self.species= species
        self.shift = shift
        self.date_added= date.today()
        self.walking= True
        self.petting_area= True
garry = Goat("Garry", "goat" , "morning")
print(f'{garry.name} the {garry.species} is available to pet during the {garry.shift}')