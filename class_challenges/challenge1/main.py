# OOP multiple methods + constructor challenge
class Archer:
    # constructor
    def __init__(self, name, health, num_arrows):
        self.name = name
        self.health = health
        self.num_arrows = num_arrows

    # method 1
    def get_shot(self):
        if self.health > 0:
            self.health -= 1
        if self.health == 0:
             raise Exception(f"{self.name} is dead")
    
    # method 2
    def shoot(self, target):
        if self.num_arrows == 0:
            raise Exception(f"{self.name} can't shoot")
        else:
            self.num_arrows -= 1
            print(f"{self.name} shoots {target.name}")
           
        # simulate target getting shot
        target.get_shot()
    
    # don't touch below this line

    def get_status(self):
        return self.name, self.health, self.num_arrows

    def print_status(self):
        print(f"{self.name} has {self.health} health and {self.num_arrows} arrows")
