def even_frequency(s):
    total = 0
    i = 0
    while i < len(s):
        count = 1
        while i+1 < len(s) and s[i] == s[i+1]:
            count += 1
            i += 1
        if count % 2 == 0:
            total += count
        i += 1
    return total

s = input()
print(even_frequency(s))

