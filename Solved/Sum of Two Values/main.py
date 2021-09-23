def find_sum_of_two(A, val):
    
    return rec(0,A,val,len(A))
def rec(idx,A,val,length):
    
    for i in range(0,length,1):
        if i == idx:
            continue
        if A[i]+ A[idx] == val:
            return True
    if idx +1 >= length:
        return False
    return rec(idx+1,A,val,length)