def move_zeros_to_left(A):
    length = len(A)
    for i in range(0,length,1):
        if A[i] == 0:
            A.pop(i)
            A.insert(0,0)

v = [1, 10, -1, 11, 5, 0, -7, 0, 25, -35]
print("Original Array:", v)

move_zeros_to_left(v)

print("After Moving Zeroes to Left: ", v)
