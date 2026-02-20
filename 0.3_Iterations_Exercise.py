"""
author: Dmytrylo
date: 2026/02/15
0.3 - Repetition Review Exercises
"""

# Task 1: Write a program to calculate the factorial of any number that the user enters using a loop. Ex. 5! = 5*4*3*2*1 = 120
# Your code goes here
x = int(input("Enter value: "))
fact = 1

if x == 0:
    print(1)
else:
    for i in range(1, x + 1):
        fact = fact * i
        print(fact)

if x == 0:
    print(1)
# Task 2a: Write a program that asks for five marks and computes the average, rounded to 1 decimal place.
# Your code goes here
n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))
n4 = int(input("Enter number 4: "))
n5 = int(input("Enter number 5: "))

marks = [n1, n2, n3, n4, n5]
total = sum(marks)
avg = total / 5

print(f"{avg:.1f}")


# 2b)  Modify the program from task 2a to also output the lowest and highest mark WITHOUT lists.
# Your code goes here
n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))
n4 = int(input("Enter number 4: "))
n5 = int(input("Enter number 5: "))

avg = (n1 + n2 + n3 + n4 + n5) / 5

highest = max(n1, n2, n3, n4, n5)
lowest = min(n1, n2, n3, n4, n5)

print(f"Average: {avg:.1f}")
print(f"Highest Mark: {highest}")
print(f"Lowest Mark: {lowest}")


# 2c)  Modify the program from task 2b to check if the mark entered is between 0 and 100. Keep asking user for input until they give a valid grade.
# Your code goes here
total = 0
highest = 0
lowest = 100

for i in range(1, 6):
    mark = int(input(f"Enter mark {i} (0-100): "))

    while mark < 0 or mark > 100:
        print("Invalid input. Mark must be between 0 and 100")
        mark = int(input(f"Enter mark {i}: "))

    total = total + mark

    if mark > highest:
        highest = mark
    if mark < lowest:
        lowest = mark

avg = total / 5

print(f"Average: {avg:.1f}")
print(f"Highest Mark: {highest}")
print(f"Lowest Mark: {lowest}")


# 2d)  Modify the program to ask the user to enter -1 when done entering marks.
# Your code goes here
total = 0
count = 0
highest = 0
lowest = 100

mark = int(input("Enter mark (-1 to stop): "))

while mark != -1:
    if 0 <= mark <= 100:
        total = total + mark
        count = count + 1

        if mark > highest:
            highest = mark
        if mark < lowest:
            lowest = mark
    else:
        print("Invalid number")

    mark = int(input("Enter mark (-1 to stop): "))

if count > 0:
    avg = total / count
    print(f"Average: {avg:.1f}")
    print(f"Highest Mark: {highest}")
    print(f"Lowest Mark: {lowest}")
else:
    print("No entered marks")


# Task 3a) Determine the largest of n positive integers entered the user.
# The program should loop until a negative value is read (aka, use Sentinel Value).
# Your code goes here
largest = -1
print("Enter positive integers. Enter a negative number to stop")

value = int(input("Enter value: "))

while value >= 0:
    if value > largest:
        largest = value
    value = int(input("Enter value: "))

if largest >= 0:
    print(f"The largest number entered was: {largest}")
else:
    print("No positive numbers were entered")


# 3b) Modify the program to find the two largest integers.
# Your code goes here
largest = -1
second_largest = -1

print("Enter positive integers. Enter a negative number to stop")

value = int(input("Enter value: "))

while value >= 0:
    if value > largest:
        second_largest = largest
        largest = value
    elif value > second_largest:
        second_largest = value

    value = int(input("Enter value: "))

if largest != -1:
    print(f"The largest number was: {largest}")
    if second_largest != -1:
        print(f"The second largest number was: {second_largest}")
    else:
        print("Only one number was entered")
else:
    print("No positive numbers were entered")


# Task 4) Use the random module to choose a number between 1 and 100.
# Then print all the factors of that number.
# Ask the user if they wish to play again – loop until the user enters “No” (sentinel value).
# Your code goes here
import random

play_again = "yes"

while play_again.lower() == "yes":
    rand_num = random.randint(1, 100)
    print(f"The randomizer chose number: {rand_num}")
    print(f"The factors of {rand_num} are:")

    for i in range(1, rand_num + 1):
        if rand_num % i == 0:
            print(i)

    play_again = input("Would you like to play again? (Yes/No): ")

print("See you later!")


# Task 5) One useful technique when analyzing a number is to use a loop and the modulus operator to extract each digit 
# from the end.
# Consider this code:

num = int(input("Enter a positive integer: "))

while (num >= 1):
    digit = num % 10
    num = num // 10
    print(digit)

# Use this above code to do the following:
# Count the number of sevens in a positive integer.

num = int(input("Enter a positive integer: "))

count_seven = 0

while num >= 1:
    digit = num % 10
    if digit == 7:
        count_seven = count_seven + 1
    num = num // 10

print(f"Number of sevens: {count_seven}")

# Count the number of odd digits, and the number of even digits, in a positive integer.

num = int(input("Enter a positive integer: "))

odd_count = 0
even_count = 0

while num >= 1:
    digit = num % 10

    if digit % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

    num = num // 10

print(f"Number of odd digits: {odd_count}")
print(f"Number of even digits: {even_count}")