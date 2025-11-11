#def union_using_set(arr1, arr2):
#    return sorted(set(arr1).union(set(arr2)))

def union_two_pointer(arr1,arr2):
    i,j = 0,0
    union = []
    while i<len(arr1) and j<len(arr2):
        if arr1[i] < arr2[j]:
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i+=1
        elif arr2[j] < arr1[i]:
            if not union or union[-1] != arr2[j]:
                union.append(arr2[j])
            j+=1
        else:
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i+=1
            j+=1
    #Add remaining
    while i<len(arr1):
        if union[-1] != arr1[i]:
            union.append(arr1[i])
        i+=1
    while j<len(arr2):
        if union[-1] != arr2[j]:
            union.append(arr2[j])
        j+=1

    return union

arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

arr1.sort()
arr2.sort()

result = union_two_pointer(arr1,arr2)
print(result)
#yup
#asd