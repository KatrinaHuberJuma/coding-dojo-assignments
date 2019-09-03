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


# #15
# def a():
#     print(1)
#     x = b()
#     print(x)
#     return 10
# def b():
#     print(3)
#     return 5
# y = a()
# print(y)

# # predicted: 1,3,5,10 ==> correct


# ++++++++++++ PART 2 ++++++++++


# Countdown - Create a function that 
# accepts a number as an input. Return a new list that 
# counts down by one, from the number (as the 0th element) 
# down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]

def count_down(num):
    lst = []
    for x in range(num, -1, -1):
        lst.append(x)

    return lst

# print(count_down(5))

# Print and Return - Create a function that will 
# receive a list with two numbers. 
# Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2

def print_and_return(lst):
    print(lst[0])
    return(lst[1])

# print(print_and_return([1,2]))


# First Plus Length - Create a function that accepts 
# a list and returns the sum of the first value 
# in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) 
# should return 6 (first value: 1 + length: 5)

def first_plus_length(lst):
    return lst[0] + len(lst)

# print(first_plus_length([1,2,3,4,5]))


# Values Greater than Second - Write 
# a function that accepts a list and 
# creates a new list containing only the 
# values from the original list that are 
# greater than its 2nd value. 
# Print how many values this is and then 
# return the new list. If the list has less than 2 
# elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) 
# should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False


def values_greater_than_second(lst):
    greater_lst = []

    if len(lst) < 2:
        return False

    for x in range(0, len(lst), 1):
        if lst[x] > lst[1]:
            greater_lst.append(lst[x])

    print(len(greater_lst))
    return greater_lst

# print(values_greater_than_second([5,2,3,2,1,4]))

# This Length, That Value - Write a function 
# that accepts two integers as parameters: size and value. 
# The function should create and return a list whose 
# length is equal to the given size, and 
# whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def length_and_value(sze, val):
    fin = []

    for x in range(sze, 0, 1):
        fin.append(val)


    return fin

print(length_and_value(4,7))
