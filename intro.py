a = 1
b = 4.4
c = True
d = "harry"
# type function
print("hey",6,5,8, sep = "~",end = "001")
#string should be written in "" codes
''' separator specidy the how to separate object
end specify whta to print at the end
escape sequence charactor : /n
pip = pip install packages
type function used to tell the type of data type
In pythonn everything is a object'''
print(type(a))
print(type(b))
print(type(c))
print(type(d))
''' ✅ Rules for Defining a Variable in Python:
Must start with a letter or underscore _
✔️ Valid: name, _value
❌ Invalid: 1name, @var

Can contain letters, digits, and underscores only
✔️ Valid: age1, student_name, num_2
❌ Invalid: my-name, total%

Case-sensitive
Age, age, and AGE are three different variables.

Cannot use Python reserved keywords (like for, while, class, def, if, etc.).
❌ Invalid: for = 10, class = "abc"

No spaces allowed in variable names.
❌ Invalid: my name = "Ishveen"
✔️ Use underscore instead → my_name = "Ishveen"'''

# typecasting
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print(type(a))
# comparison operator
a = 34
b = 80
if(a>b):
 print("a is greator")
elif(b>a):
 print("b is greator")
else: 
 print("a is equal b")
# average of num
x = int(input("enter the first num:"))
y = int(input("enter the second number"))
c = int((x+y)/2)
print(c)
# square of number
a = int(input("enter the number:"))
result = (a*a)
print(result)


