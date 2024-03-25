# First method of initializing decorator
"""
sum = 0
def f_decorator(f1):
    global sum
    def wrapper():
        result = f1()
        #Decorating function f1()
        print(f"I love you {sum}")
        return result
    return wrapper

@f_decorator
def f1():
    global sum
    for _ in range(20):
        sum += _
    return sum

f1()
number = 0
"""
#Second method of initializing decorator
"""
def decorator(function):
    def wrapper2():
        res = function(num)
        list2 = [i for i in range(res)]
        list3 = list(map(lambda x: x ** 2, list2))
        return list3
    return wrapper2

function2(num)
func = decorator(function2)
print(func())
"""
# Use of recursion function
"""
num = int(input())
def function2(num):
    if num % 10 != 0:
        function2(num + 1)
    return num
"""
# Finding missing elements in set
"""
nums = [1,4,2]
missing_numbers = []
nums_set = set(nums)

for i in range(1, 4 + 1):
    if i not in nums_set:
        missing_numbers.append(i)
        
print(missing_numbers)
"""
#Следующий декоратор @debug будет выводить аргументы,
#с которыми вызвана функция, а также возвращаемое функцией значение:
"""
import math
def debug(func):
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]    
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Вызываем {func.__name__}({signature})")
        value = func(*args)
        print(f"{func.__name__!r} возвращает {value!r}")
        return value
    return wrapper_debug


math.factorial = debug(math.factorial)

def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))

approximate_e()
"""
#Using module Collections for special variable -
# defaultdict (missing keys set to int 0 )
"""
from collections import defaultdict
d = defaultdict(int)
dic = {}
d[1] = 1
d[2] = 2
#print(d[3])
# print(d[1])
# print(dic['1'])
"""
#Using module itertools for function cycle -
#   will iterate infinitely iterable object
"""
from itertools import cycle
colors = cycle(['red','b','c'])
for i in range(4):
    print(next(colors))
"""
# Using module DATETIME to create variables of type datetime and
    # find time difference
"""
from datetime import datetime
start_datetime = datetime(2023, 5, 30, 10, 0, 0)
end_datetime = datetime(2023, 5, 31, 15, 30, 0)
time_difference = end_datetime - start_datetime
print("Time Difference:", time_difference)
"""
#Uses of module random
"""
import random
def ranfomCH(letter):
    res = "".join(random.choice(letter) for i in range(5))
    print(res)
# Different variant
def shuffle(abc):
    shufffleCG = random.sample(abc, 5)
    shufffleSTR = "".join(shufffleCG)
    print(shufffleSTR)
abc = input()
shuffle(abc)
ranfomCH(abc)

"""
# Usage of module OS for working with files
"""
import os
start_path = os.getcwd()
print(start_path)
os.chdir("..")
print(os.getcwd())
print(os.path.join(start_path, 'test'))
FileLocation = os.path.join(os.getcwd(), "test.txt")
"""
# Automatic closing of file outside usage zone:
"""
with open(FileLocation, "r") as f:
    a = f.read(4)
    b = f.readlines(1)
print(a, b)
"""
# Usage of PANDAS as pd
"""
import pandas as pd
file_path = "example.txt"
new_file_path = "ex.txt"
#Reading csv or excel
df_csv = pd.read_csv(file_path)
df_xlsx = pd.read_excel(file_path)
    #Запись in csv or excel
df_csv.to_csv(new_file_path)
df_xlsx.to_excel(new_file_path)
"""
# Functions to manipulate files
import os
os.getcwd()
os.chdir("..")
FileLocation = os.path.join(os.getcwd(), "test.txt")
"""
def data_shape(file_path):
    file = pd.read_excel(file_path)
    return file.shape # shape -> determines file size = rows and columns
            # shape returns tuple[iter.] can't be modified

def row_col_nums(file_path):
     f = pd.read_excel(file_path)
     rows = f.shape[0]
     cols = f.shape[1]
     return f"Rows = {rows}, columns = {cols}"
     
def read_file(file_path):
    lines = []
    with open(file_path, "r") as f:
        for line in f:
            if len(line.strip()) >= 5:
                lines.append(line.strip())
        return lines

g = read_file(FileLocation)
print(g)

def read_file_step(file_path, n):
    lines = []
    with open(file_path, 'r') as file:
        lines = file.readlines() # readlines -> read ALL lines in file, adding them into list
        lines = [line.strip() for line in lines]
        some = [v for i, v in enumerate(lines) if i % 3 == 0]
    return some
g1 = read_file_step(FileLocation, 3)
print(g1)

def min_max_avg_line(file_path):
    avarages  =[]
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            avarages.append(len(line.strip()))
        avg = round(sum(avarages) / len(lines), 1)
    return max(lines, key = len), min(lines, key = len), avg
print(min_max_avg_line(FileLocation))

def data_cols(file_Name):
    df = pd.read_excel(file_Name)
    return df.columns # method columns returns names of columns

def read_file_char(FileLocation, n):
    with open(FileLocation, 'r') as file:
        f = file.readlines()
        beta = [line.replace(" ", "") for line in f]
        lines = [line.strip() for line in beta if len(line.strip()) <= n]
    return lines

print(read_file_char(FileLocation, 10))

def longest_words(FileLocation):
    with open(FileLocation, "r") as file:
        lines = file.read().split()
        letter = 0
        long_words = []
        words = [len(word.strip()) for word in lines]
        for el in words:
            if len(el) > letter:
                letter = len(el)
                long_words = [el]
            elif len(el) == letter:
                long_words.append(el)
        return letter, long_words
print(longest_words(FileLocation))

# text_stats returns number of letters, words and lines/ letters are checked on being alphabetical letter
def text_stats(FileLocation):
    with open(FileLocation, 'r') as file:
        f = file.read()
        words = len(f.split())
        lines = f.count("\n") + 1
        char = []
        for i in f:
            if i.isalpha():
                char.append(i)
        letters = len(char)
        return letters, words, lines

#alpha_lines returns lines without numbers
def alpha_lines(FileLocation):
    with open(FileLocation, 'r') as file:
        lines = file.readlines()
    alphalines = []
    for line in lines:
        line = line.strip()
        if line.replace(' ','').isalpha():
            alphalines.append(line)
    return alphalines

# replace_string finds word1 in sentence and replaces it with word2, then writes modified sentence
def replace_string(FileLocation):
    with open(FileLocation, 'r') as file:
        word1 = file.readline().strip()
        word2 = file.readline().strip()
        line = file.read()
    replaced_line = line.replace(word1, word2)
    with open(FileLocation, 'w') as file:
        file.write(replaced_line)
"""