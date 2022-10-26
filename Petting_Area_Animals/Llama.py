from datetime import date

class Llama:
    def __init__(self , name , species , shift):
        self.name= name
        self.species= species
        self.shift = shift
        self.date_added= date.today()
        self.walking= True
        self.petting_area= True
        
frank = Llama("Frank", "llama" , "midday")
print(f'{frank.name} the {frank.species} is available to pet during the {frank.shift} shift.')