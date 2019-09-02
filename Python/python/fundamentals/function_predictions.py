# def a():
#     return 5
# print(a())

# # predicted: 5 ===> correct

# #2
# def a():
#     return 5
# print(a()+a())

# # predicted: 10 ===> correct

# #3
# def a():
#     return 5
#     return 10
# print(a())

# # predicted: 5 ===> correct


# #4
# def a():
#     return 5
#     print(10)
# print(a())

# # predicted: 5 ===> correct

# #5
# def a():
#     print(5)
# x = a()
# print(x)

# # predicted: 5, None ====> correct


# #6
# def a(b,c):
#     print(b+c)
# print(a(1,2) + a(2,3))

# # predicted: 3, 5, NaN ===> 3, 5, TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

# #7
# def a(b,c):
#     return str(b)+str(c)
# print(a(2,5))

# # predicted: "25" ====> correct


# #8
# def a():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(a())

# # predicted: 100, 10 ===> correct


# #9
# def a(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(a(2,3)) # 7
# print(a(5,3)) # 14
# print(a(2,3) + a(5,3)) # 21
# # correct


# #10
# def a(b,c):
#     return b+c
#     return 10
# print(a(3,5))

# # predicted: 8 # correct


# #11
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
# print(b)
# a()
# print(b)

# # predicted: 500, 500, 300, 500 ===> correct


# #12
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# a()
# print(b)

# # predicted: 500, 500, 300, 500

# #13
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=a()
# print(b)

# # predicted 500, 500, 300, 300

# #14
# def a():
#     print(1)
#     b()
#     print(2)

# def b():
#     print(3)
# a()

# # predicted: 1, error ## 1, 3, 2 
# conclusion: the b() function was defined before a() was called


#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

# predicted: 1,3,5,10 ==> correct


# ++++++++++++ PART 2 ++++++++++