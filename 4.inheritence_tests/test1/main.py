class Human:
    def __init__(self):
        self.name = "aadil"

    def get_name(self):
        return self.__name


## don't touch above this line


class Archer(Human):
    def __init__(self, num_arrows):
        super().__init__()
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows


human = Archer(3)
# has direct access to 
print(human.name)
