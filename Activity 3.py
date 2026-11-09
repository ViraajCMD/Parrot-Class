class Parrot:

    species = "Bird"


    def __init__(self, name, age):
        self.name = name
        self.age = age



blu = Parrot("Blu",10)
Woo = Parrot("Woo",15)

print("Blu is {}".format(blu.species))
print("Woo is also a {}".format(Woo.species))

print("\n{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(Woo.name, Woo.age))