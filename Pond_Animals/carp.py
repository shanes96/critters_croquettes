from datetime import date

class Carp:
    def __init__(self , name , species):
        self.name= name,
        self.species= species,
        self.date_added= date.today()
        self.swimming= True
        self.pond= True

carol = Carp("Carol", "fish")