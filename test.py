# mail=["1.gmail.com","2.gmail","3.hotmail","4.yahoou.com","5.email.com"]
# rec=filter(lambda n:n.endswith("gmail.com"),mail)
# print(list(rec))


# email=["gmail.com","gmail.com","gmail.com","gmail.com","gmail.com"]
# rec=map(lambda gmail:gmail.replace("g","e"),email)
# rec=map(lambda smail:smail.replace(".","@"),email)
# # print(list(rec))
# print(rec)

# from module import area_of_rectangle,name,perimeter_of_rectangle 
# from module import *

# from module import area_of_rectangle as area,name,perimeter_of_rectangle as perimeter #alias name

# # print(name)
# print(area(20,10))

# print(perimeter(20,10))


# if __name__ == '__main__':
#     n = int(input("enter data: ").strip())
# #     print(f"the data you entered in n:{n}")
# n=int('a'/'a')
# print(n)

n=int(input("enter number:"))

for i in range(n):
    print(i,end="")