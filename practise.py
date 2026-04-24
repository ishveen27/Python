# name = input("Enter the name: ")
# phone_no = int(input("Enter the phone no: "))
# marks = int(input("Enter the marks: "))
# a = "The name of the student is {}, his marks are {} and phone no is {}".format(name,marks,phone_no  )
# print(a)

# #
# l = [2,5,25,15,6,7,10]
# result = list(filter(lambda x : x%5==0,l))
# print(result)

# #
# from functools import reduce
# l = [12,50,14,60,13,16]
# from functools import reduce
# l = [12,50,14,60,13,16]
# # result=reduce(max,l)
# result=reduce(lambda a,b:a if a>b else b,l)
# print(result)

# #
# table_7 = [7*i for i in range(1,10)]
# print(table_7)
# vertical = "\n".join(str(a) for a in table_7)
# print(vertical)


# def generator():
#     for i in range(5000):
#         yield i
# a = generator()

# # print(next(a))
# # for j in a: # give sequence very fast in sec
# #    print(j)

# class MyIterator:
#     def __init__(self, start, end):
#         self.current = start
#         self.end = end

#     def __iter__(self):
#         return self   # iterator object return karega

#     def __next__(self):
#         if self.current <= self.end:
#             value = self.current
#             self.current += 1
#             return value
#         else:
#             raise StopIteration   # jab values khatam ho jaye
# it = MyIterator(1, 5)

# for val in it:     # for loop internally next() use karega
#     print(val)

 # it will update s1 # to merge two set
# Recursive function to find Fibonacci number

