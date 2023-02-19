def list_comprehension():
    # list comprehension
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    newfruits = []
    for x in fruits:
        if "a" in x:
            newfruits.append(x)

    print(newfruits)

    # short-hand
    print([x for x in fruits if "b" in x])
    print([x.upper() for x in fruits])
    print([x for x in range(10)])
list_comprehension()

# Sort List Alphanumerically *********************
def Alphanumeric():
    fruits_list1 = ["kiwi", "banana", "cherry", "apple", "mango"]
    fruits_list1.sort()
    print(fruits_list1)
    fruits_list1.sort(reverse=True)
    print(fruits_list1)
Alphanumeric()

# customize_sort *******************************
def customize_sort():
    def myfun(n):
        return abs(n-50)
    arr = [100, 50, 65, 82, 23]
    arr.sort(key = myfun)
    print(arr)
customize_sort()

def copy_list():
    thislist = ["apple", "banana", "cherry"]
    mylist = thislist.copy()
    print(mylist)
copy_list()

def extend_list():
    list1 = ["a", "b" , "c"]
    list2 = [1, 2, 3]
    list1.extend(list2)
    print(list1)
extend_list() 
