def print_sum(ind, arr, n, k, ds):
    if k == 0:
        print(ds)
        return
    if ind == len(arr):
        return
    
    if arr[ind] <= k:
        ds.append(arr[ind])
        print_sum(ind, arr, n, k - arr[ind], ds)
        ds.pop()

    print_sum(ind + 1, arr, n, k, ds)

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    arr.sort()
    n = len(arr)
    k = int(input())
    print_sum(0, arr, n, k, [])
    
