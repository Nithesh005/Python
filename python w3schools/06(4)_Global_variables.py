x = "nithi"

def myfun():
    global x    # Global value
    x="jennie"
    print("welcome "+x)

myfun()
print(x)