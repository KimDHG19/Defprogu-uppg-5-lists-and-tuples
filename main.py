import random
# uppg 1-3

numAmount = int(input("Enter how many numbers you want to add "))

numList = []

for i in range(0, numAmount):
	number = int(input("enter number "))
	numList.append(number)

print(numList)

num_list_Reversed = numList[::-1]

print(num_list_Reversed)

print(sum(numList) / len(numList))

absoluteList = [abs(x) for x in numList]

print(absoluteList)

print(sum(numList))

# uppg 4, 5 & 6

amount_of_numbers = random.randint(50, 100)
lst = [random.randint(0, 3000) for _ in range(0, amount_of_numbers)]

print(lst)

min_num = min(lst)
min_num_index = lst.index(min_num)
max_num = max(lst)
max_num_index = lst.index(max_num)

first_ele = lst.pop(min_num_index)
second_ele = lst.pop(max_num_index)

lst.insert(min_num, second_ele)
lst.insert(max_num, first_ele)

print(f'Lowest number is: {first_ele}, the highest number is: {second_ele},'
	  f' and the list after swapping places of the lowest and highest numbers: {lst}')

# 6

lst.sort()

print(f'List sorted lowest to highest: {lst}')
