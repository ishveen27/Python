'''list: A collection of ordered, mutable items (can store different data types).
 Lists are defined using square brackets []. Example: fruits = ["apple", "banana", "cherry"]

 tuple: A collection of ordered, immutable items (cannot be changed after creation). Tuples are defined using parentheses (). Example: coordinates = (10, 20), colors = ("red", "green", "blue")

 set: A collection of unordered, unique items. Sets are mutable and defined using curly braces {}. Example: unique_numbers = {1, 2, 3, 4}, letters = {'a', 'b', 'c'}

 dict (Dictionary): A collection of key-value pairs, where each key is unique.
Dictionaries are mutable and defined using curly braces {} with keys and values separated by a colon(:). Example: student = {"name": "John", "age": 21}

None: Represents the absence of a value or a null value. It is often used to indicate no value or a missing value. Example: result = None'''

# calculator



print("Simple Calculator")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter the choice (1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "1":
    print("The addition of num1 and num2 is:", num1 + num2)
elif choice == "2":
    print("The subtraction of num1 and num2 is:", num1 - num2)
elif choice == "3":
    print("The multiplication of num1 and num2 is:", num1 * num2)
elif choice == "4":
    if num2 != 0:
        print("The division of num1 and num2 is:", num1 / num2)
    else:
        print("Error! Division by zero.")
else:
    print("Invalid choice")

