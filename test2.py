class car:
    def __init__(self, c, m, co):
        self.color = c
        self.wheels_count = 4
        self.max_speed = m
        self.company = co

    def turn_on(self):
        print(f"ماشین {self.color} از شرکت {self.company} روشن شد!🚗")
        print("ویژژژ...! موتور داره گرم میشه")

    def turn_off(self):
        print(f"ماشین {self.color} از شرکت {self.company} خاموش شد!🛑")
        print("...موتور خنک شد!")

    def boooogh(self):
        print(f"ماشین {self.color} بوق زد!📢")
        print("بوووووووووق!")




my_service = car("yellow", 120, "benz")
my_car_1 = car("blue", 200, "saipa")
my_car_2 = car("white", 220, "iran khodro")



print(my_car_1.color)
print(my_car_2.company)

my_service.boooogh()


my_car_1.turn_on()
my_car_2.turn_off()
my_service.turn_on()
