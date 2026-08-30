# def rectangle_area(tol, arz):
#     return tol * arz


# masahat = rectangle_area(5, 6)
# print(f"masahat shoma = {masahat}")


# def greet_user(name, greeting="Hello"):
#     return f"{greeting} {name}"


# print(greet_user("Ali"))
# print(greet_user("Sara", "Hi"))


# def is_even(number):
#     return number % 2 == 0


# print(is_even(4))
# print(is_even(7))
# print(is_even(0))
# print(is_even(-3))


# def multiply_all(*numbers):
#     result = 1
#     for num in numbers:
#         result *= num
#     return result


# print(multiply_all(2, 3))
# print(multiply_all(2, 3, 4))
# print(multiply_all(5))


# def create_profile(name, **details):
#     details["name"] = name
#     return details


# user_1 = create_profile("Sara", age=22, job="Designer")
# print(user_1)

# user_2 = create_profile("Reza", city="shiraz")
# print(user_2)


# prices = [100, 200, 300, 400]
# new_list = list(map(lambda p: p * 1.2, prices))
# print(new_list)


# scores = [12, 18, 9, 15, 8, 20, 14]
# new_scores = list(filter(lambda s: s >= 10, scores))
# print(new_scores)


# products = [
#     {"name": "Laptop", "price": 1000},
#     {"name": "Mouse", "price": 20},
#     {"name": "Monitor", "price": 200},
# ]

# products_price = sorted(products, key=lambda p: p["price"])
# print(products_price)

# ("--------exercise.1--------")


# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True


# print(is_prime(2))
# print(is_prime(7))
# print(is_prime(10))
# print(is_prime(1))
# print(is_prime(0))
# print(is_prime(-5))
# print(is_prime(13))
# print(is_prime(15))


# ("--------exercise.2--------")


# def fibonacci(n):
#     if n <= 0:
#         return []
#     if n == 1:
#         return [0]

#     fib_list = [0, 1]
#     for _ in range(n - 2):
#         next_num = fib_list[-1] + fib_list[-2]
#         fib_list.append(next_num)
#     return fib_list


# print(fibonacci(1))
# print(fibonacci(2))
# print(fibonacci(5))
# print(fibonacci(8))
# print(fibonacci(0))


# ("--------exercise.3--------")


# def count_words(text):
#     words = text.split()
#     word_count = {}
#     for word in words:
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1
#     return word_count


# print(count_words("apple banana apple orange banana apple"))

# print(count_words("python is great and python is easy"))

# print(count_words(""))


# def count_chars(text):
#     result = {}
#     for letter in text:
#         result[letter] = result.get(letter, 0) + 1
#     return result


# print(count_chars("hello"))
# print(count_chars("banana"))


# def count_items(shopping_list):
#     sabad = {}
#     for clothes in shopping_list:
#         sabad[clothes] = sabad.get(clothes, 0) + 1
#     return sabad


# print(count_items(["apple", "banana", "apple", "orange", "banana", "apple"]))

# print(count_items(["milk", "milk", "bread"]))

# print(count_items([]))


# def count_numbers(numbers):
#     tedad = {}
#     for adad in numbers:
#         tedad[adad] = tedad.get(adad, 0) + 1
#     return tedad


# print(count_numbers([1, 2, 2, 3, 3, 3, 4]))
# print(count_numbers([5, 5, 5, 5]))


# def group_by_length(words):
#     result = {}
#     for word in words:
#         length = len(word)
#         result[length] = result.get(length, 0) + 1
#     return result


# print(group_by_length(["cat", "dog", "elephant", "ant", "butterfly"]))
# print(group_by_length(["hi", "hello", "hey"]))


# ("--------exercise.4--------")


# def validate_password(password):
#     errors = []
#     if len(password) < 8:
#         errors.append("ramz bayad had e aghal 8 charecter bashad")

#     has_upper = False

#     for char in password:
#         if char.isupper():
#             has_upper = True
#             break

#     if not has_upper:
#         errors.append("ramz bayad hade aghal yek harf bozorg dashte bashad")

#     has_digit = False

#     for char in password:
#         if char.isdigit():
#             has_digit = True
#             break

#     if not has_digit:
#         errors.append("ramz bayad hade aghal ye adad dashte bashad")

#     if len(errors) == 0:
#         return {"valid": True, "errors": []}
#     else:
#         return {"valid": False, "errors": errors}


# print(validate_password("Ali12345"))
# print(validate_password("ali"))
# print(validate_password("Abcdefgh"))


# ("--------exercise.5--------")


# def calculator(a, b, operation):
#     if operation == "add":
#         return a + b
#     elif operation == "subtract":
#         return a - b
#     elif operation == "multiply":
#         return a * b
#     elif operation == "divide":
#         if b == 0:
#             return "khata taghsim bar sefr emkan pazir nist"
#         return a / b
#     elif operation == "power":
#         return a**b
#     else:
#         raise ValueError(f"amaliat '{operation}' na motabar ast")


# print(calculator(10, 5, "add"))

# print(calculator(10, 5, "subtract"))

# print(calculator(10, 5, "multiply"))

# print(calculator(10, 2, "divide"))

# print(calculator(10, 0, "divide"))

# print(calculator(2, 3, "power"))


# ("--------exercise.6--------")


# def flatten(nested_list):
#     result = []
#     for item in nested_list:
#         if isinstance(item, list):
#             result.extend(flatten(item))
#         else:
#             result.append(item)
#     return result


# print(flatten([1, 2, 3]))

# print(flatten([[1, 2], [3, 4]]))

# print(flatten([[1, 2], [3, [4, 5]], 6]))

# print(flatten([[[[1]]], 2, [3, [4, [5]]]]))
