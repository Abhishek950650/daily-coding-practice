import numpy as np

# arr = [[1, 2],
#  [3, 4],
#  [5, 6]]

# matrix = np.array(arr)
# print(matrix)
# print(np.sum(matrix, axis=0))
# print(np.sum(matrix, axis=1))
# print(np.mean(matrix, axis=0))

# data = np.array([
#  [170,70,25],
#  [165,65,30],
#  [180,80,35]
# ])
# height, weight, age
# extract age column
# print(data[:,2])

# extract first two column
# for i in range(2):
#     print(data[:, i])
# print(data[:, :2])

# extracted second row
# print(data[1])

# data = np.array([
#  [170,70,25,1],
#  [165,65,30,0],
#  [180,80,35,1]
# ])

# print(data[ : , :3])
# print(data[ : , -1])

X = np.array([
 [170,70,25],
 [165,65,30],
 [180,80,35],
 [175,75,28]
])

Y = np.array([1,0,1,0])

#first 3 rows

print('X_train =', X[:3])
print('Y_train =', Y[:3])

# testing last row

print('X_test = ', X[-1])
print('Y_test = ', Y[-1])
