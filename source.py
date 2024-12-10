import random

number = "1234567890"
letter = "abcdifghigklmnopqrstuvwxyz"
symbols = "!@#$%^&*()№;:?+="
all = number + letter + symbols
password = "".join(random.sample(all, 10))
print("Password Generated -" ,password)
input()
