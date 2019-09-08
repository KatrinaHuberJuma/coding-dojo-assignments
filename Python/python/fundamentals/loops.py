# Basic - Print all integers from 0 to 150.
# for x in range(0, 150, 1):
#      print(x)
     

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
# for x in range(5, 1000, 5):
#      print(x)

# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

# for x in range(0, 100, 1):
#     if x % 5 == 0:
#         print("dojo")
#     else:
#         print(x)


# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

# def huge():
#     sum = 0
#     for x in range(1, 500000, 2):
#         # print(sum)
#         sum += x
#         # print(f"sum + {x}=", sum)

#     print(sum)

# huge()

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

# for x in range(2018, 0, -4):
#     print(x)


# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

def flex_counter(lowNum, highNum, mult):
    
    for x in range(lowNum, highNum+1, 1):
        if x % mult == 0:
            print(x)


# flex_counter(2,9,3)


# +++++++++++++ PART 2 ++++++++++++++++++


# Biggie Size - Given a list, write a function that 
# changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) 
# returns that same list, but whose values are now [-1, "big", "big", -5]

def biggie_size(lst):
    
    for x in range(0, len(lst), 1):
        if lst[x] > 0:
            lst[x] = "big"

    return lst

# print( biggie_size([-1, 3, 5, -5]) )


# Count Positives - Given a list of numbers, 
# create a function to replace the last value with the 
# number of positive values. 
# (Note that zero is not considered to be a positive number).

# Example: count_positives([-1,1,1,1]) 
# changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) 
# changes the list to [1,6,-4,-2,-7,2] and returns it

def count_positives(lst):
    counter = 0

    for x in range(0, len(lst), 1):
        if lst[x] > 0:
            counter += 1

    lst[len(lst)-1] = counter

    return lst

# print( count_positives([1,6,-4,-2,-7,-2]) )



# Sum Total - Create a function that 
# takes a list and returns the sum of all the values in the array.

# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def sum_total(lst):
    sum = 0

    for x in range(0, len(lst), 1):
        sum += lst[x]

    return sum

# print(sum_total([6,3,-2]))



# Average - Create a function that takes 
# a list and returns the average of all the values.

# Example: average([1,2,3,4]) should return 2.5


def average(lst):
    sum = 0

    for x in range(0, len(lst), 1):
        sum += lst[x]    

    return sum/len(lst)

# print(average([1,2,3,4]))



# Length - Create a function that takes a 
# list and returns the length of the list.

# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

def length(lst):
    return len(lst)

# print(length([]))


# Minimum - Create a function that takes a list of 
# numbers and returns the minimum value in the list. 
# If the list is empty, have the function return False.

# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

def minimum(lst):
    if lst == []:
        return False
    min = lst[0]
    for x in range(1, len(lst), 1):
        if lst[x] < min:
            min = lst[x]

    return min

# print(minimum([]))



# Maximum - Create a function that takes a list and 
# returns the maximum value in the array. 
# If the list is empty, have the function return False.

# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

def maximum(lst):
    if lst == []:
        return False
    max = lst[0]
    for x in range(1, len(lst), 1):
        if lst[x] > max:
            max = lst[x]

    return max

# print(maximum([37,2,1,-9]))


# Ultimate Analysis - Create a function that takes a 
# list and returns a dictionary that has the sumTotal, 
# average, minimum, maximum and length of the list.

# Example: ultimate_analysis([37,2,1,-9]) should 
# return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }


def ultimate_analysis(lst):
    analysis_dict = {
        'sum_total': lst[0],
        'min': lst[0],
        'max': lst[0],
        'length': len(lst)
    }

    for x in range(1, len(lst), 1):
        analysis_dict['sum_total'] += lst[x]
        if lst[x] < analysis_dict['min']:
            analysis_dict['min'] = lst[x]
        if lst[x] > analysis_dict['max']:
            analysis_dict['max'] = lst[x]

    avg = analysis_dict['max']/len(lst)
    analysis_dict['avg'] = avg

    return analysis_dict
        


print(ultimate_analysis([37,2,1,-9]))

# Reverse List - Create a function that takes a list and 
# return that list with values reversed. Do this without 
# creating a second list. 
# (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]


# camelCase
# UppperCamelCase
# kebab-camel
# snake_case

