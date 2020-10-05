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
        print("type:", type(self))
        print("Name:", self.name, "\nAge:", self.age)

    def __del__(self):
        print(self.name, "is destructed")


class Professor(Person):
    subject = ""

    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def show(self):
        super().show()
        print("subject:", self.subject)


e1 = Professor("Sana Hamdi", 36, "POO")
# print("name", e.name)
# print("age", e.age)
# print("subject", e.subject)
# e1.show()

t = [Professor("Aymen Sellaouti", 38, "WEB"), e1, Person("Sihem labbene <3", 21)]
for item in t:
    item.show()
