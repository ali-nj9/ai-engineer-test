# print("------day3_step1------")

# fruits = ["apple", "banana", "orange", "mango", "grape"]

# print(fruits)
# print(fruits[0])
# print(fruits[-1])
# print(fruits[0:3])
# print(fruits[-2:])
# print(fruits[::-1])
# print(len(fruits))


# print("------day3_step2------")


# numbers = [5, 2, 8, 1, 9, 3, 7, 4, 6]

# numbers.append(10)
# print(numbers)

# numbers.insert(0, 0)
# print(numbers)

# new_list = numbers.pop(0)
# print(new_list)

# numbers.sort()
# print(numbers)

# numbers.sort(reverse=True)
# print(numbers)


# print(numbers.count(5))

# print(numbers.index(8))


# print("------day3_step3------")

# numbers = [10, 25, 3, 47, 8, 16, 52, 4, 33, 21]

# total = 0

# for num in numbers:
#     total += num

# largest = numbers[0]

# for num in numbers:
#     if num > largest:
#         largest = num

# smallest = numbers[0]

# for num in numbers:
#     if num < smallest:
#         smallest = num

# average = total / len(numbers)

# print(f"Sum: {total}")
# print(f"Largest: {largest}")
# print(f"Smallest: {smallest}")
# print(f"Average: {average}")


# print("------day3_step4------")

# numbers = [64, 34, 25, 12, 22, 11, 90]

# print(f"Before: {numbers}")

# for i in range(len(numbers)):
#     for j in range(len(numbers) - 1):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# print(f"After: {numbers}")


# print("------day3_step5------")

# person = ("Ali", 23, "Tehran", 1.75)

# name, age, city, height = person

# print(f"Name:{name}")
# print(f"Age: {age}")
# print(f"City: {city}")
# print(f"Height: {height}")

# colors = ("red", "green", "blue", "yellow", "purple")

# for i in range(len(colors)):
#     print(colors[i])
# colors[0] = "orange"


# print("------day3_step6------")

# student = {
#     "name": "ALI",
#     "age": 23,
#     "city": "Tehran",
#     "grade": 85,
# }

# print(student["name"])

# print(student.get("grade"))
# print(student.get("phone", "Not found"))

# student["city"] = "Mashhad"
# print(student)

# student["email"] = "ali@gmail.com"
# print(student)

# del student["age"]
# print(student)

# for key, value in student.items():
#     print(f"{key} : {value}")


# print("------day3_step7------")

# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}

# print(a | b)
# print(a & b)
# print(a - b)

# a.add(99)
# print(a)

# b.discard(5)
# print(b)

# my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# print(set(my_list))


# print("------exercise1------")

# numbers = [45, 12, 78, 23, 56, 89, 34, 67, 11, 90]


# largest = numbers[0]

# for num in numbers:
#     if num > largest:
#         largest = num
# print(f"biggest : {largest}")

# smallest = numbers[0]

# for num in numbers:
#     if num < smallest:
#         smallest = num
# print(f"Smallest : {smallest}")

# total = 0

# for num in numbers:
#     total += num
# print(f"Sum : {total}")

# average = total / len(numbers)
# print(f"Average : {average}")


# for i in range(len(numbers)):
#     for j in range(len(numbers) - 1):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# print(f"sorted : {numbers}")


# print("------exercise2------")

# list1 = [1, 2, 3, 4, 5, 6]
# list2 = [4, 5, 6, 7, 8, 9]

# Intersection = []
# for item in list1:
#     if item in list2:
#         Intersection.append(item)

# Union = []
# for item in list1:
#     if item not in Union:
#         Union.append(item)

# for item in list2:
#     if item not in Union:
#         Union.append(item)

# Difference = []
# for item in list1:
#     if item not in list2:
#         Difference.append(item)

# print(f"Intersection: {Intersection}")
# print(f"Union: {Union}")
# print(f"Difference: {Difference}")


# print("------exercise3------")

# students = {"Ali": 85, "Sara": 92, "Reza": 78, "Maryam": 95, "Ahmad": 70}

# total = 0

# for score in students.values():
#     total += score

# average = total / len(students)
# print(average)


# best_name = ""
# best_score = 0

# for name, score in students.items():
#     if score > best_score:
#         best_score = score
#         best_name = name

# print(f"Best student: {best_name} with {best_score}")

# above_80 = []

# for name, score in students.items():
#     if score > 80:
#         above_80.append(name)

# print(f"Above 80 : {above_80}")

# sorted_students = sorted(students.items(), key=lambda x: x[1])
# print(sorted_students)

# for name, score in sorted_students:
#     print(f"{name}: {score}")


# print("------exercise4------")

# sentence = "the cat sat on the mat the cat sat"
# words = sentence.split()

# word_count = {}

# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1

# print(word_count)


# print("------matrix_stepA------")


# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print(matrix)
# print(matrix[0])
# print(matrix[1])
# print(matrix[0][0])
# print(matrix[1][1])
# print(matrix[2][2])
# print(matrix[2][0])
# print(len(matrix))
# print(len(matrix[0]))

# print("------matrix_stepB_C------")

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for row in matrix:
#     print("Row", row, "Type:", type(row))

# print("---")

# for row in matrix:
#     for item in row:
#         print(item)

# print(matrix[0][0])
# print(matrix[1][2])
# print(matrix[2][2])

# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(f"[{i}][{j}] = {matrix[i][j]}")

# print("------exercise5------")

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for row in matrix:
#     for item in row:
#         print(item, end=" ")
#     print()

# number_k = int(input("ye adad vared kon : "))

# for row in matrix:
#     for item in row:
#         print(item * number_k, end=" ")
#     print()


# matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# matrix_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]


# for i in range(len(matrix_a)):
#     for j in range(len(matrix_a[i])):
#         print(matrix_a[i][j] + matrix_b[i][j], end=" ")
#     print()


# print("------exercise6------")


# contacts = {}

# while True:
#     print("1. add contact")
#     print("2. search contact")
#     print("3. delete contact")
#     print("4. show all contacts")
#     print("5. edit contact")
#     print("6. exit")

#     person = input("ye shomare az mavared bala ro entekhab kon : ")

#     if person == "1":
#         print("add contact selected")
#         name = input("name : ").strip().lower()
#         if name in contacts:
#             choice = input("name exist. update? (y/n) : ")
#             if choice == "y":
#                 number = input("new number : ")
#                 contacts[name] = number
#                 print("contact updated")
#             else:
#                 print("operation cancelled")
#         else:
#             number = input("number : ")
#             contacts[name] = number
#             print("contact added")
#     elif person == "2":
#         print("search contact selected")
#         search_contact = input("write name : ").strip().lower()
#         result = contacts.get(search_contact)
#         if result:
#             print(search_contact, "-", result)
#         else:
#             print("contact not found")
#     elif person == "3":
#         print("delete contact selected")
#         deli = input("name delit : ").strip().lower()
#         if deli in contacts:
#             del contacts[deli]
#             print("contact deleted")
#         else:
#             print("contact not found")
#     elif person == "4":
#         print("show all contacts selected")
#         if contacts:
#             for name, number in sorted(contacts.items()):
#                 print(name, "-", number)
#         else:
#             print("no contacts")
#     elif person == "5":
#         print("edit contact selected")
#         edit_name = input("editing name : ").strip().lower()
#         if edit_name in contacts:
#             old_number = contacts.get(edit_name)
#             print(f"old number : {old_number}")

#             new_number = input("shomare jadid : ")
#             contacts[edit_name] = new_number
#             print("contact updated")
#         else:
#             print("contact not found")
#     elif person == "6":
#         print("goodbye")
#         break
#     else:
#         print("invalid choice")


# print("------exercise7------")
# cart = []

# while True:
#     print("1. add product")
#     print("2. show cart")
#     print("3. remove product")
#     print("4. calculate total")
#     print("5. update quantity")
#     print("6. apply discount")
#     print("7. print invoice")
#     print("8. exit")

#     person = input("shomare vared kon : ")

#     if person == "1":
#         product_name = input("name  product : ")
#         product_price = int(input("Enter price of price : "))
#         product_qty = int(input("Enter qty of price : "))
#         product = {"name": product_name, "price": product_price, "qty": product_qty}
#         cart.append(product)
#         # print(product)
#         # print(type(product))
#         print("mahsol azafe shod ")
#     elif person == "2":
#         print("your cart : ")
#         if cart:
#             for product in cart:
#                 print(
#                     "name :",
#                     product["name"],
#                     "- price :",
#                     product["price"],
#                     "- qty :",
#                     product["qty"],
#                 )
#         else:
#             print("cart is empty")
#     elif person == "3":
#         remove_product = input("name enter to remove : ")
#         found = False
#         for product in cart:
#             if product["name"] == remove_product:
#                 cart.remove(product)
#                 found = True
#                 print("product remove ")
#                 break
#         if not found:
#             print("product not found.")
#     elif person == "4":
#         total = 0
#         for product in cart:
#             item_total = product["price"] * product["qty"]
#             total += item_total
#         print(f"Total: {total}")
#     elif person == "5":
#         update_name = input("name of update : ")
#         new_qty = int(input("new qty : "))
#         found = False
#         for product in cart:
#             if product["name"] == update_name:
#                 if new_qty <= 0:
#                     print("invalid quantity")
#                 else:
#                     product["qty"] = new_qty
#                     print("Quantity updated.")
#                 found = True
#                 break
#         if not found:
#             print("product not found")
#     elif person == "6":
#         total = 0
#         for product in cart:
#             item_total = product["price"] * product["qty"]
#             total += item_total
#         discount_percent = float(input("Enter discount percent : "))
#         if discount_percent < 0 or discount_percent > 100:
#             print("Invalid discount.")
#         else:
#             discount_amount = total * (discount_percent / 100)
#             final_total = total - discount_amount
#             print(f"Total before discount : {total}")
#             print(f"Discount amount : {discount_amount}")
#             print(f"Final total : {final_total}")
#     elif person == "7":
#         if not cart:
#             print("Cart is empty.")
#         else:
#             print("========== INVOICE ==========")
#             print(f"{'product':<12}{'price':<8}{'Qty':<6}{'Total'}")
#             print("-" * 35)
#             subtotal = 0
#             for product in cart:
#                 item_total = product["price"] * product["qty"]
#                 subtotal += item_total
#                 print(
#                     f"{product['name']:<12}{product['price']:<8}{product['qty']:<6}{item_total}"
#                 )
#             print("-" * 35)
#             print(subtotal)
#             asking = input("Do you have a discount? (y/n) : ")
#             if asking == "y":
#                 discount_percent = float(input("type your percent : "))
#                 if 0 <= discount_percent <= 100:
#                     discount_amount = subtotal * (discount_percent / 100)
#                     final_total = subtotal - discount_amount
#                     print(f"Discount amount : {discount_amount}")
#                     print(f"final total : {final_total}")
#                 else:
#                     print("invalid discount")
#             else:
#                 print(f"Final total : {final_total}")
#             print("=============================")
#     elif person == "8":
#         print("Good bye")
#         break
#     else:
#         print("invalid choice")
