
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
    # my_finallist = [i for j, i in enumerate(a) if i not in a[:j]]
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
    first  = second = 100 #max value
    for i in range(0,len(a)):
        #print(a[i])
        if a[i] < first:
            second = first
            first  = a[i]
        if a[i] != first and a[i] < second:
            second = a[i]
    print(first,second) 

def check_prime_number():
    a = 29
    flag = 0
    i = 2 
    length = a // 2
    while i <= length:
        print(i)
        if a % i == 0:
            flag = 1
        i+=1
    if flag == 1:
        print("Given number is not a prime no.")
    else:
        print("Given number is prime no")

def count_distinct_element():
    arr = [6, 10, 5, 4, 9, 120, 4, 6, 10]      
    # hashset
    s = set()
    count = 0
    for i in arr:
        if i not in s:
            s.add(i)
            count+=1
    print(count)

def bubble_sort():
    arr = [64, 34, 25, 12, 22, 11, 90]
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print(arr)

def find_pair_sum():
    arr = [1, 4, 45, 6, 10, 8]
    n = 16
    s = set()
    for i in range(len(arr)):
        temp = n - arr[i]
        if temp in s:
            print(n,temp,arr[i])
        s.add(arr[i])

find_pair_sum()

#bubble_sort()
#count_distinct_element()
#check_prime_number()
#find_first_two_small_number()
#infinite_loop()
#separate_uniq_element()
#convert_dict()

