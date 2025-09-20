# Base Class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand   # attribute
        self.model = model   # attribute
        self.storage = storage   # attribute
    
    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")
    
    def phone_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB")

# Child Class (Inheritance)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, gpu):
        super().__init__(brand, model, storage)  # inherit attributes
        self.gpu = gpu   # new attribute
    
    def play_game(self, game):
        print(f"{self.brand} {self.model} with {self.gpu} GPU is playing {game}")

# Objects (Instantiation)
phone1 = Smartphone("Apple", "iPhone 15", 256)
phone2 = GamingPhone("Asus", "ROG Phone 7", 512, "Adreno 740")

# Method calls
phone1.phone_info()
phone1.call("123-456-7890")

print("------")

phone2.phone_info()
phone2.call("987-654-3210")
phone2.play_game("Call of Duty Mobile")
