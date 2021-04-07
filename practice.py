# Task 1
# Let us say your expense for every month are listed below,
#     January - 2200
#     February - 2350
#     March - 2600
#     April - 2130
#     May - 2190

# Create a list to store these monthly expenses and using that find out,

# 1. In Feb, how many dollars you spent extra compare to January?
# expenses_list=[2200,2350,2600,2130,2190]
# print(expenses_list[1]-expenses_list[0])

# 2. Find out your total expense in first quarter (first three months) of the year.

# expenses_list=[2200,2350,2600,2130,2190]

# total=0
# for i in range(len(expenses_list)-1):
#     total=total+expenses_list[i]
# print(f"total={total}")    

# 3. Find out if you spent exactly 2000 dollars in any month
# expenses_list=[2200,2350,2600,2130,2190,2000]
# for i in expenses_list:
#     if i==2000:
#         print("yes")

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# expenses_list=[2200,2350,2600,2130,2190,2000]
# expenses_list.append(1980)
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

# expenses_list=[2200,2350,2600,2130,2190,2000]

#expenses_list.insert(3,2130+200)

# print(expenses_list)

# solution Task 1


# Task 2
# You have a list of your favourite marvel super heros.

# heros=['spider man','thor','hulk','iron man','captain america']

# Using this find out,

# 1. Length of the list

# Task 2 Solution 
# heros=['spider man','thor','hulk','iron man','captain america']

# print(len(heros))

# 2. Add 'black panther' at the end of this list

# heros.append('black panther')

# print(heros)


# 3. You realize that you need to add 'black panther' after 'hulk',
#     so remove it from the list first and then add it after 'hulk'

# heros.remove('black panther')
# print(heros)

# heros.insert(3,"black panther")
# print(heros)


# 4. Now you don't like thor and hulk because they get angry easily :)
#     So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#     Do that with one line of code.

# for i in heros:
#     if i=="hulk":
#         heros.remove(i)
#     if i=="thor":
#         heros.remove(i)
#     if i=="iron man":
#         print(i)
# print(heros)


# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

# heros.sort()
# print(heros)



# Task 3
# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function


# odd_numbers=[]
# num=int(input("enter number:"))
# for i in range(1,num+1,2):
#     odd_numbers.append(i)
# for i in odd_numbers:
#     print(i)


# password=input("enter password: ")
# number=1
# set_password="abcd1234"
# while  number==1:
#     if password==set_password:
#         print("successful !")
#         break
#     else:
#         print("invalid password !")
#         password=input("enter again:")


# password=input("enter password: ")
# while password !="abcd1234":
#     print("invalid password")
#     password=input("enter password again: ")
# print("successful !")



# choice='y'
# while choice=='y':
#     num1=int(input("enter first number:"))
#     num2=int(input("enter second number:"))

#     print("1.sum")
#     print("2.different")
#     print("3.product")
#     print("4.division")

#     op=int(input("enter operator:"))

#     if op==1:
#         sum=num1+num2
#         print(f"sum of {num1} and {num2} is {sum}")
#     elif op==2:
#         diff=num1-num2
#         print(f"sum of {num1} and {num2} is {diff}")
#     elif op==3:
#         prod=num1*num2
#         print(f"sum of {num1} and {num2} is {prod}")

#     elif op==4:
#         div=num1/num2
#         print(f"sum of {num1} and {num2} is {div}")
#     choice=input("want to continue (y/n):")

# namelist=["ram","shayam","geeta"]

# for i in namelist:
#     print(i.capitalize())


# res=map(lambda n:n.title(),namelist)
# print(list(res))

# email=["1-gmail.com","2-gmail.com"]

# res=map(lambda name:name.replace("-","@"),email)

# print(list(res))

# a=[1,2,3,4,5,6,7,8,9,10]

# evenlist=filter(lambda n:n%2==0,a)
# print(evenlist)
# print(list(evenlist))

# email=["1@gmail.com","2@gmail.com","3@hotmail.com","4@yahoo.com"]
# newemail=filter(lambda email:email.endswith("gmail.com"),email)
# print(list(newemail))