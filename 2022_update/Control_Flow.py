# # if
# if 10 > 5:
#     print("Correct!")
# # 10
# if 10 < 5:
#     print("Correct!")
# # "=="
# if 10 == 10:
#     print("Correct!")
# a = "nico"
# if a == "nico":
#     print("True!")

# # Else & Elif
# # Else
# password_correct = False
# if password_correct:
#     print("Here is your money")
# else:
#     print("Wrong password")
# Winner = 10
# if Winner > 10:
#     print("Winner is greater than 10")
# elif Winner < 10:
#     print("Winner is less than 10")
# else:
#     print("Winner is 10")

# # Recap
# winner = 5

# if winner < 10:
#     print("If")
# else:
#     print("Else")

# # And & Or
# age = int(input("How old are you?"))

# if age < 18:
#     print("You can't drink")
# elif age > 18 and age < 36:
#     print("You drink beer!")
# else:
#     print("Go ahead")

# from random import randint

# user_choice = int(input("Choose number."))
# pc_choice = randint(1, 50)

# if user_choice == pc_choice:
#     print("You won!")
# elif user_choice > pc_choice:
#     print("Lower!")
# elif user_choice < pc_choice:
#     print("Higher!")

# # While
# distance = 0

# while distance <= 20:
#     print("I'm running:", distance, "km")
#     distance = distance + 1

# # while Python Casino
# from random import randint

# print("Welcome to python casino")
# pc_choice = randint(1,50)
# playing = True

# while playing:
#     user_choice = int(input("Choose number: "))
#     if user_choice == pc_choice:
#         print("You won!")
#         playing = False
#     elif user_choice > pc_choice:
#         print("Lower!")
#     elif user_choice < pc_choice:
#         print("Higher!")

