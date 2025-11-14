
# ----------------------------------------
# Print Practice Exercises
# ----------------------------------------

# Print Practice #1
# Write Python code that prints the sentence: I love learning Python
print("I love learning Python")


# Print Practice #2
# Write Python code that prints the sentence: Learning with 'TOTAL Python' is super fun!
print("Learning with 'TOTAL Python' is super fun!")


# Print Practice #3
# Write Python code that prints the number 555 to the screen as a result of a mathematical expression
print(500 + 55)

##############################################################################################################
# Find 3 objects around the room and create variables from it,
# Insert those variables into an f-string sentence(look at slide 22)in repl.it
object1 = "clock"
object2 = "computer"
object3 = "phone"
print(f"The {object1}, {object2}, and {object3} should all display 9:00 a.m.")


# Familiarize yourself with the syntax of the print() function.
# Print your name.
# Print today's date.
# Print the name of your favorite movie.
name = "Vanessa"
date = "November 3 2025"
favorite_movie = "Harry Potter"
print(f"Hello! My name is {name}. Today is {date} and I am going to be watching my favorite movie, {favorite_movie}.")


# Print your name and age on separate lines using a single print() function.
# Use f-strings to print a message like: "In 10 years, [Your Name] will be [Your Age + 10] years old."
name1 = "Ayelen Cardenas"
age1 = 17
print(f"In 10 years, {name1} will be {age1 + 10} years old.")

name2 = "Vanessa Rodriguez"
age2 = 17
print(f"In 10 years, {name2} will be {age2 + 10} years old.")


##############################################################################################################

###########################String Practice##################################
#syntax is the way we write code
# print("Hello World")
# name = "John"
#in other languages, this is different
# in javascript for example, you define
#variables with let or const or var
#in python, you just give your variables a
#name and then define it with a value

phrase = "Hello World"
name3 = "John"



#challenge
# find a summary of the movie blue beetle online and create a 
# variable called blue_beetle_summary and print it it out to the screen

# print the length of the summary vr
# upper case the entire summary vr
# print the summary ac
# print the summary in lowercase ac
# replace the word blue with red vr
# print the summary vr
# string index the word beetle and print it out ac
# print the last word of the summary ac
# print the summary in reverse ac
title = "Blue Beetle"
blue_beetle_summary = "Jaime Reyes suddenly finds himself in possession of an ancient relic of alien biotechnology called the Scarab. When the Scarab chooses Jaime to be its symbiotic host, he's bestowed with an incredible suit of armor that's capable of extraordinary and unpredictable powers, forever changing his destiny as he becomes the superhero Blue Beetle."

print(len(blue_beetle_summary))
print("Uppercase:",blue_beetle_summary.upper())
print("Lowercase:",blue_beetle_summary.lower())

original_string = "Jaime Reyes suddenly finds himself in possession of an ancient relic of alien biotechnology called the Scarab. When the Scarab chooses Jaime to be its symbiotic host, he's bestowed with an incredible suit of armor that's capable of extraordinary and unpredictable powers, forever changing his destiny as he becomes the superhero Blue Beetle."
new_string = original_string.replace("blue", "red")

print(new_string)

print(title[5:])
print(blue_beetle_summary[-7:-1])
blue_beetle_summary_reverse = blue_beetle_summary[::-1]
print(blue_beetle_summary_reverse)
      



##########################input practice#############################################
#input is when we ask the user for input/data
# Ask the user to enter their name.

# Input Practice #1
# Write Python code that allows the user to enter their answer, by making them the following question:
# What are you learning today?
# Your code must be able to print to the screen whatever is entered by the user (use the print function).
user_response = input("What are you learning today?: ")
print(user_response)


# Input Practice #2
# Write Python code that allows the user to enter their answer, by making them the following question:
# Where are you from?
# Your code must be able to print to the screen whatever is entered by the user (use the print function).
user_response1 = input("Where are you from?: ")

print(user_response1)
# Input Practice #3
# Write Python code that displays the user's full name on the screen, by allowing them to enter their first and last name with the following instructions:
# What is your name?
# What is your surname?
# The code must be able to print the user's first and last name on the screen, separated by a space.
first_name = input("What is your first name?: ")
last_name = input("What is your surname?: ")
print(f"{first_name} {last_name}")


# Exercise:
# Write a program that asks the user for their name and favorite color, then prints a message using both pieces of information.

name = input("What is your name?: ")
color = input("What is your favorite color?: ")
print(f"{name}'s favorite color is {color}.")





