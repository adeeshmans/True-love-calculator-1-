print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_name = name1 + name2

# converting to lower case input value
lower_case = combined_name.lower()

#counting each occurance of true love with the input
t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")

true = t + r + u + e

l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")

love = l + o + v + e

true_love_score = int(str(true) + str(love))

print(true_love_score)

#logic
if (true_love_score < 10) or (true_love_score > 90) :
    print(f"Your score is {true_love_score}, you go together like coke and mentos.")
elif (true_love_score >= 40) and (true_love_score <= 50):
    print(f"Your score is {true_love_score}, you are alright together.")
else:
    print(f"Your score is {true_love_score}")

