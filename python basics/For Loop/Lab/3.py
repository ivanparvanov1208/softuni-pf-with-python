n = int(input())

for i in range(0, n + 1):
    if i % 2 == 0:
        raisedNumber = 2 ** i
        print(raisedNumber)