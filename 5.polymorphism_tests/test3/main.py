class Sword:
    def __init__(self, sword_type):
        self.sword_type = sword_type

    def __add__(self, other):
        if self.sword_type == "bronze" and other.sword_type == "bronze":
            return Sword("iron")
        elif self.sword_type == "iron" and other.sword_type == "iron":
            return Sword("steel")
        raise Exception("cannot craft")

sword_type_one = Sword("iron")
sword_type_two = Sword("iron")

result = sword_type_one + sword_type_two 
print(result)

# testing operator overloads
