import sys
from collections import defaultdict, namedtuple

HSeg = namedtuple("HSeg", ["y", "xl", "xr"])
VSeg = namedtuple("VSeg", ["x", "yb", "yt"])

def mrg_ivs(ivs: list[tuple[int, int]]) -> list[list[int]]:
    if not ivs:
        return []
        
    ivs.sort()
    
    mrgd = []
    for s, e in ivs:
        if not mrgd or s > mrgd[-1][1]:
            mrgd.append([s, e])
        else:
            mrgd[-1][1] = max(mrgd[-1][1], e)
    return mrgd

def read_data(n: int) -> tuple[list[HSeg], list[VSeg]]:
    hmap = defaultdict(list)
    vmap = defaultdict(list)

    for _ in range(n):
        try:
            x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        except (IOError, ValueError):
            continue

        if y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            hmap[y1].append((x1, x2))
        else:
            if y1 > y2:
                y1, y2 = y2, y1
            vmap[x1].append((y1, y2))

    h_segs = []
    for y, ivs in hmap.items():
        for s, e in mrg_ivs(ivs):
            h_segs.append(HSeg(y=y, xl=s, xr=e))

    v_segs = []
    for x, ivs in vmap.items():
        for s, e in mrg_ivs(ivs):
            v_segs.append(VSeg(x=x, yb=s, yt=e))
            
    return h_segs, v_segs

def build_mask(h_segs: list[HSeg], v_segs: list[VSeg]) -> list[list[int]]:
    h_len = len(h_segs)
    v_len = len(v_segs)
    
    mask_w = (h_len + 63) // 64
    mask = [[0] * mask_w for _ in range(v_len)]

    for i in range(v_len):
        v_seg = v_segs[i]
        for j in range(h_len):
            h_seg = h_segs[j]
            
            y_ok = v_seg.yb <= h_seg.y <= v_seg.yt
            x_ok = h_seg.xl <= v_seg.x <= h_seg.xr
            
            if y_ok and x_ok:
                b_idx = j // 64
                b_off = j % 64
                mask[i][b_idx] |= (1 << b_off)
                
    return mask

def count_pairs(mask: list[list[int]], v_len: int, mask_w: int) -> int:
    total = 0
    for i in range(v_len):
        for j in range(i + 1, v_len):
            common = 0
            for b in range(mask_w):
                bits = mask[i][b] & mask[j][b]
                common += bits.bit_count()
            
            if common >= 2:
                total += common * (common - 1) // 2
                
    return total

def main():
    n_line = sys.stdin.readline()
    if not n_line:
        return
    try:
        n = int(n_line)
    except ValueError:
        return

    if n == 0:
        print(0)
        return

    h_segs, v_segs = read_data(n)
    
    h_len = len(h_segs)
    v_len = len(v_segs)
    
    if h_len == 0 or v_len == 0:
        print(0)
        return

    mask = build_mask(h_segs, v_segs)
    mask_w = (h_len + 63) // 64
    
    result = count_pairs(mask, v_len, mask_w)
    print(result,end="")

if __name__ == "__main__":
    main()