# class Car:
#     def __init__(self, brand, color, speed=0):
#         self.brand = brand
#         self.color = color
#         self.speed = speed

#     def accelerate(self, amount):
#         self.speed += amount
#         return f"New speed : '{self.speed}'"

#     def __str__(self):
#         return f"mashin '{self.brand}' ba rang '{self.color}'"


# my_car = Car("Pride", "White")
# print(my_car)
# print(my_car.speed)
# print(my_car.accelerate(30))
# print(my_car.accelerate(20))
# print(my_car.speed)

# ("--------exercise.7--------")


# class BankAccount:
#     def __init__(self, owner, initial_balance=0):
#         self.owner = owner
#         self.balance = initial_balance
#         self.transaction = []
#         if initial_balance > 0:
#             self.transaction.append(f"mojodi avalia: {initial_balance} toman")

#     def deposit(self, amount):
#         self.balance += amount
#         self.transaction.append(f"mojodi jadid bad az deposit : '{self.balance}'")
#         return self.balance

#     def withdraw(self, amount):
#         if amount > self.balance:
#             return "mojodi kafi nist"
#         if amount <= self.balance:
#             self.balance -= amount
#             self.transaction.append(f"mojodi jadid bad az withdraw: {self.balance}")
#             return self.balance

#     def get_balance(self):
#         return self.balance

#     def get_history(self):
#         return self.transaction

#     def transfer(self, other_account, amount):
#         if amount > self.balance:
#             return "enteghal na movafagh : mojodi kafi nist "
#         self.withdraw(amount)
#         other_account.deposit(amount)
#         return f"mablagh {amount} toman ba movafaghiyat fe hesab {other_account.owner} montaghel shod"

#     def __str__(self):
#         return f"hesab {self.owner}: {self.balance} toman"


# print("\n--------test_system_bank--------")

# acc1 = BankAccount("Ali", 1000)
# acc2 = BankAccount("sara", 500)

# print(acc1)
# print(acc2)

# acc1.deposit(500)
# acc2.deposit(200)
# print(f"mojodi ali : {acc1.get_balance()}")

# acc1.transfer(acc2, 300)

# print(f"mojodi ali bad az enteghal: {acc1.get_balance()}")
# print(f"mojodi sara bad az daryaft: {acc2.get_balance()}")

# print("\n tarakonesh haye Ali:")
# for t in acc1.get_history():
#     print(f" - {t}")


("--------exercise.8--------")


class Book:

    def __init__(self, title, author, isbn, year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year

    def __str__(self):
        return f"'{self.title}'by {self.author} ({self.year})"


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                return "ketab hazf shod"

        return "ketab yaft nashod"

    def search_by_title(self, title):
        results = []
        for book in self.books:
            if title.lower() in book.title.lower():
                results.append(book)
        return results

    def search_by_author(self, author):
        results = []
        for book in self.books:
            if author.lower() in book.author.lower():
                results.append(book)
        return results

    def list_all(self):
        return self.books

    def __str__(self):
        return f" library with {len(self.books)}"


print("\n---------test_Library-----------")

lib = Library()
print(lib)

b1 = Book("Python Crash Course", "Eric Matthes", "111", 2019)
b2 = Book("Clean Code", "Robert Martin", "222", 2008)
b3 = Book("Python Cookbook", "David Beazley", "333", 2013)

lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)
print(lib)

print("\n search book python:")
for b in lib.search_by_title("python"):
    print(f" - {b}")

print("\n search author'Robert':")
for b in lib.search_by_author("Robert"):
    print(f" - {b}")

print("\n remove book 222:")
print(lib.remove_book("222"))
print(lib)

print(lib.remove_book("999"))
