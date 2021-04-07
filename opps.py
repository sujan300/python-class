# class and object
# Encapsulation
# Inheritance
# polymorphism
# Abstraction
# Access modifier
# Access and mutator function
# geeter setter


# class laptop:
#     # initializer function(initalizer object)
#     def __init__(self,brand,color, ram):
#         self.brand=brand
#         self.color=color
#         self.ram=ram
#     def power_on(self):
#         print(f"{self.brand} laptop is starting .")
#     def reboot(self):
#         print(f"{self.brand} laptop is rebooting.")
# d=laptop("LENEVO","Black","16 GB")
# l=laptop("DELL","Silver","8 GB")

# # print(d.__dict__)
# d.power_on()
# l.power_on()



# class calculator:
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#     def add(self):
#         return self.num1+self.num2
#     def difference(self):
#         return self.num1-self.num2
#     def product(self):
#         return self.num1*self.num2
#     @staticmethod
#     def sqare_root(num):
#         return num**0.5
# c=calculator(10,20)
# print(f"the sum of two number is: {c.add()}")
# print(f"the difference of two number is: {c.difference()}")
# print(f"the product of two number is: {c.product()}")
# print(c.sqare_root(25))



# class student:
#     college_name="ABC College"
#     def __init__(self,_id,name,contact):
#         self._id=_id
#         self.name=name
#         self.contact=contact
# st=student("001","sujan","9808187044")
# print(st.__dict__)
# print(st.college_name)

# class product:
#     def __init__(self,name,price):
#         self.name=name
#         # self.price=price
#         # name mangaling_classname_attrname
#         self.__price=price

#     # def geter(self):
#     #     return self.__price

#     # def setter(self,price):
#     #     self.__price=price
#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def price(self,price):
#         self.__price=price

# p=product("pant",1600)
# # print(p.__dict__)
# # p.price=0

# # print(p.__dict__)
# # print(p.geter())
# # p.setter(1700)
# # print(p.__dict__)
# # p.price = 1700
# p.setter(17000)
# print(p.geter())
# # print(p.price)


# operator overloading

# class product:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#     def __eq__(self,obj):
#         return self.price==obj.price
#     def __add__(self,obj):
#         return self.price+obj.price
# pant=product("Pant",1600)
# tshirt=product("Tshirt",1600)
# print(pant == tshirt)
# print(pant+tshirt)






