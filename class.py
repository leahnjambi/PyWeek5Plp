# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery_life = battery_life

    def call(self, number):
        print(f"Calling {number} from {self.model}...")

    def browse(self):
        print(f"Browsing the internet on {self.model}.")

# Derived class: GamingSmartphone
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, cooling_system):
        super().__init__(brand, model, storage, battery_life)
        self.cooling_system = cooling_system

    def game(self, game_name):
        print(f"Playing {game_name} on {self.model} with {self.cooling_system} cooling system.")


        # Create a regular smartphone
phone = Smartphone("Samsung", "Galaxy S23", "256GB", "20 hours")
phone.call("+2547456789")
phone.browse()

# Create a gaming smartphone
gaming_phone = GamingSmartphone("Asus", "ROG Phone 7", "512GB", "16 hours", "Advanced Vapor Chamber")
gaming_phone.game("PUBG Mobile")
gaming_phone.call("+2547654321")

