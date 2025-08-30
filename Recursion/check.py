def print_sum(ind, arr, n, k, ds):
    if ind >= n:
        if sum(ds) == k:  # Use ds, not arr!
            print(ds)
        return

    # Include arr[ind]
    ds.append(arr[ind])
    print_sum(ind + 1, arr, n, k, ds)
    ds.pop()

    # Exclude arr[ind]
    print_sum(ind + 1, arr, n, k, ds)

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    n = len(arr)
    k = int(input())
    ds = []
    print_sum(0, arr, n, k, ds)
