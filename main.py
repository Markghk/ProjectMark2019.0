class Pets:
    group = "cats"
    gender = "male"
    breed = "Maine Coon"

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color


cat1 = Pets(name="Snow", age=5, color="white")
cat2 = Pets(name="Barsik", age=3, color="orange")
cat3 = Pets(name="Grey", age=6, color="grey")


class Pets2:
    group = "cats"
    gender = "female"
    breed = "British Shorthair"

    def __init__(self, name1, age1, color1):
        self.name = name1
        self.age = age1
        self.color = color1


catt1 = Pets2(name1="Chloe", age1=1, color1="white with grey")
catt2 = Pets2(name1="Peach", age1=2, color1="orange with black and brown")
catt3 = Pets2(name1="Coal", age1=7, color1="black")
