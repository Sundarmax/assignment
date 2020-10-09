# Python closure example
def print_msg_ex1(msg):
    
    def printer():
        print(msg)
    printer()

# print_msg("hello")

# Defining a closure function.
def print_msg(msg):
    
    def printer():
        print(msg)
    return printer

#a = print_msg("hello")
#print(a)
#a()
# By default read only permission given to non local variables. 
num = 90

def outside_fun():
    num = 80
    b   = 100
    
    def inner_fun(): # Read 
        print(num)
    
    def inner_fun2() : # write 
        nonlocal b
        b = 101
    print(b)
    inner_fun()
    inner_fun2()
    print(b)

#outside_fun()

def sort_priority(values,groups):
    def helper(x):
        print(x)
        if x in groups:
            return(0,x)
        return (1,x)
    values.sort(key=helper)

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group   = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)