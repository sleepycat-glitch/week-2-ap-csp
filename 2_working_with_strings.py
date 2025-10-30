
# ----------------------------------------
# . Working with Strings
# ----------------------------------------

# Strings are sequences of characters enclosed in quotes (' ' or " ")
greeting = "Hello" # string data tpye
name = "World" # string data type

# ----------------------------------------
# Basic String Operations
# ----------------------------------------

# 1. Concatenation: Combining strings using the + operator
message = greeting + " " + name
print("Concatenated String:", message)  # Output: Hello World

# ----------------------------------------
# 2. String Functions
# ----------------------------------------

phrase = "Python is FUN!"
name = "Ayelen"
phrase2 = "SUPERCAGEFRAGISLISTCIOUS"
# # Convert all characters to lowercase
print("Lowercase:", phrase.lower())  # Output: python is fun!
print("Name Lowercase:", name.lower())
print("Phrase2 Lowercase:", phrase2.lower())
# () = method, required for code to function

# # Convert all characters to uppercase
print("Uppercase:", phrase.upper())  # Output: PYTHON IS FUN!
print("Uppercase:", phrase.upper()) 
print("Name Uppercase:", name.upper())
print("Phrase2 Uppercase:", phrase2.upper())
# # Check if all characters are uppercase
print("Is Uppercase?", phrase.isupper())  # Output: False
print("Is Uppercase?", name.isupper())
print("Is Upper?", phrase2.isupper() )


# # Find the length of the string
# print("Length of phrase:", len(phrase))  # Output: 14
phrase = "We hold these truths to be self-evident, that all men are created equal, that they are endowed, by their Creator, with certain unalienable rights, that among these are life, liberty, and the pursuit of happiness."
print(len(phrase))

# # ----------------------------------------
# # 3. Indexing and Slicing
# # ----------------------------------------

# # Indexing: Access characters by position (0-based index)
# print("First character:", phrase[0])  # Output: P
# print("Last character:", phrase[-1])  # Output: !
chicago_mayor = "Johnson"
# first character = 0
# last character = -1
print(chicago_mayor[0])
print(chicago_mayor[-1])
print(chicago_mayor[-3])

# # Slicing: Get a range of characters (start inclusive, end exclusive)
# print("Characters 1 to 4:", phrase[1:4])  # Output: yth

# # Example combining everything:
# print("Formatted Example:", (greeting + " " + name + "!").upper())
# # Output: HELLO WORLD!
print(chicago_mayor[4:])
#first number in slicing is including the character
#second number is excluding the character
print(chicago_mayor[0:4])
print(chicago_mayor[1:5])
#when we get one character, it's called string indexing
#when we get a string of characters, it's called string slicing

# phrase2 = "SUPERCAGEFRAGISLISTCIOUS"
phrase3 = "supercagefragislistcious"
print(phrase.upper())
cut = phrase3[0:5]
print(cut)
# # ----------------------------------------
# # 7. Strings: Advanced Concepts
# # ----------------------------------------

# # Creating Strings: use single or double quotes
# greeting1 = 'Hello'
# greeting2 = "Hi there"

# # Printing Strings
# print(greeting1)
# print(greeting2)

# # ----------------------------------------
# # String Methods
# # ----------------------------------------

sentence = "Python is fun to learn"

# # .split(): Splits the string into a list of words
words = sentence.split()
print("Split result:", words)
words2 = words.join()
print(words2)

# # .format(): Allows inserting values into strings using {}
# name = "Marvin"
# age = 35
# intro = "My name is {} and I am {} years old.".format(name, age)
# print(intro)

# # You can also use f-strings (Python 3.6+)
# intro_fstring = f"My name is {name} and I am {age} years old."
# print(intro_fstring)
