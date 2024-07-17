import sys


slowo = "kajak" #input("Jakie slowo chcesz sprawdzic? ")
same = 0
for i in range(len(slowo)):
    if slowo[i] == slowo[-i-1]:
        print('yes')
        same +=1
    else:
        print('no')
    print("-------")

if same == len(slowo):
    print(f"{slowo} jest palindromen")

print("Zmiany")
