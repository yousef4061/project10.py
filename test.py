class Person:
    def __init__(self, n, a, h, c, e):
        # properties
        self.name = n
        self.age = a
        self.height = h
        self.city = c
        self.country = "iran"
        self.eye_color = e
        self.spouse = None
        self.child = None
        self.food = None

    # methods
    def sleep(self):
        print(f"{self.name} داره میخوابه...😴")

    def walk(self):
        print(f"{self.name} داره راه میره!🚶")

    def marry(self, name1, name2):
        self.spouse = name1
        self.child = name2
        print(f"{self.name} با {name1} ازدواج کرد و  {name2} به عنوان بچه اومد!💍")
    
    def programming(self):
        print(f"{self.name} داره برنامه نویسی میکنه💻!")

    def study(self):
        print(f"{self.name} داره درس میخونه📚")
    
    def eat(self):
        if self.food:
            print(f"{self.name} داره {self.food} میخوره🍽!")
        else:
            print(f"{self.name} هنوز غذایی انتخاب نکرده😕!")

    def travel(self, new_city):
        self.city = new_city
        print(f"{self.name} به {new_city} سفر کرد✈!")

my_friend = Person("ali", 30, 190, "mashhad", "brown")
my_friend.food = "kabob"
my_sister = Person("sara", 20, 170, "tehran", "black")
my_sister.food = "makaroni"
my_boss = Person("ahmad", 37, 183, "mashhad", "black")
my_boss.food = "ghorme sabzi"

print(my_friend.name) 
print(my_friend.city)

my_friend.eat()
my_sister.eat()
my_boss.eat()

my_friend.programming()
my_boss.programming()

print(my_sister.name)
my_sister.marry("mamad", "jafar")
print(my_sister.spouse)
print(my_sister.child)

print(my_friend.city)
my_friend.travel("tabriz")
print(my_friend.city)
