# PART 1
# without method (function declared outside class)
class Soldier:
    health = 5

soldier_one = Soldier()
soldier_health = soldier_one.health

def take_damage(health, damage):
    health -= damage
    return health
    
soldier_one_health = take_damage(soldier_health, 2)
print(soldier_one_health)
# health prints 3 (only health argument becomes 3 not health attribute)
print(soldier_one.health)
# health attribute stays 5

# PART 2
# with method (function declared in class)
class Soldier:
    health = 5

    def take_damage(self, damage):
        self.health -= damage

soldier_one = Soldier()
soldier_one.take_damage(2)
print(soldier_one.health)
# prints "3"
