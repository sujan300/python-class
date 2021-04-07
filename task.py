# Exercise: List DataStructure

# Task 1
# Let us say your expense for every month are listed below,
#     January - 2200
#     February - 2350
#     March - 2600
#     April - 2130
#     May - 2190

# Create a list to store these monthly expenses and using that find out,

# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this



# Task 2
# You have a list of your favourite marvel super heros.

# heros=['spider man','thor','hulk','iron man','captain america']

# Using this find out,

# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#     so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#     So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#     Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)



# Task 3
# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function




# a=[
#     {"1":
#         {
#             "name":["Ram","kumar","shrestha"]
#         },
#         "contact":{
#             "home":["9808187044"],
#             "office":["014458505"]
#         }
#     }
# ]

# fullname=a[0].get("1").get("name")
# fullname=" ".join(fullname)
# print(f"your name is {fullname}")

# contact=a[0].get("contact").get("home")
# print(f"your home conctat is {contact[0]}")

# office=a[0].get("contact").get("office")
# print(f"your office contact is {office[0]}")

# 1. Make a program which takes user input and display either user input is leap year or not.
# User input must be 4 digit integer
# example: 2020 is leap year, 2021 is not
# Note: Program should ask for user input till user input is incorrect

# def check_leapyear(year):
#     if year>=1000 and year<=9999:
#         if year % 400 ==0:
#             return "leap year"
#         elif year % 100 == 0:
#             print("not leap year")
#             return "not leap year"
#         elif year % 4 ==0:
#             return "leap year"
#         else:
#             print("not leap year")
#             return "not leap year"
#     else:
#         print("please enter year in 4 digit:")
#         return "not leap year"
# year=check_leapyear(int(input("enter year :")))
# while year=="not leap year":
#     year=check_leapyear(int(input("enter again year: ")))

# if year=="leap year":
#     print(year)


# 2. Take five user input, cast into integer. Print count of all the duplicate numbers.
# # a = [1, 2, 3, 4, 5] => {1:1, 2:1, 3:1, 4:1, 5:1}
# # b = [1, 2, 2, 3, 3] => {1:1, 2:2, 3:2}
# a=[]
# for i in range(5):
#     a.append(int(input("enter data in list: ")))
# b={}
# for i in a:
#     b.update({i:a.count(i)})
# print(b)




# 3. Write a program to calculate simple interest. Take principal, time and rate as user input.

# print("calculate simple intrest")
# time=int(input("enter time: "))
# rate=int(input("enter rate: "))
# principle=int(input("enter principle: "))

# simple_intrest=(time*rate*principle)/100

# print(f"simple intrest is ={simple_intrest}")


# 4. Write a program to calculate Compound Interest and Compound Amount. Take principal, time
# and rate as user input.

# print("calculate compound intrest")
# t=int(input("enter time: "))
# r=int(input("enter rate: "))
# p=int(input("enter principle: "))


# cal=(1+(r/100)**t)

# ci=p*(cal-1)

# print(f"the compound intrest is ={ci}")


# 5. Print the sum of given lists:
# a) [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# b) [1, 2, ‘3’, 4, 5, ‘6’, 7, 8, 9, 10]


# list_a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list_b=[1, 2, '3', 4, 5, '6', 7, 8, 9, 10]

# sum=0
# for i in list_a:
#     sum=sum+i
# print(f"sum of list a): {sum}")
# print()
# sum1=0
# for i in list_b:
#     a=int(i)
#     sum1=sum1+a

# print(f"sum of list a) is={sum1}")


# 6. Suppose, we have given list:
# a = [
# {“username”: “ram@gmail.com”, “last_login”: “157950”},
# {“username”: “ shyam @gmail.com”, “last_login”: “157659”},
# {“username”: “hari@gmail.com”, “last_login”: “157680”},
# {“username”: “krishna@gmail.com”, “last_login”: “157880”}
# ]
# Sort the above given list according to their last_login in ascending order.


# a = [
# {"username": "ram@gmail.com", "last_login": "157950"},
# {"username": " shyam @gmail.com", "last_login": "157659"},
# {"username": "hari@gmail.com", "last_login": "157680"},
# {"username": "krishna@gmail.com", "last_login": "157880"}
# ]


# for i in range(len(a)-1):
#     for j in range(i+1,len(a)):
#         if(int(a[i].get("last_login"))>int(a[j].get("last_login"))):
#             temp=a[i]
#             a[i]=a[j]
#             a[j]=temp
# for i in a:
#     print(i)


# 7. Make a list which contains value from 1 to 1000. (if possible, try to do in one line)
# a=list(range(1,1001))
# print(a)

# users=[
#     {
#         "name":"Ram",
#         "contact":"987654321",
#         "address":"ktm",
#         "friends":[
#             {"name":"Shayam","contact":"987665154","address":"ktm"},
#             {"name":"kirshna","contact":"98765890","address":"Pkr"},
#             {"name":"Hari","contact":"98765154","address":"Bkt"}  
#         ]
#     },
#     {
#         "name":"Shayam",
#         "Contact":"98765154",
#         "address":"ktm",
#         "friends":[
#             {"name":"Ram","contact":"987654321","address":"ktm"},
#             {"name":"Hari","contact":"98765154","address":"Bkt"},        
#         ]
#     },
#     {
#         "name":"Hari",
#         "Contact":"98765154",
#         "address":"ktm",
#         "friends":[
#             {"name":"Hari","contact":"98765154","address":"Bkt"},
#         ]       
#     }
# ]


# Task for question 8:
# Print all friends name, contact and address for user Ram.

# for i in users[0].get("friends"):
#     name=i.get("name")
#     contact=i.get("contact")
#     address=i.get("address")
#     print(f"name: {name} ,contact: {contact} and address: {address}")
# Find out which user have less friends
# def check_friends(data):
#     name=data.get("name")
#     count=0
#     for i in data.get("friends"):
#         count+=1
#     return name,count
# friends= {}
# for i in range(len(users)):
#     a=list(check_friends(users[i]))
#     for j in range(len(a)-1):
#         friends.update({a[j]:a[j+1]})
# if int(friends.get("Ram"))<int(friends.get("Shayam"))<int(friends.get("Hari")):
#     name=friends.get("name")
#     print("Ram has less friends")
# elif int(friends.get("Shayam"))<int(friends.get("Hari")):
#     name=friends.get("Shayam")
#     print("Shayam has less friends")
# else:
#     name=friends.get("Hari")
#     print("Hari has less friends")

# Find out which user have most friend in common.

# a=[]
# for i in users:
#     for j in i.get("friends"):
#         a.append(j.get("name"))


# def common_friend(friends_List):
#     counter=0
#     for i in friends_List:
#         most_common_friends=friends_List.count(i)
#         if(most_common_friends > counter):
#             counter=most_common_friends
#             num=i
#     return num
# print(f"most common friend all of them is: {common_friend(a)}")


# 9. Find out all prime numbers between 1 to 100.
# n=int(input("enter number you want:"))
# for i in range(2,n):
#     count=0
#     for j in range(2,i):
#         if i%j==0:
#             count+=1
#     if count==0:
#         print(f"prime number is: {i}")

# 10. Take 15 user input as integer and print sum of all even numbers and odd numbers separately.
# a=[]
# n=int(input("enter number: "))
# for i in range(n):
#     a.append(int(input("enter 15 number:")))
# sumeven=0
# sumodd=0
# for i in range(len(a)):
#     if a[i]%2==0:
#         sumeven=sumeven+a[i]
#     elif a[i]%2==1:
#         sumodd=sumodd+a[i]
# print(f"the sum of even numbers is :{sumeven}")
# print(f"the sum of odd numbers is :{sumodd}")




