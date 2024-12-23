import math
import timeit
from re import split
import heapq
'''
q1:
    Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
    between 2000 and 3200 (both included).
    The numbers obtained should be printed in a comma-separated sequence on a single line.
'''
def q_1():
    x = 2000
    y = 3200
    res = []
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            res.append(str(i))
    return ",".join(res)

# print(div_by_seven())
'''
q2:
    Write a program which can compute the factorial of a given numbers.
    The results should be printed in a comma-separated sequence on a single line.
    Suppose the following input is supplied to the program:
    8
    Then, the output should be:
    40320
'''
def q_2(n):
    if n == 0:
        return 1
    return n * q_2(n-1)
# x = int(input())
# print(q_2(x))

'''
q3:
    With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
    Suppose the following input is supplied to the program:
    8
    Then, the output should be:
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
'''
def q_3(n):
    res = {}
    for i in range(1, n+1):
        res[i] = i*i
    return res
# print(q_3(int(input())))

'''
q4:
    Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
    Suppose the following input is supplied to the program:
    34,67,55,33,12,98
    Then, the output should be:
    ['34', '67', '55', '33', '12', '98']
    ('34', '67', '55', '33', '12', '98')
'''
def q_4(s):
    s_list = s.split(',')
    s_tuple = tuple(s_list)
    print("list:",s_list)
    print("tuple:",s_tuple)
    return
# q_4(str(input()))

'''
q5:
    Define a class which has at least two methods:
    getString: to get a string from console input
    printString: to print the string in upper case.
    Also please include simple test function to test the class methods.
'''

class q5(object):
    def __init__(self):
        self.s = ""
    def getString(self):
        self.s = input()
        return self.s
    def toUpper(self):
        print(self.s.upper())
        return self.s.upper()

# str_cls = q5()
# new_str = str_cls.getString()
# upper_str = str_cls.toUpper()
# print(upper_str == new_str.upper())

'''
q6:
    Write a program that calculates and prints the value according to the given formula:
    Q = Square root of [(2 * C * D)/H]
    Following are the fixed values of C and H:
    C is 50. H is 30.
    D is the variable whose values should be input to your program in a comma-separated sequence.
    Example
    Let us assume the following comma separated input sequence is given to the program:
    100,150,180
    The output of the program should be:
    18,22,24
'''

def q_6():
    res = []
    c = 50
    h = 30
    #2*50*100 / 30 -> 10000 / 30
    d_list = [d for d in input().split(',')]
    for number in d_list:
        number = float(number) 
        q = math.floor(math.sqrt((2*c*number) // h))
        res.append(str(q))
    res = ','.join(res)
    print(res)
# q_6()

'''
q7:
    Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
    Note: i=0,1.., X-1; j=0,1,¡­Y-1.
    Example
    Suppose the following inputs are given to the program:
    3,5
    Then, the output of the program should be:
    [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
'''

def q_7():
    inp = [inp for inp in input().split(',')] 
    if len(inp) != 2:
        print("function expects 2 arguments row and column")
        return

    matrix_row = int(inp[0])
    matrix_col = int(inp[1])

    #with list comprehension we can built a 2d matrix filled with 0s of length m x n where m is matrix_row and n is matrix_col
    res = [[0 for _ in range(matrix_col)] for _ in range(matrix_row)]

    for i in range(matrix_row):
        for j in range(matrix_col):
            res[i][j] = i*j
    print(res)

# q_7()

'''
q8:
    Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
    Suppose the following input is supplied to the program:
    without,hello,bag,world
    Then, the output should be:
    bag,hello,without,world
'''

# start = timeit.default_timer()

def q_8():
    words = [word for word in input().split(',')]
    # words.sort()
    heapq.heapify(words)
    print(','.join(words))
# q_8()

# stop = timeit.default_timer()
# print('Time: ', stop - start)  

'''
q9:
    Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
    Suppose the following input is supplied to the program:
    Hello world
    Practice makes perfect
    Then, the output should be:
    HELLO WORLD
    PRACTICE MAKES PERFECT
'''

def q_9():
    res = []
    while True:
        s = str(input())
        if s:
            res.append(s.upper())
        else:
            break
    for r in res:
        print(r)
# q_9()

'''
q10:
    Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
    Suppose the following input is supplied to the program:
    hello world and practice makes perfect and hello world again
    Then, the output should be:
    again and hello makes perfect practice world
'''

def q_10():
    s = input()
    words = [word for word in s.split(' ')]
    words = set(words)
    words = list(words)
    words.sort()
    print(' '.join(words))
# q_10()


        