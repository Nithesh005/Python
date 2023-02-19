def simple_tuple():
    thistuple = ("apple", "banana", "cherry", "apple", "cherry")
    print(thistuple)
def access_tuples():
    thistuple = ("apple", "banana", "cherry")
    print(thistuple[1])    
def update_tuple():
    thistuple = ("apple", "banana", "cherry")
    y = list(thistuple)
    y[1] = "pine apple"
    x = tuple(y)
    print(x)
def unpacking_tuples():
    fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
    (red,*green,blue) = fruits
    print(red)
    print(green)
    print(blue)
def loop_tuples():
    thistuple = ("apple", "banana", "cherry")
    for x in thistuple:
        print(x)
def join_tuples():
    tuple1 = ("a", "b" , "c")
    tuple2 = (1, 2, 3)
    tuple3 = tuple1 + tuple2
    print(tuple3)

simple_tuple()
access_tuples()
update_tuple()
unpacking_tuples()
loop_tuples()
join_tuples()

# ******************* tuple methods ******************************
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found