from datetime import date

class Pony:
    def __init__(self , name , species , shift):
        self.name= name
        self.species= species
        self.shift = shift
        self.date_added= date.today()
        self.walking= True
        self.petting_area= True

pete = Pony("Pete", "pony" , "morning")
print(f'{pete.name} the {pete.species} is available to pet during the {pete.shift} shift')