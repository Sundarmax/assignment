
import sys
import copy
def convert_dict():
    a = [1,2,3,4]
    b = [5,6,7,8]
    index = 0
    new_dict = {} 
    while index < len(a) and index < (len(b)):
        new_dict.update({a[index]:b[index]})
        index+=1
    print(new_dict)


def separate_uniq_element():
    a = [1,2,3,4,5,6,1,2,3,4]
    # with using inbuild lib
    # a = set(a)
    # print(a)
    # with using separate list 
    uniq_list = []
    for item in a:
        if item not in uniq_list:
            uniq_list.append(item)
    print("Unique list",uniq_list)
    # without using separate list so we can use inbuild lib.
    my_finallist = [i for j, i in enumerate(a) if i not in a[:j]]
    #print(my_finallist)
    result = [i for index,i in enumerate(a) if i not in a[:index]]
    print(result)

def infinite_loop():
    a = [1,2,3,4]
    for i in a:
        a.append(i*i)
    print(a)

def find_first_two_small_number():
    a = [1,3,4,7,2]
    first  = second = 100
    for i in range(0,len(a)):
        #print(a[i])
        if a[i] < first:
            second = first
            first  = a[i]
        if a[i] != first and a[i] < second:
            second = a[i]
    print(first,second) 

def copy_in_python():
    a = [1,2,4]
    b = a
    # shallow copy
    print('--shallow copy--') 
    print(id(a))
    print(id(b))
    a[0] = 0 # [0,2,4]
    print(a,b)
    print('--deep copy--')
    c = copy.deepcopy(a)
    print(id(a)) 
    print(id(c)) #Independent object
    a[0] = 3
    print(a,c)

class Student:
    
    count = 0

    def __init__(self):
        Student.count +=1

obj1 = Student()
obj2 = Student()

def onezeros(r,c):
    for i in range(r):
        for j in range(c):
            if j % 2 == 0:
                print('1',end=' ')
            else:
                print('0',end=' ')
        print()

def get_list_input():
    a = [int(i) for i in input().split()]
    print(a)

def count_vowels():
    vowel = ['a','e','i','o','u']
    s_input = "SUNDAR"
    s_input =  s_input.lower()
    count = 0
    for char in s_input:
        if char in vowel:
            count+=1
    print(count)

def count_word():
    test_string = "Geeksforgeeks is best Computer Science Portal"
    # printing original string 
    print ("The original string is : " +  test_string) 
    # using split() 
    # to count words in string 
    res = len(test_string.split()) 
    # printing result 
    print ("The number of words in string are : " +  str(res)) 
    print ("length of the string is : ",len(test_string) ) 
count_word()

#count_vowels()
#get_list_input()
#r,c = input().split()
#onezeros(int(r),int(c))
#print("No of objects created for the class : ",Student.count)
#copy_in_python()
#find_first_two_small_number()
#infinite_loop()
#separate_uniq_element()
#convert_dict()

