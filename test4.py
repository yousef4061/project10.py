
class dinosaur:
    def __init__(self, age, weight, color):
        self.age = age
        self.weight = weight
        self.color = color

    def eat(self):
        print("دایناسور {self.color} 🐊داره غذا میخوره! اوم نوم نوم")
        self.weight += 10
        print(f"وزن جدید دایناسور: {self.weight}")

    def sleep(self):
        print(f"دایناسور {self.color} خروپف خروپف داره میخوابه...😴")

dino = dinosaur(30, 400, "gray")
dino.eat()
dino.sleep()
    
