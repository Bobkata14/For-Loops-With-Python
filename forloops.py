# Python For Loops

"""
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
"""
from operator import index

# Print each fruit in a fruit list:

fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)

# The for loop does not require an indexing variable to set beforehand.


"""
Looping Through a String
Even strings are iterable objects, they contain a sequence of characters:
"""

# Loop through the letters in the word "banana":

for x in "banana":
    print(x)


"""
The break Statement
With the break statement we can stop the loop before it has looped through all the items:"""

# Exit the loop when x is "banana":

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break


# Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)


"""
The continue Statement
With the continue statement we can stop the current iteration of the loop, and continue with the next:"""

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)


"""
The range() Function
To loop through a set of code a specified number of times, we can use the range() function,

The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number."""

for x in range(6):
    print(x)

# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.

"""
The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter:
range(2, 6), which means values from 2 to 6 (but not including 6):"""

for x in range(2, 6):
    print(x)


"""
The range() function defaults to increment the sequence by 1,
however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):"""

for x in range(2, 30, 3):
    print(x)

"""
Else in For Loop
The else keyword in a for loop specifies a block of code to be executed when the loop is finished:"""

# Print all numbers from 0 to 5, and print a message when the loop has ended:

for x in range(6):
    print(x)
else:
    print("Finally finished!")

# Note: The else block will NOT be executed if the loop is stopped by a break statement.

# Break the loop when x is 3, and see what happens with the else block:

for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")

"""
Nested Loops
A nested loop is a loop inside a loop.

The "inner loop" will be executed one time for each iteration of the "outer loop":"""

# Print each adjective for every fruit:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

"""
The pass Statement
for loops cannot be empty, but if you for some reason have a for loop with no content,
put in the pass statement to avoid getting an error."""

for x in [0, 1, 2]:
    pass


# Code Challenge
"""
Create a list called fruits with: "apple", "banana", "cherry"
Write a for loop that prints each item in fruits
Use break to stop the loop when the item is "banana
"""

fruits = ["apple", "banana", "cherry"]

for x in fruits:
    if x == "banana":
        break
    print(x)


# Exercise 1
names = ["Ivan", "Maria", "Peter", "Georgi", "Anna"]

for name in names:
    print(name)


# Exercise 2
games = ["Minecraft", "GTA V", "Hogwarts Legacy", "CS2", "WWE 2K16"]

for game in games:
    print(f"I like {game}")


# Exercise 3
numbers = [5, 10, 15, 20, 25]

for number in numbers:
    print(number)

for number in numbers:
    print(f"Number: {number}")


# Exercise 4
numbers = [10, 20, 30, 40, 50]
total = 0

for number in numbers:
    total += number
    print(total)


# Exercise 5
numbers = [1, 4, 7, 10, 13, 16, 20]

for number in numbers:
    if number % 2 == 0:
        print(number)


# Exercise 6
numbers = [5, -3, 10, -8, 0, 15, -2]

for number in numbers:
    if number > 0:
        print(f"Positive number: {number}")
    elif number < 0:
        print(f"Negative number: {number}")
    else:
        print(f"Zero: {number}")


# Exercise 7
numbers = [12, 45, 7, 89, 23, 56]
largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(f"Largest number: {largest}")


numbers = [34, 8, 72, 15, 91, 43]
largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(f"Largest number: {largest}")


# Exercise 8
i = 0

for i in range(10):
    i += 1
    print(i)


# Exercise 9
i = 0

for i in range(2, 22, 2):
    print(i)


# Exercise 10
number = (int(input("Enter a number: ")))
i = 0

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
    i += 1


# Exercise 11
word = "programming"
count = 0

for letter in word:
    if letter == "a":
        count += 1
    elif letter == "e":
        count += 1
    elif letter == "i":
        count += 1
    elif letter == "o":
        count += 1
    elif letter == "u":
        count += 1

print(f"Vowels: {count}")


# Exercise 12
grades = [6, 5, 4, 3, 6, 5, 2]

i = 0

count = 0

count_two = 0

for grade in grades:
    i += grade

print(f"Average grade: {i/len(grades)}")

for grade in grades:
    if grade == 6:
        count += 1

print(f"Excellent grade: {count}")

for grade in grades:
    if grade < 4:
        count_two += 1

print(f"Grades below 4: {count_two}")


# Exercise 13
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"]
prices = [1200, 50, 100, 500, 150]

total_price = 0
max_prices = prices[0]
expensive_product = products[0]
count = 0


for index, product in enumerate(products):
    price = prices[index]

    if product == "Laptop":
        if price == 1200:
            total_price += price
            print(f"{product} - {price}")

    elif product == "Mouse":
        if price == 50:
            total_price += price
            print(f"{product} - {price}")

    elif product == "Keyboard":
        if price == 100:
            total_price += price
            print(f"{product} - {price}")

    elif product == "Monitor":
        if price == 500:
            total_price += price
            print(f"{product} - {price}")

    elif product == "Headphones":
        if price == 150:
            total_price += price
            print(f"{product} - {price}\n")

print(f"Total price: {total_price}")

for product, price in zip(products, prices):
    if price > max_prices:
        max_prices = price
        expensive_product = product

print(f"The most expensive product is {expensive_product} with a price of {max_prices}")

for product, price in zip(products, prices):
    if price > 100:
        count += 1

print(f"More than 100: {count}\n")

#Overall - 8.8/10