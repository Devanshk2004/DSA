def kaprekar(num):
    sq = num**2
    str_sq = str(sq)
    for i in range(1,len(str_sq)):
        left = str_sq[:i]
        right = str_sq[i:]

        left_num = int(left) if left else 0
        right_num = int(right) if right else 0

        if left_num + right_num == num and right_num!= 0:
           return True
    return num == 1
            
num = int(input())
if kaprekar(num):
    print("It is kaorekar number")
else:
    print("It is not Kaprekar number")