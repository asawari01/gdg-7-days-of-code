a = -1    

while (a < 0):
    a = int(input("enter a positive integer: "))
    
b = int(input("enter an integer greater than previous one: "))

for i in range(a, b+1):

    if (i % 5 == 0) and (i % 7 == 0):
        print("FooBar")
    elif (i % 5 == 0) and (i % 7 != 0):
        print("Foo")
    elif (i % 5 != 0) and (i % 7 == 0):
        print("Bar")
    else:
        print("Baz")



