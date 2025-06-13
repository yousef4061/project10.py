class akhond:

    def __init__(self, age, ac, h, n):
        self.age = age
        self.ammame_color = ac
        self.height = h
        self.name = n


    def roze(self):
        print(f"{self.name} حاج اقا داره روزه میگیره.🛕")
        print("خدایا اگه امروز به افطار برسونم فردا دو برابر روزه میگیرم!")

    def speak(self):
        print(f"{self.name} حاج اقا داره سخنرانی میکنه📢")
        print("ای مردم مارو دور نندازید")
      
    def eat(self):
        print(f"{self.name} حاج اقا داره افطار میکنه🍽")
        print("به به! عجب چایی و خرمای خوشمزه ای داشتم میمردم از گرسنگی🥴")

    def doa(self):
        print(f"{self.name} حاج اقا داره دعا میکنه🤲!")
        print("خدایا  جیب های مارو پر بگردان!")

    def filter(self):
        print(f"{self.name} حاج اقا  داره فیلتر میکنه🚫")
        print("اینستاگرام؟ نه بابا فقط اسلام!")

makarem = akhond(70, "white", 167, "naser")
# sistani = akhond()
safi = akhond(65, "black", 170, "safi")


print(makarem.name)
print(makarem.age)
makarem.age += 1
print(makarem.age)


makarem.roze()
makarem.speak()
makarem.eat()
makarem.doa()
makarem.filter()


print(safi.name)
safi.speak()
safi.doa()
