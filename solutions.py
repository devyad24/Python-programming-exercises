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
x = int(input())
print(q_2(x))
