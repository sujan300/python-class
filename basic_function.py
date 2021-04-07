# def func_name():
    # function name
    # code or instruction


# def demo():
#     print("this is demo function")

# demo()



# def welcome(first_name,last_name):
#     print("welcome", first_name , last_name)


# welcome("ram",'adhikari')
# welcome('shyam','kc')
# welcome('hari','khanal')


# def display_profile(name,address,contact,country='Nepal'):
#     print("Name =",name)
#     print("Address =",address)
#     print("Conctact=",contact)
#     print("Country=",country)

# display_profile('sujan adhikari','ktm',9808174011)
# print("-----------------------------------------")
# display_profile(name='sabin kc',address='gorkha',contact=9845674021,country='china')



# def add(num1,num2):
#     total=num1+num2
#     return total
# res=add(10,8)
# print(res)


# def add(num1,num2):
#     total=num1+num2
#     print('tootal=',total)
# res=add(10,8)
# print('resut=',res)


# def add(num1,num2):
#     total=num


# def defference(num1,num2):
#     if(num1>num2):
#         d=num1-num2
#         print('different=',d)
#     else:
#         d2=num2-num1
#         print('different=',d2)

# defference(10,1)

# def product(num1,num2):
#     total=num1*num2
#     print('product=',total)
# product(10,8)

# def calculator(num1,num2,op):
#     if op=='add':
#         return num1+num2
#     elif op=='product':
#         return num1*num2
        
#     elif op=='different':
#         return num1-num2
        

# res=calculator(1,2,'add')
# print('result=',res)


# a="apple"
# a.capitalize()

# print(a)


# email="sujanadhikari.com@gmail.com"
# userinput="Sujanadhikari.com@gmail.com"

# print(email==userinput)

# print(email==userinput.casefold())


# print(email.center())


# sen ="Welcome Program"
# print(sen.center(50))
# print()
# print(sen.center(50,'*'))


# fruit="papaya"
# print(fruit.count("a"))
# print()
# print(fruit.count("p"))
# print()
# print(fruit.count('y'))


# email="ram@gmail.com"
# print(email.endswith("gmail.com"))

# strip()
# email=' sujan.com'
# print(email.strip())


# phone="+9808187044+"
# print(phone.strip("+"))
# first_name="_sujan adhikari"
# print(first_name.strip("_"))


# split
# a="sujan-Gorkha-98722-85584"
# print(a.split("-",2))


# repla
# a="pythan"
# a=a.replace("a","o")
# print(a)


# b=a.replace("p","b")
# print(b)


# partition 

# a="ram@gmail.com"
# b=a.split("@")
# a=a.partition("@")

# print(a)
# print(b)


# name="sujan-ktm-9808187044"

# newname=name.split("-")
# print(newname)

# new2name=name.partition("-")
# print(new2name)


# f-string 

# a=10
# b=20
# c=a+b


# print(f"sum of {b} and {a} is ={c}")



# list


# a=[]

# print(type(a))

# print(a)

# a=[1,2,3,4,5.7,True,None]

# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a[5])
# print(a[6])

# emp_list=['Ram','Shyam','Gita','Hari']
# print(emp_list)
# emp_list.append("Sujan")

# print(emp_list)


# emp_list=['Sujan','Suraj','Sabin','Rabi']

# new_emp_list=emp_list

# new_emp_list.clear()


# print(emp_list)


# emp_list=['Sujan','Suraj','Sabin','Rabi']
# new_emp_list=emp_list.copy()
# emp_list.clear()
# print(new_emp_list)


# employees=["Ram","Shayam","Hari"]

# new_emp=["Saugat","Chetan","Monster"]

# employees.append(new_emp)

# print(employees)


# employees.extend(new_emp)
# print(employees)

# print(new_emp)


# employees=["Ram","Shayam","Hari"]

# print(employees.index("Hari"))

# employees.insert(0,"sabin kc")

# print(employees)


# employees=["Ram","Shayam","Hari"]

# pop_employees=employees.pop(1)

# print(employees)
# print(pop_employees)

# employees.remove("Ram")

# print(employees)


# employees=["Ram","Shayam","Hari"]

# employees.sort()
# print(employees)



# assending order
# employees=["Ram","Shayam","Hari"]

# employees.reverse()

# print(employees)


# dessending order
# employees=["Ram","Shayam","Hari"]
# employees.sort(reverse=True)
# print(employees)

# a=[6,8,7,4,3,2,9]
# b=a[2:5]
# # a.clear()
# print(b)
# print(a)


# print(a[5:2:-1])

# print(a[5:2:-2])


# for loop 
# a_list=["ram","sujan","sabin","suraj"]

# for item in a_list:
#     print(item)

# b_list=[1,2,3,4,5,6,7,8,9,10]

# for a in b_list:
#     print(a)



# for i in range(0,100):
#     print(i)

# for i in range(1,30,2):
#     print(i)


# for a in range(2,50,5):
#     print(a)


# a=[]

# for i in range(10):
#     a.append(int(input("enter number:")))

# b=0
# for i in a:
#     print(i)
#     b=b+i
# print(b)

# a=[]
# num=int(input("enter number:"))
# total=0
# for i in range(10):
#     num=int(input("enter number:"))
#     total=total+num
#     a.append(num)
# print(total)


# Task 1


# for i in range(1,25):
#     if i%3==0:
#         break
#     print(i)

# print("-----------------------------------------------------")
# for i in range(1,25):
#     if i%3==0:
#         continue
#     print(i) 

# while loop 


# Bounded loop
#   which has fixed boundary
#  for loop

# Unbounded loop 
#  no fix boundary 
# while loop

# while <condition>
#     code to repeat 



# choice='y'

# while choice=='y':
#     num1=int(input("enter first number: "))
#     num2=int(input("enter second number: "))
#     sum=num1+num2
#     print(f"Sum of {num1} and {num2} is {sum}")
#     choice=input("want to continue(y/n)?: ")

# tuple 
# a=(1,2,3,4,2,3,4,1,6,1)
# print(a.count(1))
# print(a.count(2))
# print(a.count(3))
# a+=(6,7)
# print(a)

# import sys 

# a=()
# b=[]

# print(sys.getsizeof(a))
# print(sys.getsizeof(b))



# set 

# a={}
# print(type(a))


# b=set()

# print(type(b))

# a={"apple","banana","grapes","apple"}
# print(a)


# nat_foot_play={"ram","sita","hari","sabin"}

# # nat_foot_play.add('sujan')

# # print(nat_foot_play)

# # nat_foot_play.clear()

# # print(nat_foot_play)
# new_foot_play=nat_foot_play.copy()

# # print(new_foot_play)
# nat_foot_play.add('sujan')
# new_foot_play.add("suraj")
# # print(nat_foot_play.difference(new_foot_play))

# print(nat_foot_play.difference_update())


# old_members={"sujan","sabin","ram"}
# new_members={"sujan","sabin","sita"}

# print(new_members.difference_update(old_members))
# print(new_members)


# old_members.discard("sujan")
# print(old_members)

# old_members.remove("sabin")

# print(old_members)

# print(old_members.pop())
# old_members.remove("sujan")
# print(old_members)


# a_list={1,2,3,4,5}
# print(a_list.pop())


# dict


# mappale object

# a={'name':'ram','contact':'9808187044','address':'ktm'}

# print(a)

# a={'name':'ram','contact':9808187044,'address':'ktm'}

# print(a)

# b={1:'one'}
# print(b)

# new_dict={[1,2,3]:'sujan adhikari'}

# print(new_dict)


# profile={'name':'sujan','contact':9808187044,'address':'ktm'}


# p=profile.copy()
# print(p)
# p.clear()
# print(p)


# fromkeys
# p={}
# a=['username','password','email']
# b=p.fromkeys(a,'default_name')
# print(b)


# print(profile.get('name',"sabin"))
# print(profile.get('email',"sujanadhikari.com@gmail.com"))


# for key in profile.keys():
#     print(key)



# for val in profile.values():
#     print(val)

# for key ,val in profile.items():
#     print(key,"=",val)


# print(profile.pop('name'))
# print(profile)

# print(profile.popitem())

# profile.setdefault("email","sujanadhikari.com")

# print(profile)


# profile.update({"sabin":9823808037})

# print(profile)

# def func(*args):
#     print(type(args))
#     print(args)

# func(1,2,3,4,5,'sujan adhikari','python')


# def func(*args,**kwargs):
#     print(args,'\n',kwargs)

# func(1,2,3,4,'python',name='sujan',contact=9808187044)


# def welcome():
#     print("welcome Ram")

# w=welcome # call by reference
# print(w)
# w()


# def welcome(name):
#     print(f'welcome {name}')

# def nameste(name):
#     print(f"nameste {name}")
# def greet(f,name):
#     # f->welcome
#     # f()->welcome()
#     f(name)
# greet(welcome,'Harry')
# greet(nameste,'Ram')

# def main():
#     def inner():
#         print("i am inner function")
#     inner()

# main()


# def main():
#     def inner():
#         print("i am inner function")
#     return inner

# f=main()
# f()
# f()

# def main(n):
#     def addition(a,b):
#         return a+b
#     def substraction(a,b):
#         return a-b
#     if n==1:
#         return addition
#     if n==2:
#         return substraction
# add=main(1)
# sub=main(2)
# num=int(input("enter first number:")
# print(add(10,9))
# print(sub(10,9))

# num =10
# def main():
#     global num
#     num=num+1
#     print(num)
# main()


# alist=[1,2,3,4,5,6]
# def func():
#     alist.append(1000)

# func()
# print(alist)


# a=[1,2,3,4,5]
# b=[]


# num=1
# def main():
#     num=10
#     def inner():
#         # nonlocal num

#         global num
#         num=num+1
#         print(num)
#     inner()
# main()


# closure

# def multiplier(n):
#     def times(a):
#         return a*n
#     return times
# times5=multiplier(5)
# del multiplier
# print(f"total={times5(10)}")

# decorators 
# def decorate_func(func):
#     def wrapper():
#         print(f"func:{func}")
#         print("Nice to see u")
#         func()
#         print("welcome again")
#     return wrapper
# @decorate_func
# def greet():
#     print("welcome home")
# greet()
# print(f"greet:{greet}")


# def smart_division(func):
#     print(f"func:{func}")
#     def wrapper(a,b):
#         if(b==0):
#             return "could not divide by zero"
#         else:
#             return func(a,b)
#     return wrapper


# @smart_division
# def division(num1,num2):
#     return num1/num2
# print(division(10,10))
# print(division(10,0))
# print(division)





# def decor(func):
#     def wrapper():
#         print(func())
#     return wrapper

# @decor
# def sujan():
#     print("i am chor")
# print(sujan())



# def smart_division(func):
#     print(f"func:{func}")
#     def wrapper(a,b):
#         if(b==0):
#             return "could not divide by zero"
#         else:
#             return func(a,b)
#     return wrapper


# @smart_division
# def division(num1,num2):
#     return num1/num2
# print(division(10,10))
# print(division(10,0))
# print(division)

# def decor(func):
#     def wrapper(num1,num2):
#         return func()
#     return wrapper
# def sum(a,b):
#     return a+b
# print(sum(10,20))


