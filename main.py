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


class Owners:
    group = "students"
    gender = "male"
    age = 13-16

    def __init__(self, name1, age1, gender):
        self.name = name1
        self.age = age1
        self.gender = gender


owner1 = Owners(name1="Bill", age1=13, gender="male")
owner2 = Owners(name1="Jack", age1=16, gender="male")
owner3 = Owners(name1="Peter", age1=14, gender="male")
