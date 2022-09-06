# this is a one line comment

"""
this is 
a
multi line comment
"""

print("hello world:", __name__)

# 2 ways to run a python file (AKA module)
# 1. directly
# e.g. python hello_world.py
# the __name__ special variable stores "__main__"
# 2. by importing it from another module
# e.g. in main.py I have a import hello_world
# the __name__ variable in hello_world.py stores "hello_world"

def main():
    print("hello from hello_world.main()")

if __name__ == "__main__":
    main()