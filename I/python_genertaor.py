import random
characters = 'abcdefghijklABCHSGAJSHGAKAHSHS216673267'
length = int(input("Enter password length :"))
password = ''
for i in range(length):
    password+=random.choice(characters)
print("Generated password :", password)