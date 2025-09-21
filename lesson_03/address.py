class Address:
    def __init__(self, indeks, town, street, house, flat):
        self.indeks = indeks
        self.town = town
        self.street = street
        self.house = house
        self.flat = flat

    def __str__(self):
        return f"{self.indeks} {self.town}, {self.street}, \
        {self.house}, {self.flat}"
