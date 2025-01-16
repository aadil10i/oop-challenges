class Soldier:
    def __init__(self, health):
        self.health = health
    
    def take_damage(self, damage):
        self.health -= damage

soldier_one = Soldier()
soldier_one.take_damage(2)
print(soldier_one.health)
