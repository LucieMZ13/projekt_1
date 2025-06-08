"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Lucie Mrázková
email: llmrazkova@gmail.com
"""
import string

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]
registered_user_1 = {"username" : "bob", "password" : "123"}
registered_user_2 = {"username" : "ann", "password" : "pass123"}
registered_user_3 = {"username" : "mike", "password" : "password123"}
registered_user_4 = {"username" : "liz", "password" : "pass123"}
all_users = dict()
all_users["user_1"] = registered_user_1
all_users["user_2"] = registered_user_2
all_users["user_3"] = registered_user_3
all_users["user_4"] = registered_user_4

separator = "-" * 40
titlecase_words = 0
uppercase_words = 0
lowercase_words = 0
numeric_strings = list()
sum_of_numbers = 0
number_of_texts = len(TEXTS)



username = input("username")
password = input("password")

is_registered = False
for user in all_users.values():
    if user["username"] == username and user["password"] == password:
        is_registered = True
        break

print(separator)

if is_registered:
    print("Welcome to the app,", username)
else:
    print("Unregistered user, terminating the program..")
    quit()

print("We have", number_of_texts, "texts to be analyzed.")
print(separator)

text_choice = input(f"Enter a number between 1 and {number_of_texts} to select:")
if int(text_choice) > number_of_texts:
    print("This text does not exist, terminating the program.")
    quit()
chosen_text = TEXTS[int(text_choice)-1]
chosen_text_split = chosen_text.split()
chosen_text_plain = [word.strip(string.punctuation) for word in chosen_text_split]
print(separator)

for word in chosen_text_plain:
    if word.istitle():
        titlecase_words +=1
    elif word.isupper():
        uppercase_words +=1
    elif word.islower():
        lowercase_words +=1
    elif word.isnumeric():
        numeric_strings.append(word)
    else:
        continue

for word in chosen_text_plain:
    if word.isnumeric():
        sum_of_numbers += int(word)
    else:
        continue

print("There are", len(chosen_text_plain), "words in the selected text.")
print("There are", titlecase_words, "titlecase words.")
print("There are", uppercase_words, "uppercase words.")
print("There are", lowercase_words, "lowercase words.")
print("There are", len(numeric_strings), "numeric strings.")
print("The sum of all the numbers is", sum_of_numbers)
print(separator)
print(f"{"LEN":>4}|{"OCCURENCES".center(20)}|{"NR.":<3}")
print(separator)

length_of_word = [len(word) for word in chosen_text_plain]
for length in range(1, max(length_of_word)+1):
    occurrence = length_of_word.count(length)
    if occurrence > 0:
        print(f"{length:>3} | {("*" * occurrence).ljust(18)} | {occurrence:<3}")


