import csv

import hello_world

# warm up task
# 2, 4, ...., 38, 40
for i in range(2, 40, 2):
    print(i, end=", ")
print(i + 2)

# LISTS
# are like arrays
# grow and shrink in size
# have mixed types
# lists are objects
fibs = [1, 1, 2, 3, 5, 8]
print(fibs, type(fibs))

# for loop demos
for value in fibs:
    print(value)
for i in range(len(fibs)):
    print(i, ":", fibs[i])
for i, value in enumerate(fibs):
    print(i, ":", value)

# negative indexes
print(fibs[-1])

# built in list functions
# len(), sum(), min(), max(), sorted(), etc.
# sorted() returns a copy of the list argument sorted
print(sorted(fibs, reverse=True))
print(fibs)

# list methods
# recall: method invocation syntax <object name>.<method name>()
print(fibs.index(5))
fibs.append(13)
print(fibs)
fibs.pop(-1)
print(fibs)
fibs.remove(5)
print(fibs)
# inplace sort of a list
fibs.sort(reverse=True)
print(fibs)

# nested lists (AKA 2D list AKA tables)
matrix = [[0, 1, 2], [3, 4, 5]]
print(matrix)
# TASK: define/call a function called pretty_print(table)
# that prints out a table in a nice 2D grid like format
# 0 1 2
# 3 4 5
def pretty_print(table):
    for row in table:
        for value in row:
            print(value, end=" ")
        print()

# call
pretty_print(matrix)

# FILE IO
# we often want to open a file and read its contents
# into program memory
# lets start with CSV (comma separated value) format
def convert_to_numeric(values):
    # values is a 1D list of values to attempt to
    # convert to a numeric type
    for i in range(len(values)):
        try:
            numeric_val = float(values[i])
            # success
            values[i] = numeric_val
        except ValueError as e:
            print(e)


def read_table(filename):
    table = []
    # 1. open
    infile = open(filename, "r")

    # 2. read/write (process)
    # we can write our own CSV parsing
    # algorithm (BONUS PA1)
    # instead use the csv module (standard library)
    reader = csv.reader(infile)
    for row in reader:
        print(row)
        # we need to convert numeric values from string
        # to a numeric type
        convert_to_numeric(row)
        print(row)
        table.append(row)

    # 3. close
    infile.close()

    return table

def write_table(table, filename):
    outfile = open(filename, "w")
    writer = csv.writer(outfile)
    writer.writerows(table)
    outfile.close()

table = read_table("data.csv")
print(table)
# TASK: define/call write_table()
write_table(table, "data_copy.csv")