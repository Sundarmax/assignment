
import sys

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


find_first_two_small_number()

#infinite_loop()
#separate_uniq_element()
#convert_dict()

