import csv

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
matrix = [[0, 1, 2], [3, 4, 5]]
print(matrix[0], matrix[0][1])

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

table = load_table("data.csv")
print(table)