'''Write a Python program that prompts the user to enter his/her full name 
(without any spaces) and then creates a secret password consisting of three letters 
(in lowercase) randomly picked up from his/her full name, and a random four-digit number. 
For example, if the user enters "JackClary", 
a secret password can probably be one of "jcs1578" or "yka8832" or "awu1250".'''

import random
def password_generator():
    name = input("Enter your name:")
    name=name.replace(" ", "").lower()
    part1=random.choices(name, k=3)
    part1=part1[0]+part1[1]+part1[2]
    part2=random.choice(range(1000, 9999))
    password=part1+str(part2)
    print(password, name)
password_generator()