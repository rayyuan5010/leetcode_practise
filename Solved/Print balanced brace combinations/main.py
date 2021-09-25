def print_all_braces(n):
    output = ["{"]*3 + ["}"]*3
    rec(output)
    return output
def rec(datas):
    need_mark = 0
    tmp_sum = -1
    for i in datas:
        if i == '{':
            tmp_sum += 1
        else:
            tmp_sum -= 1
        if tmp_sum  >= 1:
            break
        need_mark += 1
    
    if datas[len(datas)-2] == "}":
        rec(datas)
    else:
        return
            
    
    
print(print_all_braces(3))