""" char_name = "John"
char_age = "35"
print("There once was a man named " + char_name + ", ")
print("he was 70 years old " + char_age + ".")
print("He really liked the name" + char_name + ", ")
print("but didn't like being " + char_age + ".") """
import random

# def state_toss():
#     heads = 0
#     tails = 0
#     flip = random.randint(0, 1)
#     if (flip == 0):
#         print("Heads")
#         recordList.append("Heads")
#     else:
#         print("Tails")
#         recordList.append("Tails")
#     print(str(recordList))
#     print(str(recordList.count("Heads")) + str(recordList.count("Tails")))


coin = random.randint(0, 1)

if (coin == 0):
    phrase = "Florida"
else:
    phrase = "New York"

if (phrase == "New York"):
    print("STAY OUT")
else:
    print("Come on in")