
n = int(input("enter no. of rows: "))

for i in range(n):

    #print spaces
    for x in range(n-i-1):
        print(" ", end=" ")

    #print stars
    for x in range(0,(2*i)+1):
        print("*", end=" ")

    print()



