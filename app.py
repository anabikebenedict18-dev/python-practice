import random
num = random.randint(1,100)
for _ in range(10):
    g = int(input("Guess: "))
    if g == num: print("Correct"); break
    print("High" if g > num else "Low")
else:
    print("Number was", num)