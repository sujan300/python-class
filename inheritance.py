# child class "IS A" parent class

# class Person:
#     def __init__(self,name,contact):
#         self.name=name
#         self.contact=contact
#     def walk(self):
#         print(f"{self.name} is walking.")

# class Student(Person):
#     def __init__(self,name,contact):
#         super().__init__(name,contact)
# class Teacher(Person):
#     def __init__(self,name,contact):
#         super().__init__(name,contact)

# st=Student("Ram","9808187044")
# st.walk()
# t=Teacher("shyam","989875221")
# t.walk()


class Brid:
    def __init__(self,name):
        self.name=name
    def fly(self):
        print(f"{self.name} flying")
class Pigeon(Brid):
    def __init__(self,name):
        super().__init__(name)

class Ostrich(Brid):
    def __init__(self,name):
        super().__init__(name)
    def fly(self):
        print(f"{self.name} could not fly.")
P=Pigeon("Sujan")
P.fly()

O=Ostrich("sabin kc")
O.fly()

class Hummingbrid(Brid):
    def __init__(self,name):
        super().__init__(name)
    def fly(self):
        super().fly()
        print(f"{self.name} fly backward")
# H=Hummingbrid("Suraj")
# H.fly()



