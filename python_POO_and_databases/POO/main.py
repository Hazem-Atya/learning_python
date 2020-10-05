class Person:
    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("I am constructed")

    def changeAge(self, age):
        self.age = age
        print("The age is now:", self.age)

    def show(self):
        print("Name:", self.name, "\nAge:", self.age)

    def __del__(self):
        print(self.name, "is destructed")


print("Hello")

p = Person("Safa Atya", 18)
p.name = "Hazem Atya"
p.changeAge(21)
Person.changeAge(p, 22)
p.show()
p = 2
# if we don't change the value of p , it will be
# destructed at the end of program
print("Bye")
