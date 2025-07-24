
'''print(0)
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))'''

'''import math
x=math.factorial(3)
print(x)'''

#first its in str 
'''x="6"
print(type(x))
y=int(x)
print(type(y))# its in int'''

'''import turtle
z=turtle.Screen()
z.setup(300,800)'''

'''x=input()
print(type(x))'''# for input

'''x=input()
print(type(int(x)))'''

# perform arthmetic operation
'''x=input()
y=input()
print(x+y)
print(int(x)+int(y))'''

# to convert bin , octal , hex to decimal and virse versa
'''a=int(input("enter number"))
print(bin(a),oct(a),hex(a),sep='\n')'''

'''#for find the max ,min, address
a=[2,3,4,5,6,7,8,9]
print(max(a), min(a),id(a),sep='\n')'''

# use of if else and elif
'''x=int(input("enter a number" ))
if x>0:
 print(x,"is greater than zero")
elif x<0:
 print(x,"is smaller than zero")
else:
 print(x,"is equal to zero")
print("program complete")'''

# use for loop
'''i=int(input("enter a number"))
a=input("enter a string")
for d in a:
 print(d,end='')
for d in range(i):
 print(d)
for d in range(3,i):
 print(d)
for d in range(3,i,2):
 print(d)
print(range(i))'''

# use of while loop
'''i=[2,33,44,55,66,77,88,99,11]
x=0
while x<len(i):
    print(i[x])
    x=x+1'''
'''# some function for list
a=[22,33,44,55,66,77,88,99,11]
a.append(44)
print(a)
print(a.count(a))'''

# function for tuple
'''i=(11,22,33,44)
i.count(22)
print(i)'''
# slicing operator
'''a=[22,33,44,55,66,77,88,99,11]
print(a[2:8:2],a[1::],a[-1::-1])'''

# while-else OR for -else loop
'''p=2345
pin=int(input("enter pin"))
c=0
while c<3:
    c=c+1
    if pin==p:
     print("pin is correct")
     break
    else:
     pin=int(input("enter pin"))
else:
 print("setup")'''

# use of dictionary fun
'''a={"ak":12,"al":"asd","ad":23}
print(a)
for i in a:
  print(i,":",a[i],sep='',end=' ')
b=dict(ak=12,asd="asd",ad=23)
print(b)'''

'''import math
print('Enter the radius')
r=float(input())
print(f'Area={round(math.pi*r*r,2)}cm\u00b2')'''
# use of tenary operator
'''n=int(input())
# print('positive' if (n > 0) else 'negative')
# use of string'''
'''print(help(str))
a=input()
print(a.upper(),a.lower(),a.capitalize(),a.isdigit(),a.isalpha(),a.isalnum,a.find('b'),len(a))'''
# use of indexing
'''a="1234-5678-9012"
print(a[1:8:2])  # output: [2, 4,...
print(a[1::2])  # output: [2, 4, 5,...
print(a[:])# output : [1, 2, 3, 4,...
print(a[::-1])# output : [2,1,0,9
print(a[-4:])#output : [9,0,1,2'''
#use of format specifier
'''a=1234.5678
b=-2356.098
c=678.09
print(f'price is {a:.2f}')#output:price is 1234.57
print(f'{b:.2f}')#output: -2356.10
print (f'{c:.2f}') #output: 678.09

print(f'price is {a:10}')#output:price is  1234.5678
print(f'price is {b:8}')#output:price is -2356.098
print (f'price is {c:9}')#output:price is    678.09

print(f'price is {a:010}')#output:price is 01234.5678
print(f'price is {b:08}')#output:price is -2356.098
print (f'price is {c:09}')#output:price is 000678.09

print(f'price is {a:+}')#output:price is +1234.5678
print(f'price is {b:+}')#output:price is -2356.098
print (f'price is {c:+}')#output:price is +678.09

print(f'price is {a:+,.2f}')#output:price is +1,234.56
print(f'price is {b:+,.2f}')#output:price is -2,356.10
print (f'price is {c:+,.2f}')#output:price is +678.09'''

# use of time method
'''import time

mytime=int(input("Enter time in sec"))

for x in range(mytime,0,-1):
  sec=x%60
  min=int(x/60)%60
  hour=int(x/3600);
  time.sleep(1)
  print(f'{hour:02d}:{min:02d}:{sec:02d}')'''
# use of set,tuple,,list
# list
'''fruits=["apple","banana","orange","mango"]
print(dir(fruits),help(fruits))
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
print(fruits.index('apple'))
fruits.extend('pineapple')
print(fruits)
print(fruits.count('banana'))
fruits.append('guvava')
print(fruits)
fruits.clear()
print(fruits)'''
# set
# fruits.sort() not in set
#fruits.reverse() not in set
#print(fruits.index('apple')) not in set
#print(fruits.count('banana')) not in set
'''fruits={"apple","banana","orange","mango"}
print(dir(fruits),help(fruits))
fruits.add('pineapple')
print(fruits)
fruits.remove('apple')
print(fruits)
fruits.pop()
print(fruits)
fruits.clear()
print(fruits)'''
# tuple
#fruits.add('pineapple') not in tuple
#fruits.remove('apple') not in tuple

#print(dir(fruits),help(fruits))
'''fruits=("apple","banana","orange","mango")
print(fruits.count('banana'))
print ('apple' in fruits)
print(len(fruits))

fruits=["apple","banana","orange","mango","apple"]
set(fruits)
print(fruits)'''
#nums=[1,2,3,4]


# def permuteUnique( nums):
#     """
#     :type nums: List[int]
#     :rtype: List[List[int]]
#     """
#     def backtrack(path, used):
#         if len(path) == len(nums):
#             res.append(path[:])
#             return
#         for i in range(len(nums)):
#             if used[i]:
#                 #print(f'a={i}')
#                 print(f'if={path}')
#                 continue
#             # Skip duplicates
#             if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
#                 continue
#             used[i] = True
#             print(f'b={path}')
#             #print(f'b={i}')
#             path.append(nums[i])
#             #print(nums[i])
#             backtrack(path, used)
#             print(f'pop={path}')
#             path.pop()
            
#             used[i] = False

#     nums.sort()  # Sort to detect duplicates
#     res = []
#     used = [False] * len(nums)
#     backtrack([], used)
#     #print(res)


# permuteUnique( nums)


# use of dictionary
'''dict1={"name":"John","age":30,"city":"New York"}
print(dict1)
dict1.update({"country":"Usa"})
print(dict1)
print(dict1.get("name"))
print(dict1.get("countr"))
print(dict1.keys())
print(dict1.values())
dict1.pop("city")
print(dict1)
dict1.popitem() 
print(dict1)
dict1.clear()'''


# use of random
'''import random 
print(random.randrange(0,12))
a={'apple', 'banana', 'orange', 'mango'}
b=[1,2,3,4,5,6,7,8,9,10]
print(random.choice(list(a)))
random.shuffle(b)
print(b)
print(random.sample(b,3))  # Randomly select 3 elements from b
print(random.random())  # Generate a random float between 0.0 and 1.0

print("\u25CF","\u250C","\u2500","\u2510","\u2502","\u2514","\u2518","\u2502","\u253C","\u252C","\u2534","\u2524","\u251C","\u2524","\u253C","\u251C")  # Unicode characters for various box drawing symbols
 #   ● ┌ ─ ┐ │ └ ┘
"┌────────────────┐"
"│                │"
"│                │"
"│                │"
"│       ●        │"
"│                │"
"│                │"
"│                │"
"└────────────────┘"
dice_art={
  1:( "┌────────────────┐",
      "│                │",
      "│                │",
      "│                │",
      "│       ●        │",
      "│                │",
      "│                │",
      "│                │",
      "└────────────────┘"),
  2:( "┌────────────────┐",
      "│ ●              │",
      "│                │",
      "│                │",
      "│                │",
      "│                │",
      "│                │",
      "│              ● │",
      "└────────────────┘"),
  3:( "┌────────────────┐",
      "│ ●              │",
      "│                │",
      "│                │",
      "│       ●        │",
      "│                │",
      "│                │",
      "│              ● │",
      "└────────────────┘"),
  4:( "┌────────────────┐",
      "│ ●            ● │",
      "│                │",
      "│                │",
      "│                │",
      "│                │",
      "│                │",
      "│ ●            ● │",
      "└────────────────┘"),
  5:( "┌────────────────┐",
      "│ ●            ● │",
      "│                │",
      "│                │",
      "│       ●        │",
      "│                │",
      "│                │",
      "│ ●            ● │",
      "└────────────────┘"),
  6:( "┌────────────────┐",
      "│ ●            ● │",
      "│                │",
      "│                │",
      "│ ●            ● │",
      "│                │",
      "│                │",
      "│ ●            ● │",
      "└────────────────┘")                   
     

  
}

dice=[] 

total=0

n=int(input("Enter the number of dice to roll: "))    
for i in range(n):
    roll = random.randint(1, 6)
    total += roll
    dice.append(roll)
    print(f"Dice {i+1}: {roll}")
    print("\n".join(dice_art[roll]))

print(f"Total: {total}")
for i in range(9):
    for die in dice:
        print(dice_art.get(die)[i])'''
    

# use of function

'''# 1 use of arguments 
#use of positional arguments
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet("Alice", 30)
# use of keyword arguments
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")
greet(age=30, name="Alice")  # Order doesn't matter with keyword arguments
# use of default arguments
def greet(name, age=25):
    print(f"Hello, {name}! You are {age} years old.")
greet("Alice")  # age will default to 25
greet("Bob", 40)  # age is explicitly set to 40
# use of arbitrary arguments
# use of *args
def greet(*names):
    for name in names:
        print(f"Hello, {name}!")
greet("Alice", "Bob", "Charlie")
# use of **kwargs
def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
greet(name="Alice", age=30, occupation="Engineer")
greet(name="Alice", age=30, city="New York")   '''

# use of memebership operator example in and not in
'''a=[1, 2, 3, 4, 5]
b=int(input("Enter a number to check if it's in the list: "))
if b in a:
    print(f"{b} is in the list")
else:
    print(f"{b} is not in the list")
fruits = {"apple", "banana", "orange", "mango", "grape", "kiwi", "pear", "peach", "plum", "cherry"}
fruit_to_check = input("Enter a fruit to check if it's in the set: ")
if fruit_to_check not in fruits:
    print(f"{fruit_to_check} is not in the set")
else:
    print(f"{fruit_to_check} is in the set")'''

# use of list comprehension

'''numbers=[nums for nums in range(1, 11)]
print(numbers)  
squares = [num ** 2 for num in numbers]
print(squares)  
even= [num for num in numbers if num % 2 == 0]
print(even)
odd = [num for num in numbers if num % 2 != 0]
print(odd)
fruits = ["apple", "banana", "orange", "mango", "grape", "kiwi", "pear", "peach", "plum", "cherry"]
fruit_lengths = {fruit.upper() for fruit in fruits}
print(fruit_lengths)'''

# use of match case
'''def get_day_name(day_number):
    match day_number:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day number"

print(get_day_name(3))  
print(get_day_name('Monday'))'''

# use of scope follow rule LEGB meaning first follow Local,then follow Enclosing, then Global, then Built-in
def outer_function():
    x = "outer"

    def inner_function():
        nonlocal x  # Access the variable from the enclosing scope
        x = "inner"
        print("Inner function:", x)

    inner_function()
    print("Outer function:", x)
outer_function()

x= "global"
print("Global variable:", x)




a=5.5
5.5
print(int(a))
























