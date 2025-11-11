import heapq

n = int(input())
if n == 0:
    print(0)
    exit()

orders = []
for i in range(n):
    at, pt, vip = map(int, input().split())
    orders.append((at, pt, vip, i))

orders.sort()

vip_q = []
reg_q = []
ctime = 0
idx = 0
done = 0
waits = [] 

while done < n:
    
    if not vip_q and not reg_q and idx < n:
        ctime = max(ctime, orders[idx][0])

    while idx < n and orders[idx][0] <= ctime:
        at, pt, vip, i = orders[idx]
        item = (at, pt, i)
        if vip:
            heapq.heappush(vip_q, item)
        else:
            heapq.heappush(reg_q, item)
        idx += 1

    if vip_q:
        at, pt, i = heapq.heappop(vip_q)
    elif reg_q:
        at, pt, i = heapq.heappop(reg_q)
    else:
        continue 

    start = ctime
    
    if at < start:
        waits.append((at, start))

    ctime = start + pt
    done += 1

if not waits:
    print(0)
    exit()

events = []
for s, e in waits:
    events.append((s, 1))
    events.append((e, -1))

events.sort(key=lambda x: (x[0], -x[1]))

max_c = 0
cur_c = 0
for t, type in events:
    cur_c += type
    max_c = max(max_c, cur_c)

print(max_c)