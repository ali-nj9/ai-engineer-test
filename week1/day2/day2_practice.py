# print("------step1------")

# a = 15
# b = 7

# print(a > b)
# print(a == b)
# print(a > 10 and b < 10)
# print(a < 5 or b > 5)
# print(not a == 15)


# print("------step2------")

# for a in range(1, 11):
#     print(a)

# print("-------")

# for b in range(2, 21, 2):
#     print(b)

# print("-------")

# kol = 0
# for c in range(1, 101):
#     kol = kol + c
# print(kol)

# print("-------")

# for d in range(1, 6):
#     print((str(d) + "") * d)


# print("------step3------")

# command = ""

# while command != "quit":
#     command = input("chi dastor midi aziz : ")
#     if command == "quit":
#         print("Goodbye!")
#     else:
#         print(command.upper())


# print("------step4------")
# print("part1")
# for H in range(1, 11):
#     if H == 6:
#         break
#     print(H)

# print("part2")
# for K in range(1, 11):
#     if K == 4 or K == 7:
#         continue
#     print(K)


# print("------step5------")
# for S in range(1, 6):
#     for r in range(S):
#         print("*", end="")
#     print()


# print("------step6------")

# for s in range(1, 6):
#     for l in range(s):
#         print("*", end="")
#     print()

# for s2 in range(4, 0, -1):
#     for L2 in range(s2):
#         print("*", end="")
#     print()


# print("------exercise1------")

# score = int(input("Enter your score : "))

# if 0 > score or score > 100:
#     print("Invalid score.")
# elif score >= 90:
#     print("Excellent")
# elif 80 <= score:
#     print("Good")
# elif 70 <= score:
#     print("Average")
# elif 60 <= score:
#     print("Acceptable")
# elif 60 > score:
#     print("Fail")


# print("------exercise2------")
# number = int(input("type your number : "))

# if number <= 1:
#     print("Not prime")
# else:
#     is_prime = True

#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print("prime")
#     else:
#         print("Not prime")


# print("------exercise3------")

# number = int(input("enter your number : "))

# if number < 0:
#     print("Invalid input")
# else:
#     result = 1

#     while number > 1:
#         result = result * number
#         number = number - 1

#     print(result)


# print("------exercise4------")

# n = int(input("enter your number : "))
# if n <= 0:
#     print("Invalid input")
# else:
#     a = 0
#     b = 1

#     for i in range(n):
#         print(a)
#         a, b = b, a + b


# import random

# print("------exercise5_step1------")
# secret_number = random.randint(1, 100)
# print(secret_number)


# import random

# print("------exercise5_step2,3,4,5------")
# secret_number = random.randint(1, 100)
# guess = int(input("hads bezan : "))
# attempts = 1

# while guess != secret_number:
#     if guess > secret_number:
#         print("Too high")
#     else:
#         print("Too low")

#     guess = int(input("try again : "))
#     attempts += 1

# print("Correct")
# print(f"You found it in {attempts} attempts")


# print("------exercise6_step1,2------")


# for row in range(1, 11):
#     for col in range(1, 11):
#         print(f"{row * col:4}", end="")
#     print()


# print("------exercise7------")

# for i in range(1, 6):
#     for s in range(i):
#         print("*", end="")
#     print()

# for t in range(4, 0, -1):
#     for g in range(t):
#         print("*", end="")
#     print()


# print("------exercise8------")

# password = input("enter your password : ")

# special_chars = "!@#$%^&*"


# has_digit = False
# has_upper = False
# has_special = False

# for char in password:

#     if char.isdigit():
#         has_digit = True

#     if char.isupper():
#         has_upper = True

#     if char in special_chars:
#         has_special = True

# if len(password) < 8:
#     print("Password must be at least 8 characters.")

# if not has_digit:
#     print("Password must contain at least 1 digit.")

# if not has_upper:
#     print("Password must contain at least 1 uppercase letter.")

# if not has_special:
#     print("Password must contain at least 1 special character.")

# if len(password) >= 8 and has_digit and has_upper and has_special:
#     print("Strong password.")


# print("------exercise9------")

# balance = 5000000

# Enter_key = ""

# # print(f"you chose : {Enter_key}")
# while Enter_key != "4":
#     print("1. Show balance")
#     print("2. Deposit")
#     print("3. Withdraw")
#     print("4. Exit")

#     Enter_key = input("ye mored az mavared bala ro vared kon : ")

#     if Enter_key == "1":
#         print(f"Your balance is: {balance}")
#     elif Enter_key == "2":
#         print("Deposit selected.")
#         ask_2 = float(input("mablagh ra vared konid : "))
#         if ask_2 <= 0:
#             print("khata : mablagh nabayad manfi bashad")
#         else:
#             balance += ask_2
#             print(f"Deposited successfully. New balance: {balance}")
#     elif Enter_key == "3":
#         print("Withdraw selected.")
#         ask_3 = float(input("mablagh ra vared konid : "))
#         if ask_3 <= 0:
#             print("khata : mablagh nabayad manfi bashad")
#         elif ask_3 > balance:
#             print("Insufficient funds.")
#         else:
#             balance -= ask_3
#             print(f"Withdrawal successful. New balance: {balance}")
#     elif Enter_key == "4":
#         print("Goodbye!")
#     else:
#         print("Invalid option.")


# print("------exercise10------")

# email = input("type your email : ")

# is_valid = True

# if email == "":
#     print("1. خالی نباشد")
#     is_valid = False

# if " " in email:
#     print("2. فاصله نداشته باشد")
#     is_valid = False

# if not "@" in email:
#     print("3. @ داشته باشد")
#     is_valid = False

# if "@" in email:
#     parts = email.split("@")

#     local_part = parts[0]
#     domain_part = parts[1]

#     if local_part == "":
#         print("4. قبل از @ حداقل 1 کاراکتر داشته باشد")
#         is_valid = False

#     if "." not in domain_part:
#         print("5. بعد از @ یک . داشته باشد")
#         is_valid = False

#     if "." in domain_part:
#         domain_parts = domain_part.split(".")
#         extension = domain_parts[-1]

#         if len(extension) < 2:
#             print("6. بعد از آخرین . حداقل 2 کاراکتر داشته باشد")
#             is_valid = False

# if is_valid:
#     print("Valid email.")
