number = []

for i in range(10):
    num = int(input("enter 10 numbers"))
    number.append(num)

for a in number:
    if a % 2 == 0:
        print("these are even numbers", a)
    else:
        print("these are odd numbers", a)
