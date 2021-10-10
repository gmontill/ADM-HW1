#Python if-else
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if (n%2 == 0):
        if (n <= 5 and n >= 2):
            print("Not Weird")
        elif (n > 5 and n < 21):
            print("Weird")
        else:
            print("Not Weird")
    else:
        print("Weird")

#Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

#Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

#Loops
if __name__ == '__main__':
    n = int(input())
    i=0
    while i < n:
        print(i*i)
        i=i+1

#Write a Function
def is_leap(year):
    leap = False
    if (year % 4 == 0):
        if (year % 100 == 0 and year % 400 == 0):
            return True
        elif (year % 100 == 0):
            return False
        return True
        # Write your logic here

    return leap

#Say "Hello WOrld!" with Python
if __name__ == '__main__':
    print "Hello, World!"

#Print Function
if __name__ == '__main__':
    n = int(input())
    print(*range(1, n + 1), sep='')

#List Comprehension
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print([[a, b, c] for a in range(0, x + 1) for b in range(0, y + 1) for c in range(0, z + 1) if a + b + c != n])

#Nested Lists
if __name__ == '__main__':
    students = dict()
    second_min = 1000
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students[name] = score

    min = min(students.values())
    for i in students.values():
        if (i < second_min and i > min):
            second_min = i

    outputs = []
    for key in students.keys():
        if (students[key] == second_min):
            outputs.append(key)
    outputs.sort()
    for output in outputs:
        print(output)

#Finding the Percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    sum = 0

    for key in student_marks:
        if key == query_name:
            for i in student_marks[key]:
                sum += i
    avg = "{:.2f}".format(sum / 3)

    print(avg)


#Lists
if __name__ == '__main__':
    N = int(input())
    lis = []

    for i in range(0, N):
        inp = input().split()

        if len(inp) == 1:
            cmd = inp[0]
        elif len(inp) == 2:
            cmd = inp[0]
            e = int(inp[1])
        elif len(inp) == 3:
            cmd = inp[0]
            i = int(inp[1])
            e = int(inp[2])

        if cmd == 'insert':
            lis.insert(i, e)
        elif cmd == 'print':
            print(lis)
        elif cmd == 'remove':
            lis.remove(e)
        elif cmd == 'append':
            lis.append(e)
        elif cmd == 'sort':
            lis.sort()
        elif cmd == 'pop':
            lis.pop()
        elif cmd == 'reverse':
            lis.reverse()

#Tuples
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    t = tuple(integer_list)
    print(hash(t))

#Find the runner up score
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    maximum = max(arr)
    second_max = -101
    for i in arr:
        if i < maximum and i > second_max:
            second_max = i
    print(second_max)

#String Split and Join
def split_and_join(line):
    line = line.split(' ')
    line = "-".join(line)
    return line

#What's your name?
def print_full_name(first, last):
    print('Hello ' + first + ' ' + last + '! You just delved into python.')

#Mutations
def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string

#Find a String
def count_substring(string, sub_string):
    count=0
    for s in range(0, len(string)):
        if string[s:s+len(sub_string)] == sub_string:
            count+=1
    return count

#String Validators
if __name__ == '__main__':
    s = input()
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))

#Text alignment
#Replace all ______ with rjust, ljust or center.

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


#Text Wrap
def wrap(string, max_width):
    return (textwrap.fill(string, max_width))

#Designer Door Mat
rows,cols = map(int,input().split())

middle = rows//2 + 1

for r in range(1, middle):
    c = (r*2)-1
    c*='.|.'
    print(c.center(cols, '-'))

print("WELCOME".center(cols, '-'))

for r in reversed(range(1, middle)):
    c = (r*2 -1)*'.|.'
    print(c.center(cols, '-'))

#String Formatting
    def print_formatted(number):


    # your code goes here
    out = []
    spaces = 0
    for i in range(1, number + 1):
        dec_num = str(i)
        oct_num = str(oct(i))[1:]
        hex_num = (str(hex(i)[2:])).upper()
        bin_num = str(bin(i))[2:]
        line = [dec_num, oct_num, hex_num, bin_num]
        out.append(line)
        spaces = max(spaces, len(line[3]))

    for i in range(number):
        for j in range(4):
            print
            out[i][j].rjust(spaces, ' '),
        print

#Alphabet Rangoli
def print_rangoli(size):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'[0:size]
    for a in range(size - 1, -size, -1):
        c = abs(a)
        line = alphabet[size:c:-1] + alphabet[c:size]
        print('--' * c + '-'.join(line) + '--' * c)

#Capitalize!
def solve(s):
    for n in s.split():
        s = s.replace(n, n.capitalize())
    return s

#The Minion Game
def minion_game(string):
    # your code goes here
    vocals = 'AEIOU'
    k_score = 0
    s_score = 0
    for i in range(len(s)):
        if s[i] in vocals:
            k_score += len(s) - i
        else:
            s_score += len(s) - i

    if s_score > k_score:
        print('Stuart', s_score)
    elif k_score > s_score:
        print('Kevin', k_score)
    else:
        print('Draw')

#sWAP cASE
def swap_case(s):
    out = ''
    for i in s:
        if i.isupper():
            out+=i.lower()
        else:
            out+=i.upper()
    return out

#Merge the Tools
def merge_the_tools(string, k):
    i=0
    while i<len(string):
        a = string[i:i+k]
        out = ''
        for c in a:
            if c not in out:
                out += c
        print out
        i+=k

#Introduction to Sets
def average(array):
    s = sum(set(array))
    l = len(set(array))
    return s/l

#Symmetric Difference
x = int(raw_input())
a = raw_input().split()
y = int(raw_input())
b = raw_input().split()

s1 = set(a)
s2 = set(b)

f1 = s1.difference(s2)
f2 = s2.difference(s1)

final = f1.union(f2)

print ('\n'.join(sorted(final, key=int)))

#Set.add()
n = int(input())
s = set()

for i in range(n):
    s.add(input())

print(len(s))

#Set.discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))

l = int(input())

for i in range(l):
    func = input().split(' ')
    if func[0] == 'pop':
        s.pop()
    elif func[0] == 'remove':
        s.remove(int(func[1]))
    elif func[0] == 'discard':
        s.discard(int(func[1]))
print(sum(s))

#Set .union() Operation
n1 = int(input())
s1 = set(map(int, input().split(' ')))
n2 = int(input())
s2 = set(map(int, input().split(' ')))

print(len(s1.union(s2)))

#Set .intersection() Operation
n1 = int(input())
s1 = set(map(int, input().split(' ')))
n2 = int(input())
s2 = set(map(int, input().split(' ')))

print(len(s1.intersection(s2)))

#Set .difference() Operation
n1 = int(input())
s1 = set(map(int, input().split(' ')))
n2 = int(input())
s2 = set(map(int, input().split(' ')))

print(len(s1.difference(s2)))

#Set .symmetric_difference() Operation
n1 = int(input())
s1 = set(map(int, input().split(' ')))
n2 = int(input())
s2 = set(map(int, input().split(' ')))

print(len(s1.symmetric_difference(s2)))

#Set Mutations
a = input()

set_A = set(map(int, input().split()))
N = int(input())

for i in range(N):
    cmd = input().split()[0]
    s = set(map(int, input().split()))

    if cmd == 'update':
        set_A.update(s)
    elif cmd == 'intersection_update':
        set_A.intersection_update(s)
    elif cmd == 'difference_update':
        set_A.difference_update(s)
    elif cmd == 'symmetric_difference_update':
        set_A.symmetric_difference_update(s)

print(sum(set_A))

#The Captain Room
n = int(input())

l = list(map(int, input().split()))
dict_l = {}
for i in l:
    if i not in dict_l:
        dict_l[i] = 1
    elif i in dict_l:
        dict_l[i] += 1
for i in l:
    if dict_l[i] == 1:
        print(i)

#Check Subset
t = int(input())
for i in range(t):
    n_a = input()
    a = set(input().split())
    n_b = input()
    b = set(input().split())
    print(a.issubset(b))

#Check Strict Superset
a = set(input().split())
n = int(input())
for i in range(n):
    b = set(input().split())
    if a.issuperset(b):
        print(True)
        break
    else:
        print(False)
        break

#No Idea
n, m = input().split()

my_arr = input().split()
my_happ = 0

a =  set(input().split())
b = set(input().split())
for i in my_arr:
    if i in a:
        my_happ += 1
    if i in b:
        my_happ -= 1
print(my_happ)

#Polar Coordinates
import cmath

c = complex(input())
print(abs(c))
print(cmath.phase(c))

#Find Angle MBC
import math

a_b = int(input())
b_c = int(input())

m_c = math.sqrt(a_b**2 + b_c**2)/2
b = b_c/2
angle = str(int(round(math.degrees(math.acos(b/m_c)))))

print(angle+chr(176))

#Triangle Quest 2
for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(int(((10**i-1)/9)**2))

#Mod DIVMOD
import math

a = int(input())
b = int(input())

print(a//b)
print(a%b)
print(divmod(a, b))

#Power Mod-Power
a = int(input())
b = int(input())
c = int(input())

print(pow(a, b))
print(pow(a, b, c))

#Integers Come in All sizes
a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(pow(a, b) + pow(c, d))

#Triangle Quest
for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print((10**(i)//9)*i)

#collections.Counter()
from collections import Counter

x = int(input())
sizes = Counter(map(int, input().split()))
n = int(input())

earned = 0
for i in range(n):
    s, p = map(int, input().split())
    if sizes[s]:
       earned += p
       sizes[s] -= 1
print(earned)


#PROBLEM 2

#Birthday Cake Candles
# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    max_c = max(candles)
    count = 0
    for i in candles:
        if i == max_c:
            count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


#Number Line Jumps
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if(v1 > v2):
        if((x2 - x1) % (v2 - v1) == 0):
            return("YES")
        else:
            return("NO")
    else:
        return("NO")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


#Viral Advertising
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    tot = 0
    shar = 5
    for i in range(n):
        likes = shar//2
        tot += likes
        shar = likes * 3
    return tot

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()


#Recursive Digit Sum
# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

# I build a function that return the sum of the digits of n, so the code is easier to read and to apply
def check(n):
    if n < 10:
        return n
    else:
        tot = sum([int(i) for i in str(n)])
        return check(tot)
        # return the single digit


def superDigit(n, k):
    # Write your code here
    out = k * check(int(n))
    return check(out)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()


#Insertion Sort - Part 1
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    pivot = arr[-1]
    pos = n - 1
    while pos > 0 and pivot < arr[pos - 1]:
        arr[pos] = arr[pos-1]
        print(*arr)
        pos -= 1
    arr[pos] = pivot
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


#Insertion Sort - Part 2
# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Write your code here
    for i in range(1, n):
        pivot = arr[i]
        j = i
        while j > 0 and pivot < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = pivot
        print(*arr)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
