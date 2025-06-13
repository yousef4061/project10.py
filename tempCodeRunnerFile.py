class Person:
    # properties
    def __init__(self, n="mammd", a=31, h=180, c="semnan", e="blue"):
        self.name = n
        self.age = a
        self.height = h
        self.city = c
        self.eye_color = e
        self.food = None
    # methods
    def sleep(self):
        print(f"{self.name} داره میخوابه 😴")

    def walk(self):
        print(f"{self.name}  داره راه میره 🚶‍♂️")

    def marry(self):
        if not hasattr(self, 'spouse') or self.spouse is None:
            print(f"{self.name} هنوز ازدواج نکرده💔")
        else:
            print(f"{self.name} با {self.spouse} ازدواج کرده💍")
    
    def programming(self):
        print(f"{self.name} داره برنامه نویسی میکنه💻")

    def study(self):
        print(f"{self.name} داره درس میخونه📚!")
    
    def eat(self, food=None):
        if food:
            self.food = food
        if self.food:
            print(f"{self.name} داره {self.food} میخوره 🍽")
        else:
            print(f"{self.name} هنوز غذایی انتخاب نکرده🙁!")


my_friend = Person("ali", 25, 175, "tehran", "green")
my_friend.food = "pitza"
my_sister = Person("sara", 22, 165, "shiraz", "brown")
my_sister.food = "makaroni"
my_boss = Person("ahmad", 40, 185, "mashhad", "black")
my_boss.food = "ghorme sabzi"


print(my_friend.name) 
print(my_friend.city)
my_friend.eat("pitza")
my_sister.eat("makaroni")
my_boss.eat("ghorme sabzi")

