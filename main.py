class Gun:
    def __init__(self, name):
        self.name = name

    def __str__(self, name):
        self.name = name

class Machinegun(Gun):
    def pewpew(self):
        print(f"Machine gun {self} goes *brrrrrt*")

    def reload(self):
        print(f"Machine gun {self} reloads *clunk-chink*")


