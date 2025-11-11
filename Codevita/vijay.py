import sys

L = sys.stdin.read().splitlines()
K = int(L[3])

G = {
    (' _ ', '| |', '|_|'): 0,
    ('   ', '  |', '  |'): 1,
    (' _ ', ' _|', '|_ '): 2,
    (' _ ', ' _|', ' _|'): 3,
    ('   ', '|_|', '  |'): 4,
    (' _ ', '|_ ', ' _|'): 5,
    (' _ ', '|_ ', '|_|'): 6,
    (' _ ', '  |', '  |'): 7,
    (' _ ', '|_|', '|_|'): 8,
    (' _ ', '|_|', ' _|'): 9,
}

orig_d = []
num_digits = (len(L[0]) + 1) // 4

for i in range(num_digits):
    k = (L[0][i*4:i*4+3], L[1][i*4:i*4+3], L[2][i*4:i*4+3])
    if k in G:
        orig_d.append(G[k])

orig_n = int("".join(map(str, orig_d)))

T = { 8: 7, 7: 1, 4: 0 }
mod_d = list(orig_d)
toggled = set()

for _ in range(K):
    opts = []
    for i, d in enumerate(mod_d):
        if i not in toggled and d in T:
            opts.append((T[d], i))
    
    if not opts:
        break

    opts.sort()
    n_d, idx = opts[0]
    mod_d[idx] = n_d
    toggled.add(idx)

n = len(mod_d)
i = n - 2
while i >= 0 and mod_d[i] >= mod_d[i+1]: i -= 1
j = n - 1
while mod_d[j] <= mod_d[i]: j -= 1
mod_d[i], mod_d[j] = mod_d[j], mod_d[i]
mod_d[i+1:] = mod_d[i+1:][::-1]

anagram_n = int("".join(map(str, mod_d)))

print(abs(orig_n - anagram_n))