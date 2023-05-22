import random

class Lotteri:
    
    def __init__(self):
        self.list_vinster = [
        "Solstol",
        "Röd Porche",
        "Handduk",
        "Ockelbo 500",
        "10 liter tvål",
        "BMX cykel",
        "Surf Bräda ",
        "Burton Snowboard"
        "Kawasaki KLX 230 Cross"
        "ett paket Bregott",
        "Hawai resa",
        "en biltvätt på OK",
        "Kaffe och bulle",
        "Lyx yatch",
        "Iphone",
        "JBL hörlurar",
        "Makitat skruvdragare",
        "parfume från Hugo Boss",
        "konsertbiljett till The Killers",
        "ett kilo kattmat",
        "ett marsvin"
        ]

    def get_vinst(self):
        slumptal = random.randint(0, 19)
        return self.list_vinster[slumptal]
        