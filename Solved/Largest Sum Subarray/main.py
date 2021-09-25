def find_max_sum_sub_array(A):
    length = len(A)
    if length < 1 :
      return A[0]
    current_max = A[0]
    now_max = A[0]
    for i in range(0,length,1):
        if now_max < 0:
            now_max = A[i]
        else:
            now_max += A[i]
        if current_max < now_max:
            current_max = now_max
    return current_max