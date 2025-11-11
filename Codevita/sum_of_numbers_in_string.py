def sum_of_num(s):
    sum = 0
    current = ""
    for i in s:
        if (i >= '0' and i <= '9' ):
            current += i
            continue
        else:
            if current:
                sum += int(current)
            current = ""
    if current:
        sum += int(current)
        
    return sum

s = input()
print(sum_of_num(s))