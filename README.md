# project10.py
# My Python projects 🐍
This project contains several simple Python classes created to practice object-oriented programming (OOP) concepts. Each clas has its own attributes and methods, which are detailed below.

---

## Classes

### 1. `dinosaur` Class (File: `test4.py`)

#### Description
This class models a dinosaur with basic attributes and behaviors.

#### Attributes
- `age`: Age of the dinosaur (integer)
- `weight`: Weight of the dinosaur (integer)
- `color`: Color of the dinosaur (string)

#### Methods
- `eat()`: The dinosaur eats and increases its weight by 10 units, printing a message.
- `sleep()`: The dinosaur sleeps and prints a message.

#### Example Usage
```python
dino = dinosaur(30, 400, "gray")
dino.eat()
dino.sleep()
```
## Output
```
دایناسور gray داره غذا میخوره! اوم نوم نوم🦖
وزن جدید دایناسور: 410
دایناسور gray داره میخوابه... خروپف خروپف😴

```

## 2. akhond Class(File:test3.py)
### Description
This class models a cleric with humorous and religious behaviors.

### Attributes
- age: Age (integer)
- ammame_color: Turban color (string)
- height: Height (integer)
- name: Name (string)

### Methods
- roze( ): The cleric fasts and says a prayer.
- speak( ): The cleric gives a short speech.
- eat( ): The cleric breaks their fast and enjoys food.
- doa( ): The cleric says a prayer.
- filter( ): The cleric "filters" modern things(e.g., instagram) with a humorous twist.

### Example Usage
```
makarem = akhond(78, "white", 167, "naser")
safii = akhond(65, "black", 170, "safii")
makarem.roze()
makarem.speak()
safii.doa()
```
### Output
```
حاج اقا ناصر  داره روزه می گیره🛕
خدایا اگه امروز به  افطار برسونم فردا دو برابر  روزه میگیرم!
:حاج اقا ناصر داره سخنرانهی میکنه 📢
مارو دور نندازید
حاج اقا صفایی دعا میکنه:🤲📿
خدایا جیب های مارو پر بگردان!
```

## 3. car Class(file:test2.py)
### Description
this class models a car with basic attributes and behaviors.
### Attributes
- color: Car color (string)
- wheels_count: Number of wheels (integer, default 4)
- max_speed: Maximum speed (integer)
- company: Manufacturing company (string)
### Methods
- turn_on( ): Turns the car on and prints a message.
- turn_off( ): Turns the car off and prints a message.
- boooogh( ): The car honks and prints a message.
### Example Usage
```
my_service = car("yellow", 120, "benz")
my_car_1 = car("blue", 200, "saipa")
my_car_2 = car("white", 220, "iran khodro")
my_car_1.turn_on()
my_service.boooogh()
my_car_2.turn_off()
```
### Output
```
ماشینblue از شرکت saipa روشن شد🚗!
ویژژژ... موتور داره گرم میشه!
ماشین yellow بوق زد!📢
ماشین white از شرکت iran khodro خاموش شد!🛑
موتور خنک شد...
```
### Note
For proper Persian output in Cloud Code, set the encoding to UTF-8:
- Add at the tep of the file: # -*- coding: utf-8 -*-
- Add in code:
sys.stdout.reconfigure(encode='utf-8')

## 4.person Class(File:test.py)
### Description
This class models a person with everyday attributes and behaviors.
### Attributes
- name: Name(string)
- age: Age(integer)
- height: Height(integer)
- city: City(string)
- country: Country(string, default"Iran")
- eye_color: Eye color(string)
- spouse: Spouse(string, default None)
- child: Child(string, default None)
- food: Food(string, default None)
### Methods
- sleep(): The person sleeps and prints a message.,
- walk(): The person walks and prints a message.
- marry(name1, name2): The person marries and sets a spouse and child.
- programming(): The person programs and prints a message.
- study(): The person studies and prints a message.
- eat(): The person eats(if food is specified) and prints a message.
- travel(new_city): The person travels to a new city and updates their city.
### Example Usage
```
my_friend = person("ali", 30, 190, "mashhad", "brown")
my_friend.food = "kabab"
my_sister = person("sara", 20, 170, "tehran", "black")
my_sister.food = "makaroni"
my_boss.food = "ghorme sabzi"
my_friend.eat()
my_sister.marry("jafar", "maryam")
my_friend.travel("tabriz")
```
### Output
```
علی داره کباب میخوره!🍽
سارا با جعفر  ازدواج کرد و مریم به عنوان بچه اومد!💍
علی به تبریز سفر کرد!✈
```
## 5. Person Class(file: tempCodeRunnerFile.py)
### Description
This is a simpler version of the Person class from test.py, with similar methods.
### Attributes
- name: Name(string, default"mamad")
- age: Age(integer, default 31)
- height: Heigh(integer, default 180)
- city: City(string, default"semnan")
- eye_color: Eye color(string, default"blue")
- food: Food(string, default None)
- spouse: Spouse(string, default None)
### Methods
- sleep(): The person sleeps and prints a message.
- walk(): The person walks and prints a message.
- marry(): Checks if the person is married and prints a message.
- study(): The person studies and prints a message.
- eat(): The person eats(if food is specified) and prints a message.
### Example Usage
```
my_friend = person("ali", 25, 175, "tehran", "green")
my_friend.food = "pitza"
my_sister = person("sara", 22, 165, "shiraz", "brown")
my_sister.food = "makaroni"
my_boss = person("ahmad", 40, 185, "mashhad", "black")
my_boss.food = "ghorme sabzi"
my_friend.eat()
my_sister.eat()
my_boss.eat()
```
### Output
```
علی داره پیتزا میخوره🍽
سارا داره ماکارونی میخوره🍝
احمد داره قرمه سبزی میخوره🍽
```
### Note
A TypeError occurred when calling eat() due to an extra
argument. This was fixed by ensuring eat() is called without
arguments(e.g., my_friend.eat() instead of
my_friend.eat("pitza")).

## How to Run
1. Install Python 3.
2. Run each file individually (e.g., python test4.py).
3. If Persian output is not displayed correctly in Cloud Code, set the encoding to UTF-8(see the car class note).
## Tools
. Editor: Cloud Code
. System: Windows (HP Laptop)
## Date
These projrcts were created and completed as of **June 5, 2025**.

**Author**: [Yousef damqani] 
