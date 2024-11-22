n = int(input("no of integers: "))

array = list(map(int, input("enter elements separated by space: ").strip().split()))

sum = 0

for i in array:

    if i > 0:
        sum += i

print(sum)
