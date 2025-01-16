# learning about methods part 1
# here we created fortify method which is called and mutates the armor attribute
class Wall:
    armor = 10
    height = 5

    def fortify(self):
        self.armor = self.armor * 2
        return self.armor


armor_one = Wall()
armor_one.fortify()
print(armor_one.armor)
