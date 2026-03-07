nums = [1, 2, 3, 4, 5]

# reverse this list
print(nums[::-1])

fruits = ['apple', 'banana', 'mango']
#print index and value
for index, value in enumerate(fruits):
    print(index, value)


names = ["John","Sam","Alex"]
ages = [25,30,28]

for name, age in zip(names, ages):
    print(name, age)


numbers = [3, 7, 2, 9, 5]

# Create a new list where each number is squared using list comprehension.

newlist = [x*x for x in numbers] 
print(newlist)

