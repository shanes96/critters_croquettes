from datetime import date
from zoneinfo import available_timezones

class Donkey:
    def __init__(self ,name , species , shift):
        self.name= name
        self.species= species
        self.shift = shift
        self.date_added= date.today()
        self.walking= True
        self.petting_area= True
doug = Donkey("Doug", "donkey" , "midday")
print(f'{doug.name} the {doug.species} is available to pet during the {doug.shift} shift.')
