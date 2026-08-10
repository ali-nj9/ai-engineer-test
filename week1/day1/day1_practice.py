# name = "ali"
# age = 23
# height = 1.78
# is_student = False


# print(name)
# print(age)
# print(height)
# print(is_student)

# print("----")

# print(type(name))
# print(type(age))
# print(type(height))
# print(type(is_student))


# print("------step2-------")

# current_year = 2026

# name = input("enter your name : ")
# age = int(input("Enter your age : "))

# birth_year = current_year - age

# print(f"سلام {name} , تو {age} سالته و حدودا سال {birth_year} به دنیا اومدی.")

# print(type(name))
# print(type(age))
# print(type(birth_year))


# /////////////////////////////////////////////////
# text = "  hello   "

# print(text.strip())
# print(text.title())
# print(len(text))

# text1 = "learning python is fun"
# words = text1.split()
# print(words)

# word = "programming"
# print(word[::-1])

# messy_text = "   leaRning pyThon is Fun   "

# clean_text = messy_text.strip().title()
# print(clean_text)

# print(len(clean_text))

# words = clean_text.split()
# print(words[0])
# print(words[-1])
# print(words)

# word = "Programming"
# print(word[::-1])


# text = "   pyThon IS very POWERful and useful   "

# clean_text = text.strip().title()

# print(clean_text.upper())
# print(clean_text.lower())
# print(len(clean_text))

# word = clean_text.split()
# print(len(word))
# print(word[0])
# print(word[-1])
# print(word[1])
# print(word)
# print(clean_text[::-1])


# text = "   pyThon IS very POWERful and useful   "
# clean_text = text.strip().title()
# words = clean_text.split()
# print(words[1])
# print(words[0:2])
# print(words[-2:])
# print(words[0][0])
# print(words[-1][-1])


# print("------step4------")

# sentence = input("Enter a sentence : ")
# clean_sentence = sentence.strip()
# words = clean_sentence.split()

# if not clean_sentence:
#     print("Sentence is empty.")
# else:
#     print(clean_sentence)
#     print(len(clean_sentence))
#     print(len(words))
#     print(words[0])
#     print(words[-1])
#     print(clean_sentence.upper())
#     print(clean_sentence.lower())
#     print(clean_sentence[::-1])

# age = int(input("Enter age : "))
# temperature = float(input("Enter temperature : "))


# print("------step5.1.2.3.4------")

# print("Available options:")
# print("c_to_f = Celsius to Fahrenheit")
# print("f_to_c = Fahrenheit to Celsius")

# choice = (
#     input(
#         "Enter c_to_f for Celsius to Fahrenheit or f_to_c for Fahrenheit to Celsius: "
#     )
#     .strip()
#     .lower()
# )

# print(choice)

# if choice == "c_to_f":
#     print("You chose Celsius to Fahrenheit")
#     temperature = float(input("You entered °C : "))
#     print(f"you Entered {temperature} °C")
#      result = (temperature * 9 / 5) + 32
#     print(f"{temperature} °C = {result:.2f} °F")
# elif choice == "f_to_c":
#     print("You chose Fahrenheit to Celsius")
#     temperature = float(input("You entered °F : "))
#     print(f"you entered {temperature} °F")
#     result = (temperature - 32) * 5 / 9
#     print(f"{temperature} °F ={result:.2f} °C")
# else:
#     print("Invalid choice. Please enter c_to_f or f_to_c.")


# name = input("write your name : ")
# words = name.split()
# print(words)  برای دیباگ کردن خوبه ولی معمولا برای نسخه نهایی حذفش میکنیم
# clean_name = " ".join(words).title()
# print(clean_name)
# no_space_name = clean_name.replace(" ", "")
# print(len(no_space_name))


# weight = float(input("give me your weight : "))
# height = float(input("give me your height : "))

# BMI = weight / (height**2)
# print(f"Your BMI is {BMI:.2f}")


# if BMI < 18.5:
#     category = "Underweight"
# elif 18.5 <= BMI < 25:
#     category = "Normal"
# elif 25 <= BMI < 30:
#     category = "Overweight"
# else:
#     category = "Obese"

# print(f"Category : {category}")


# number_1 = float(input("type your first number : "))
# number_2 = float(input("type your second number : "))

# amaliyat = input(
#     "ye mored ra vared konid   جمع +    تفریق -   *   ضرب   /   تقسیم    **  توان   %   باقی‌مانده  :"
# )


# if amaliyat == "+":
#     result = number_1 + number_2
#     print(f"{number_1} + {number_2} = {result}")
# elif amaliyat == "-":
#     result = number_1 - number_2
#     print(f"{number_1} - {number_2} = {result}")
# elif amaliyat == "*":
#     result = number_1 * number_2
#     print(f"{number_1} * {number_2} = {result}")
# elif amaliyat == "/":
#     if number_2 == 0:
#         print("Error: Division by zero is not allowed.")
#     else:
#         result = number_1 / number_2
#         print(f"{number_1} / {number_2} = {result}")
# elif amaliyat == "**":
#     result = number_1**number_2
#     print(f"{number_1} ** {number_2} = {result}")
# elif amaliyat == "%":
#     if number_2 == 0:
#         print("Error: Division by zero is not allowed.")
#     else:
#         result = number_1 % number_2
#         print(f"{number_1} % {number_2} = {result}")
# else:
#     print("khata :  az gozine ha ye dade shode bayad stefade konid")


# print("Available point : ")
# print(
#     "km_to_mi  = کیلومتر به مایل , kg_to_lb  = کیلوگرم به پوند , l_to_gal  = لیتر به گالن"
# )

# tabdil = input("yeki az mavared bala ke namayesh dade shode ro vared kon : ")

# if tabdil == "km_to_mi":
#     km = float(input("km ra vared konid : "))
#     result = km * 0.621371
#     print(f"{km} km = {result :.2f} mile ast")
# elif tabdil == "kg_to_lb":
#     kg = float(input("kg ra vared konid : "))
#     result = kg * 2.20462
#     print(f"{kg} kg = {result :.2f} pound ast")
# elif tabdil == "l_to_gal":
#     liter = float(input("liter ra vared konid : "))
#     result = liter * 0.264172
#     print(f"{liter} liter = {result :.2f} galun ast")
# else:
#     print("kahata : vorodi na mo tabar ast")


# principal = float(input("mablagh avalye ra vared konid : "))
# rate = float(input("adad nerkh sod salane mad nazar ra vared konid %  : ")) / 100
# years = int(input("adad sal mad nazar ra vared konid : "))

# print(f"principal : {principal :.2f}")
# print(f"Rate : {rate  * 100}%")
# print(f"Years : {years}")

# Simple_profit = principal * rate * years
# Total_Simple = principal + Simple_profit


# Total_Compound = principal * (1 + rate) ** years
# Compound_profit = Total_Compound - principal

# print(f"Simple profit : {Simple_profit :.2f}")
# print(f"Total Simple : {Total_Simple :.2f}")
# print("---")
# print(f"Total_Compound : {Total_Compound :.2f}")
# print(f"Compoundprofit : {Compound_profit :.2f}")
