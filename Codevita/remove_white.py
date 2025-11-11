def remove_white(s):
    removed = []
    for i in s:
        if i != " ":
            removed.append(i)
    return removed
s = input()
print("".join(remove_white(s)))