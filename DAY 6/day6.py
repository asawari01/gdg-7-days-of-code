inp = input("Enter a string: ")

v = inp.lower()
all_vowels = 0

for x in v:
    
    if x == 'a' or x == 'e' or x == 'i' or  x == 'o' or x == 'u':
        all_vowels +=1


print(all_vowels)