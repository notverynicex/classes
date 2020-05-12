class Gun:
    def __init__(self, model):
        self.model = model

    def __str__(self):
        return self.model
####
class Machinegun(Gun):
    def pewpew(self):
        print(f"Machine gun {self.model} goes *brrrrrt*")

    def reload(self):
        print(f"Machine gun {self.model} reloads *clunk-chink*")
####
class Pistol(Gun):
    def pewpew(self):
        print(f"Pistol {self.model} goes *pew pew*")

    def reload(self):
        print(f"Pistol {self.model} reloads *click click*")
####
browning = Machinegun("Browning M2")
glock = Pistol("Glock 19")
my_guns = [browning, glock]
####
for g in my_guns:
    print(g)
    g.pewpew()
    g.reload()