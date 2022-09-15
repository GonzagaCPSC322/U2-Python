import csv
import copy

# subject.py with Subject
# import subject
# subject.Subject
# from subject import Subject
# Subject

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

# warm up task
def add_one(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            table[i][j] += 1

print("matrix before:", matrix)
add_one(matrix)
print("matrix after:", matrix)

def clear_out(table):
    table = []

print("matrix before:", matrix)
clear_out(matrix)
print("matrix after:", matrix)

# PYTHON IS PASS BY OBJECT REFERENCE
# object refernces are passed by value (copied)
# for more details: https://robertheaton.com/2014/02/09/pythons-pass-by-object-reference-as-explained-by-philip-k-dick/

# SHALLOW VS DEEP COPY
# shallow copy copies the object references not the objects themselves
matrix_copy = matrix.copy() # shallow copy
# deep copy copies the objects themselves
matrix_deep_copy = copy.deepcopy(matrix) # deep copy

print("matrix before:", matrix)
print("matrix_copy before:", matrix_copy)
print("matrix_deep_copy before:", matrix_deep_copy)
add_one(matrix)
print("matrix after:", matrix)
print("matrix_copy after:", matrix_copy)
print("matrix_deep_copy after:", matrix_deep_copy)

# you probably want a deep copy

# CLASSES
# class: a collection of state and behavior that completely
# describes something
# object: an instance of a class
class Subject:
    """Represent a human subject in a research study.

    Attributes:
        sid(int): unique id number for the subject
        name(str): name of the subject
        measurements(dict or str:float): stores the timestamp:value
            measurements collected from the subject during
            the study

        num_subjects(int): class-level attribute storing
            the total number of subjects in the study
    """
    # declare your class-level attributes here
    num_subjects = 0
    # one num_subjects variable that is shared amongst all
    # Subject objects
    # do not declare instance-level attributes here

    # special method __init__(self)
    # like a constructor
    def __init__(self, name, measurements=None):
        # self is like the this reference
        # self is a reference to the "current" or
        # "invoking" object
        self.sid = Subject.num_subjects
        Subject.num_subjects += 1
        self.name = name
        if measurements is None:
            measurements = {}
        self.measurements = measurements
    
    # special method __str__
    # invoked whenever a string represntation of
    # an object is needed
    def __str__(self):
        return "SID: " + str(self.sid) + " NAME: " + self.name + \
            " MEASUREMENTS: " + str(self.measurements)

    # let's define our own instance-level method
    def record_measurement(self, timestamp, value):
        # should do error checking...
        self.measurements[timestamp] = value
    
    # let's define our own class-level method
    def display_num_subjects():
        print("Number of subjects:", Subject.num_subjects)

# lets create some Subject objects
sub1 = Subject("cassidy")
print(sub1)
print(sub1.__str__())
sub1.record_measurement("09-15-2022 10:21:00.00am", 1.1)
print(sub1)
print(sub1.measurements)

sub2 = Subject("conan")
print(sub2)
Subject.display_num_subjects()

# ASSERT STATEMENTS
# assert something is true or false
# if the assert statement evaluates to true, 
# then execution continues
# if the assert statement evaluates to false,
# then execution stops
assert 4 == 3
print("here")

# use assert statements to write unit tests
# a unit test is a function that tests another function
# for functional correctness
# unit tests are comprised of several test cases
# ranging from simple (e.g. common example, "happy path" example)
# to complex (e.g. rare example) to edge cases 

# assert statement operand ordering
# actual vs expected (solution)