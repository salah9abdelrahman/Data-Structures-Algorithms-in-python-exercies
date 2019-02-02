#1.12 Exercises
# It's what I could solve from it.

# R-1.3
def minmax(data):
    smallest = data[0]
    largest = data[0]
    for n in data:
        if n < smallest:
            smallest = n
        if n > largest:
            largest = n
    return smallest,largest

print(minmax((3,2,9,8,1,4)))

# R-1.4
def sum_squares(n):
    sum = 0
    for k in range(n):
        sum += k ** 2
    #     or sum += k*k
    return sum

print(sum_squares(10))


# R-1.5
print(sum(k**2 for k in range(10)))

# R-1.6
def sum_square_odd(n):
    sum = 0
    for k in range(n):
        if k % 2 != 0:
            sum += k**2
    return sum

print(sum_square_odd(10))

# R-1.7
print(sum(k**2 for k in range(10) if k %2 != 0))

# R-1-9
for x in range(50,81,10):
    print(x)

# R-1.10
for x in range(8,-9,-2):
    print(x)

# R-1.11
print([2**n for n in range(9)])

# c-1.13
def reverse(data):
    temp = []
    n = len(data) - 1
    for thing in range(n, -1, -1):
        temp.append(data[thing])
    return temp

any_list = [1,2,3,4]
print(reverse(any_list))

# c-1.14
# first check if there are pairs that the product of them is odd or not
def product_pair_odd_t_or_f(alist):
    odd_list = 0
    for x in alist:
        for y in alist:
            if (x * y) % 2 != 0:
                odd_list += 1
    return True if odd_list > 0 else False

any_list = [2,4]
print(product_pair_odd_t_or_f(any_list))

# second print the numbers
def product_pair_odd(alist):
    odd_list = []
    for x in alist:
        for y in alist:
            if (x * y) % 2 != 0:
                odd_list.append((x,y))
    return odd_list

any_list = [2,3,4,5]
print(product_pair_odd(any_list))

# c-1.15
def is_all_different(alist):
    count = 0
    for x in range(len(alist)):
        for y in range(len(alist)):
            # to not loop in the same number in the same time
            if x == y:
                break
            elif alist[x] == alist[y]:
                count += 1
    return 'They all different' if count == 0 else 'there is a similarity'

any_list = [1,2,3,4]
print(is_all_different(any_list))

# c-1.18
print([x*(x+1) for x in range(10)])

# c-1.19
print([chr(k) for k in range(97, 123)])
# another solution
import string
print(list(string.ascii_lowercase))

# c-1.23
alist = [1,2,3]
try:
    alist[3]= 3
except IndexError:
    print('Don’t try buffer overflow attacks in Python!')

# c-1.24
def how_many_vowels(astring):
    count_vowels = 0
    for n in astring:
        if n == 'a' or n == 'i' or n== 'o' or n== 'e' or n == 'u':
            count_vowels += 1
    return count_vowels

print(how_many_vowels('salah'))

# c-1.25
def remove_punctuation (astring):
    without_punctuation = []
    for n in astring:
        if not n == "'" or n == ',' or n == '.':
            without_punctuation.append(n)
    return ''.join(without_punctuation)

print(remove_punctuation("Let's try, Mike."))

# P-1.29 not all words
alist = ['c', 'a', 't', 'o', 'g']

for x in range(len(alist)):
    word = [alist[x]]
    for y in range(len(alist)):
        if x == y:
            continue
        else:
            word.append(alist[y])
    print(''.join(word))


# p-1.30
x = float(input('Enter number greater than 2: '))
count = 0
while x > 2:
    x = x / 2
    count += 1
print(count)

# p-1.31
first_num = float(input('enter first num: '))
opertaor = input('enter operator: ')
second_num = float(input('enter second num: '))
if opertaor == '+':
    print(first_num + second_num)

if opertaor == '-':
    print(first_num - second_num)

if opertaor == '*':
    print(first_num * second_num)

if opertaor == '/':
    print(first_num / second_num)

# p-1.33
stop = 'exit'
out = input('when you want to stop the program, write exit\n if not click enter').lower()
while stop not in out:
    first_num = float(input('enter first num: '))
    opertaor = input('enter operator: ')
    second_num = float(input('enter second num: '))
    if opertaor == '+':
        print(first_num + second_num)

    if opertaor == '-':
        print(first_num - second_num)

    if opertaor == '*':
        print(first_num * second_num)

    if opertaor == '/':
        print(first_num / second_num)
    out = input('enter exit to stop').lower()

# p-1.34
# write a sentence 100 times and the number of the sentences
# every sentence should have 8 different typos
import random
import string
for x in range(1,101):
    typo = random.choice(string.ascii_lowercase)
    sentence = list("I will never spam my friends again.")
    for n in range(9):
        y = random.randint(0, len(sentence) - 1)
        sentence[y] = typo
    print(f"This is sentence number: {x}, {''.join(sentence)}")

# p-1.35
import random
n = int(input('Enter by number How many people in the room'))
people_have_same_bd = 0
for n in range(n):
    x = random.randint(1, 30), random.randint(1, 12)
    y = random.randint(1, 30), random.randint(1, 12)
    if x == y:
        people_have_same_bd += 1
print(people_have_same_bd)

# p-1.36
list_of_words = 'hey dude this is the last project, bye dude'
alist = list_of_words.split(' ')
count = 0
for n in range(len(alist)):
    for x in range(len(alist)):
        if n == x:
            continue
        elif alist[n] == alist[x]:
            count += 1

print(count)





