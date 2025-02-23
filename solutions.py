from collections import defaultdict
from curses.ascii import isalnum, isalpha, isdigit, islower, isupper
import itertools
import math
from operator import itemgetter
import os
import timeit
import re
import heapq

from traitlets import default
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


'''
q11:
    Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
    Example:
    0100,0011,1010,1001
    Then the output should be:
    1010
'''      

def q_11():
    nums = [inp for inp in input().split(',')]
    res = []
    for n in nums:
        #you can turn binary to decimal by typecasting string to base 2
        dec = int(n,2)
        if dec % 5 == 0:
            res.append(n)
    print(','.join(res))
# q_11()

'''
q12:
    Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
    The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

def q_12():
    res = []
    for num in range(1000, 3001):
        org_num = num
        while num != 0:
            last_digit = num % 10
            if last_digit % 2 != 0:
                break
            num //= 10
        if num == 0:
            res.append(str(org_num))
    print(','.join(res))

# q_12()

'''
q13:
    Write a program that accepts a sentence and calculate the number of letters and digits.
    Suppose the following input is supplied to the program:
    hello world! 123
    Then, the output should be:
    LETTERS 10
    DIGITS 3
'''

def q_13():
    s = input()
    letters = digits =  0

    for c in s:
        if c.isdigit():
            digits += 1
        elif c.isalpha():
            letters += 1
    print('LETTERS', letters)
    print('DIGITS', digits)

# q_13()

'''
q14:
    Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
    Suppose the following input is supplied to the program:
    Hello world!
    Then, the output should be:
    UPPER CASE 1
    LOWER CASE 9
'''

def q_14():
    s = input()
    upper = lower = 0
    for c in s:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
    print("UPPER", upper)
    print("LOWER", lower)

# q_14()

'''
q15:
    Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
    Suppose the following input is supplied to the program:
    9
    Then, the output should be:
    11106
'''

def q_15():
    a = input()
    # "%s" is a format specifier for string just like in C
    n1 = int( "%s" % a )
    n2 = int( "%s%s" % (a,a) )
    n3 = int( "%s%s%s" % (a,a,a) )
    n4 = int( "%s%s%s%s" % (a,a,a,a) )
    print(n1+n2+n3+n4)

# q_15()

'''
q16:
    Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
    Suppose the following input is supplied to the program:
    1,2,3,4,5,6,7,8,9
    Then, the output should be:
    1,3,5,7,9
'''

def q_16():
    odd_nums = [n for n in input().split(',') if int(n) % 2 != 0]
    print(','.join(odd_nums))

# q_16()

'''
q17:
    Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
    D 100
    W 200

    D means deposit while W means withdrawal.
    Suppose the following input is supplied to the program:
    D 300
    D 300
    W 200
    D 100
    Then, the output should be:
    500
'''

def q_17():
    net = 0 
    while True:
        transaction = input()
        if transaction:
            transaction = transaction.split(' ')
            trans_type = transaction[0] 
            trans_amount = transaction[1] 
            #assuming if trans_type is not D then it would be W
            net = (net + int(trans_amount)) if trans_type == 'D' else (net - int(trans_amount))
        else:
            break
    print(net)

# q_17()

'''
q18:
    A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
    Following are the criteria for checking the password:
    1. At least 1 letter between [a-z]
    2. At least 1 number between [0-9]
    1. At least 1 letter between [A-Z]
    3. At least 1 character from [$#@]
    4. Minimum length of transaction password: 6
    5. Maximum length of transaction password: 12
    Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
    Example
    If the following passwords are given as input to the program:
    ABd1234@1,a F1#,2w3E*,2We3345
    Then, the output of the program should be:
    ABd1234@1
'''

def q_18():
    passwords = [x for x in input().split(',')]
    valid_passwrd = []
    for p in passwords:
        if len(p) < 6 or len(p) > 12:
            continue  
        elif not re.search('[a-z]', p):
            continue
        elif not re.search('[A-Z]', p):
            continue
        elif not re.search('[0-9]', p):
            continue
        elif not re.search('[$#@]', p):
            continue
        else:
            valid_passwrd.append(p)
    print(','.join(valid_passwrd))

# q_18()

'''
q19:

    You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
    1: Sort based on name;
    2: Then sort based on age;
    3: Then sort by score.
    The priority is that name > age > score.
    If the following tuples are given as input to the program:
    Tom,19,80
    John,20,90
    Jony,17,91
    Jony,17,93
    Json,21,85
    Then, the output of the program should be:
    [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
'''

def q_19():

    details = []
    while True:
        detail = input()
        if detail:
            details.append(tuple(detail.split(',')))
        else:
            break
    print(sorted(details, key=itemgetter(0,1,2)))

# q_19()

'''
q20:
    Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
'''

#https://stackoverflow.com/questions/1756096/understanding-generators-in-python
def q_20():
    a = 0

    while True:
        b = a
        a = a + 1
        if b % 7 == 0:
            yield b
# print(list(itertools.islice(q_20(), 100)))

'''
q21:
    A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
    UP 5
    DOWN 3
    LEFT 3
    RIGHT 2
    ¡­
    The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
    Example:
    If the following tuples are given as input to the program:
    UP 5
    DOWN 3
    LEFT 3
    RIGHT 2
    Then, the output of the program should be:
    2
'''
def q_21():
    pos = [0, 0]

    while True:
        s = input()
        if not s:
            break
        movement = s.split(' ')
        direction = movement[0]
        step = int(movement[1])

        if direction == 'UP':
            pos[1] += step
        elif direction == 'DOWN':
            pos[1] -= step
        elif direction == 'LEFT':
            pos[0] -= step
        elif direction == 'RIGHT':
            pos[0] += step
        else:
            pass
    #distance formula for two points on a cartesian plane is ((x2-x1)^2 + (y2-y1)^2)^1/2 here x1 = y1 = 0
    print(int(round(math.sqrt(pos[0]**2 + pos[1]**2))))

# q_21()

'''
q22:
    Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
    Suppose the following input is supplied to the program:
    New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
    Then, the output should be:
    2:2
    3.:1
    3?:1
    New:1
    Python:5
    Read:1
    and:1
    between:1
    choosing:1
    or:2
    to:1
'''

def q_22():
    word_freq = defaultdict(int)
    s = input()
    words = s.split(' ')
    words.sort()
    for i in range(len(words)):
        word_freq[words[i]] += 1
    print(word_freq)
    return word_freq

# word_freq = q_22()
# print('\n'.join([f'{k}:{v}' for k,v in word_freq.items()]))


'''
q23:
    Write a method which can calculate square value of number
'''

def q_23():
    s = input()
    if not isdigit(s):
        pass
    s = int(s)
    return s**2

# square_val = q_23()
# print(square_val)

'''
q24:
    Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.
    Please write a program to print some Python built-in functions documents, such as abs(), int(), input()

And add document for your own function
'''

def q_24():
    '''
    This method returns docs of some popular python methods.
    And this is the documentation of current method.
    '''
    print(abs.__doc__)
    print(int.__doc__)
    print(input.__doc__)

    return


# a = q_24
# print(a.__doc__)
# print(a())

'''
q25:
    Define a class, which have a class parameter and have a same instance parameter.
'''
class dummy:
    number = 0
    def __init__(self, number=0):
        self.number = number
    
    def increment_num(self):
        self.number += 1
    def decrement_num(self):
        self.number -= 1
    def get_num(self):
        return self.number
    def set_num(self, number):
        self.number = number

# s = input()
# new_cls = dummy(int(s))
# print(new_cls.get_num())
# new_cls.increment_num()
# new_cls.increment_num()
# print(new_cls.get_num())
# new_cls.decrement_num()
# print(new_cls.get_num())

'''
q26:
    Define a function which can compute the sum of two numbers.
'''
def q_26():
    s = input()
    nums = s.split(' ')
    a = int(nums[0])
    b = int(nums[1])
    return a + b
# print(q_26())

'''
q27:
    Define a function that can convert a integer into a string and print it in console.
'''

def q_27(a):
    return str(a)
# int_in_str = q_27(55)
# print(int_in_str, type(int_in_str))

'''
q28:

'''

'''
q29:
    solution same as q26
'''

'''
q30:
    Define a function that can accept two strings as input and concatenate them and then print it in console.
'''
def q_30():
    s = input()
    return "".join(s.split(' '))
# print(q_30())







    
