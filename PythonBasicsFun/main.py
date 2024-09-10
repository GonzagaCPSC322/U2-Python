import csv
import copy

import hello_world



# warm up task
# Write a for loop to print the first 20 even numbers all on one line 
# separated by a comma and a space (e.g. 2, 4, ..., 38, 40)
for i in range(2, 42, 2):
    if i == 40:
        print(i)
    else:
        print(i, end=", ")

# LISTS
# are like vectors in C++
# can grow/shrink size
# they can have mixed types
# lists are objects
fibs = [1, 1, 2, 3, 5, 8]
print(fibs, type(fibs))
print(fibs[0], fibs[-1])

for val in fibs:
    print(val, end=" ")
print()
for i in range(len(fibs)):
    print(i, ":", fibs[i], end=" ")
print()
for i, val in enumerate(fibs):
    print(i, ":", val, end=" ")
print()

# built in functions
# sum(), min(), max(), len(), sorted(), etc.
print(sorted(fibs, reverse=True)) # sorts a copy

# list methods
# method invocation syntax: <object>.<method>()
# fibs.sort(reverse=True) # sorts fibs in place
# print(fibs)
print(fibs.index(5))
fibs.pop(4)
print(fibs)
fibs.insert(4, 5)
print(fibs)
fibs.remove(8)
print(fibs)
fibs.append(8)
print(fibs)

# 2D lists (AKA nested list)
def pretty_print(table):
    for row in table:
        for value in row:
            print(value, end=" ")
        print()
    print()

matrix = [[0, 1, 2], [3, 4, 5]]
print(matrix[0], matrix[0][1])
pretty_print(matrix)

# FILE IO
# often we want to open a file and read its contents into memory
# lets start with a CSV (comma separated value)
def convert_to_numeric(values):
    for i in range(len(values)):
        try:
            numeric_val = float(values[i])
            # success if here
            values[i] = numeric_val
        except ValueError as e:
            # failure to convert
            print(e)

def load_table(filename):
    table = []
    # 1. open the file
    infile = open(filename, "r")
    # 2. process the file
    # lets use the csv module to read the rows from the file
    reader = csv.reader(infile)
    for row in reader:
        # TASK: use a try/except block to convert
        # strings to numeric type appropriately
        convert_to_numeric(row)
        print(row)
        table.append(row)
    # 3. close the file
    infile.close()
    return table

def write_table(table, filename):
    outfile = open(filename, "w")
    writer = csv.writer(outfile)
    writer.writerows(table)
    outfile.close()

table = load_table("data.csv")
print(table)
write_table(table, "data_copy.csv")

# ASSERTS
# assert statements "assert" that something is true
# if the statement evalues to true, then execution continues
# if the statement evaluates to false, the execution stops (crashes)
assert 3 == 3
print("after assert")

# use assert statements to write unit tests
# a unit test is a function that tests another function for functional correctness
# a unit test is comprised of one or more test cases
# the test cases should cover common/simple input/output pairs (e.g. happy path)
# plus rare/complex input/output pairs (e.g. edge cases)
# the order of assert statement operands
# actual (what code produced) vs expected (solution)
# ex: remove_missing_values(...) == [[], ...]

# PYTHON IS PASS BY OBJECT REFERENCE
# this means that object references are passed by value (copied)
# for more details: https://robertheaton.com/2014/02/09/pythons-pass-by-object-reference-as-explained-by-philip-k-dick/

# TASK: define/call a function add_one(table) that accepts a reference
# to a 2D list of numbers and adds 1 to every single element
def add_one(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            table[i][j] += 1

def clear_out(table):
    table = []

print("matrix before:", matrix)
add_one(matrix)
print("matrix after:", matrix)

print("matrix before:", matrix)
clear_out(matrix)
print("matrix after:", matrix)

# COPIES
# shallow copy: copies the references, not the objects
matrix_copy = matrix.copy()
print("matrix before:", matrix)
print("matrix_copy before:", matrix_copy)
add_one(matrix)
print("matrix after:", matrix)
print("matrix_copy after:", matrix_copy)
# deep copy: copies the objects themselves
matrix_deep_copy = copy.deepcopy(matrix)
print("matrix before:", matrix)
print("matrix_copy before:", matrix_copy)
print("matrix_deep_copy before:", matrix_deep_copy)
add_one(matrix)
print("matrix after:", matrix)
print("matrix_copy after:", matrix_copy)
print("matrix_deep_copy after:", matrix_deep_copy)

# CLASSES
# class: a collection of state and behavior that completely describes something
# object: an instance of a class
class Subject:
    """Represents a human subject in a research study.

    Attributes:
        sid(int): a unique subject id
        name(str): the subject's name
        measurements(dict of string:float): timestamp:value recordings
            for this subject's measurements in the study
    
    """