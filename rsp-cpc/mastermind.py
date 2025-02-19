n = input()
numbers = set()
for i in range(int(n)):
    temp = input()
    num, is_divisible = temp.split(" ")
    num = int(num)
    counter = 0
    while counter <= 100:
        counter += num
        if is_divisible == "y":
            numbers.add(counter)
print(numbers)    