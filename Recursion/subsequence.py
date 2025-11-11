def print_sub(ind, ds, arr, n, k):
    if ind >= n:
        if sum(ds) == k:
            print(ds)
            return True
        return False
    
    ds.append(arr[ind])
    if print_sub(ind + 1, ds, arr, n, k) == True:
        return True
    ds.pop()

    if print_sub(ind + 1, ds, arr, n, k) == True:
        return True

    return False

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    n = len(arr)
    ds = []
    k = int(input())
    print_sub(0, ds, arr, n, k)

