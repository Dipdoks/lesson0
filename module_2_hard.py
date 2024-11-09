import random
def lottery():
    numbers = range(3,21)
    win = random.choice(numbers)
    return win
n = lottery()
string = ''
for i in range(1, n):
    for j in range(i + 1, n):
        if n % (i + j) == 0:
            string = string + str(i) + str(j)
print(n, '-', string)