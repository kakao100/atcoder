k = int(input())
n = input()

if(k < len(n)):
    print(n[:k]+"...")
else:
    print(n)