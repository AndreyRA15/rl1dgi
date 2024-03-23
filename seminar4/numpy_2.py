import numpy as np



# t = np.linspace(0, 99, 100)
# print(t[-11:-1:2])


# revt = t[::-1]
# print(revt)



# t1 = np.linspace(0, 10, 6).reshape(6,1)
# t2 = np.linspace(0, 20, 5).reshape(1,5)

# print(t1, t2)

# prod1 = t1@t2

# print(prod1)

# print(matr1)

# print(matr1[1:5:2,1:8:1])


# t1 = np.linspace(1,4,4).reshape(4,1)
# t2 = np.linspace(5,8,4).reshape(1,4)

# prod2 = t1@t2

# print(prod2[1:3, (0,2)])


A = np.array([[1, 1],[0, 1]])

B = np.array([[2, 0],
              [3, 4]])

print(np.dot(A, B))