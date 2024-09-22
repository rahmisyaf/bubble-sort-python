import random

user_numbers_length = int(input("enter the length of your array : "))
min_range = int(input("enter the min range : "))
max_range = int(input("enter the max range : "))
numbers = []
numbers_length = 0

# if min_range > max_range :
#     print("min range is not valid")


for i in range (user_numbers_length):
    # while len(numbers) <= user_numbers_length :
    random_number = random.randint(min_range, max_range)
    numbers.append(random_number)
    numbers_length += 1

print(numbers)
print(numbers_length)

print("===========================================================")


swapped = True

while swapped :
    swapped = False
    for i in range (numbers_length-1):
        if numbers[i]>numbers[i+1]:
            temp = numbers[i]
            numbers[i] = numbers[i+1]
            numbers[i+1] = temp
            swapped = True

print(numbers)
        