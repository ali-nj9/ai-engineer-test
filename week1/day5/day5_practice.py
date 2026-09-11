# with open("test.txt", "w", encoding="utf-8") as file:
#     file.write("salam donya \n")
#     file.write("in avalin fyle man dar python ast. \n")

# print("fyle ba movafaghyat sakhte va neveshte shod.")

# with open("test.txt", "r", encoding="utf-8") as file:
#     content = file.read()
#     print("\n mohtavay fyle:")
#     print(content)

# with open("test.txt", "a", encoding="utf-8") as file:
#     file.write("in khat sevom be enteha khat sevom ezafe shod.\n")

# with open("test.txt", "r", encoding="utf-8") as file:
#     for line in file:
#         print(line.strip())

# with open("test.txt", "r", encoding="utf-8") as file:
#     for index, line in enumerate(file, start=1):
#         print(f"line {index}: {line.strip()}")

# print("\n--- ezafe kardan khat gadid ba halat 'a' ---")

# print("\n--- khandan khat be khat ba shomare khat ---")


# import json

# data = {"name": "Ali", "age": 23}

# with open("data.json", "w", encoding="utf-8") as file:
#     json.dump(data, file, ensure_ascii=False, indent=4)

# with open("data.json", "r", encoding="utf-8") as file:
#     data = json.load(file)
#     print(data)
#     print(data["name"])

# data = {"name": "ali"}
# json_string = json.dumps(data, ensure_ascii=False)
# print(json_string)

# json_string = '{"name": "Ali", "age": 23}'
# data = json.loads(json_string)
# print(data["age"])


# print("\n--- JSON: zakhireh va khandan etela at danesh jo ---")

# import json

# student_db = [{"name": "Ali", "age": 23, "grades": [20, 18, 19], "is_passed": True}]

# with open("student_db.json", "w", encoding="utf-8") as file:
#     json.dump(student_db, file, ensure_ascii=False, indent=4)

# print("daneshjo aval zakhireh shod")

# with open("student_db.json", "r", encoding="utf-8") as file:
#     current_student = json.load(file)

# new_student = {"name": "sara", "age": 20, "grades": [20, 18, 15], "is_passed": True}

# current_student.append(new_student)

# with open("student_db.json", "w", encoding="utf-8") as file:
#     json.dump(current_student, file, ensure_ascii=False, indent=4)

# print("danweshjo dovom ezafe shod ! gdsj nahaii")
# print(current_student)


# try:
#     file = open("my_data.txt", "r")
#     content = file.read()
# except FileNotFoundError:
#     print("fyle yaft nashod. lotfan fyle ra barresi konid.")
# else:
#     print("fyle ba movafaghyat khand shod. mohtavay fyle:")
#     print(content)
# finally:
#     print("amaliat khandan fyle tamam shod.")


# def safe_calculator():
#     try:
#         num1 = int(input("lotfan adad vared konid : "))
#         num2 = int(input("lotfan adad dovom ra vared konid : "))
#         result = num1 / num2
#     except ValueError:
#         print("lotfan faghat adad vared konid.")
#     except ZeroDivisionError as e:
#         print("taqsim bar sefr mojaz nist.")
#     else:
#         print(f"natige taqsim {num1} bar {num2} = {result}")
#     finally:
#         print("payan amaliat mashin hesab")


# safe_calculator()


# ("--------exercise.1--------")
# from datetime import datetime

# while True:
#     print("===modiriat yaddasht ha===")
#     print("1. afzodan yaddasht jadid")
#     print("2. moshahede hame yaddasht ha")
#     print("3. pak kardan hame yaddasht ha")
#     print("4. khoroj")
#     mavarad = input("lotfan yek ghesmat ra entekhab konid (1-4): ")
#     if mavarad == "1":
#         note = input("lotfan matn yaddasht ra vared konid: ")
#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         with open("notes.txt", "a", encoding="utf-8") as file:
#             file.write(f"\n{note} [{timestamp}]")
#             print("yaddasht ba movafaghyat zakhireh shod.")
#     elif mavarad == "2":
#         try:
#             with open("notes.txt", "r", encoding="utf-8") as file:
#                 content = file.read()
#                 if content:
#                     print("\n --- hame yaddasht ha ---")
#                     print(content)
#                 else:
#                     print("hich yaddashti sabt nashode ast.")
#         except FileNotFoundError:
#             print("hich yaddashti sabt nashode ast.!")
#         else:
#             print(content)
#     elif mavarad == "3":
#         porsesh = input(
#             "aya motmaen hastid ke mikhahid hame yaddasht ha ra pak konid? (bale/na): "
#         )
#         if porsesh.lower() == "bale":
#             with open("notes.txt", "w", encoding="utf-8") as file:
#                 file.write("")
#                 print("hame yaddasht ha pak shodand.")
#     elif mavarad == "4":
#         print("khoroj az barname...")
#         break


# ("--------exercise.2--------")

# import json

# FILENAME = "products.json"


# def load_products():
#     try:
#         with open(FILENAME, "r", encoding="utf-8") as file:
#             return json.load(file)
#     except FileNotFoundError:
#         return []


# def save_products(products):
#     with open(FILENAME, "w", encoding="utf-8") as file:
#         json.dump(products, file, ensure_ascii=False, indent=4)


# while True:
#     print("===modiriat mahsolat===")
#     print("1.namaye hame mahsolat")
#     print("2. afzodan mahsol jadid")
#     print("3. virayesh mahsol")
#     print("4. hazf mahsol")
#     print("5. khoroj")
#     number = input("lotfan yek ghesmat ra entekhab konid (1-5): ")

#     if number == "1":
#         products = load_products()
#         if products:
#             print("\n--- hame mahsolat ---")
#             for product in products:
#                 print(
#                     f"ID: {product['id']}, Name: {product['name']}, price: {product['price']}, quantity: {product['quantity']}"
#                 )
#         else:
#             print("hich mahsoli sabt nashode ast.")
#     elif number == "2":
#         products = load_products()
#         name = input("lotfan nam mahsol ra vared konid: ")
#         new_id = (max(product["id"] for product in products) + 1) if products else 1
#         price = float(input("lotfan gheymat mahsol ra vared konid: "))
#         quantity = int(input("lotfan tedad mahsol ra vared konid: "))
#         new_product = {"id": new_id, "name": name, "price": price, "quantity": quantity}
#         products.append(new_product)
#         save_products(products)
#         print("mahsol ba movafaghyat ezafe shod.")
#     elif number == "3":
#         products = load_products()
#         product_id = int(input("lotfan ID mahsol ra vared konid: "))
#         found = False
#         for product in products:
#             if product["id"] == product_id:
#                 new_price = float(input("lotfan gheymat jadid ra vared konid: "))
#                 found = True
#                 break
#         if found == True:
#             products["price"] = new_price
#             save_products(products)
#             print("mahsol ba movafaghyat virayesh shod.")
#         if found == False:
#             print("mahsol ba in ID yaft nashod.")
#     elif number == "4":
#         products = load_products()
#         product_id = int(input("lotfan ID mahsol ra vared konid: "))
#         found = False
#         for product in products:
#             if product["id"] == product_id:
#                 products.remove(product)
#                 found = True
#                 break
#         if found == True:
#             save_products(products)
#             print("mahsol ba movafaghyat hazf shod.")
#         if found == False:
#             print("mahsol ba in ID yaft nashod.")
#     elif number == "5":
#         break


# ("--------exercise.3--------")

# from datetime import datetime
# import json


# class InvalidFileFormatError(Exception):
#     pass


# def log_error(error_massage):
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     with open("error.log", "a", encoding="utf-8") as file:
#         file.write(f"[{timestamp}] ERROR: {error_massage}\n")


# def safe_read_json(filename):
#     try:
#         with open(filename, "r", encoding="utf-8") as file:
#             return json.load(file)
#     except FileNotFoundError:
#         msg = f"file '{filename}' not found so let's create it."
#         log_error(msg)
#         print(f"! {msg}")
#         with open(filename, "w", encoding="utf-8") as file:
#             json.dump([], file, indent=4, ensure_ascii=False)
#             return []
#     except json.JSONDecodeError:
#         msg = f"file '{filename}' kharab bod va reset shod."
#         log_error(msg)
#         print(f"!!! {msg}")
#         with open(filename, "w", encoding="utf-8") as file:
#             json.dump([], file, indent=4, ensure_ascii=False)
#             return []


# print("\n--- shorooe test safe_read_json ---")

# with open("corrupted.json", "w", encoding="utf-8") as file:
#     file.write("yek file kharab ast va JSON nist.")

# data1 = safe_read_json("products.json")
# print(f"natige products.json: {len(data1)} mahsol dar file ast.")

# data2 = safe_read_json("not_exist.json")
# print(f" natige not_exist.json: {data2}")

# data3 = safe_read_json("corrupted.json")
# print(f"natige corrupted.json: {data3}")
