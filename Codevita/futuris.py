import sys

def get_val(token, v_map):
    token = token.strip()
    return v_map[token] if token in v_map else int(token)

op_funcs = {
    "==": lambda l, r: l == r,
    "!=": lambda l, r: l != r,
    "<":  lambda l, r: l < r,
    ">":  lambda l, r: l > r,
}

def evaluate_condition(cond_str, v_map):
    for op, func in op_funcs.items():
        if op in cond_str:
            left, right = cond_str.split(op)
            lval = get_val(left, v_map)
            rval = get_val(right, v_map)
            return func(lval, rval)
    return False

def collect_block(lines, start, stops):
    block, depth, i = [], 0, start
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("for") or line.startswith("if"):
            depth += 1
        elif line == "end":
            if depth == 0 and "end" in stops:
                break
            depth -= 1
        elif line in stops and depth == 0:
            break
        block.append(lines[i])
        i += 1
    return block, i

def run(lines, v_map):
    output, i = [], 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        
        parts = line.split()
        cmd = parts[0]

        if cmd == "print":
            token = parts[1]
            output.append(str(get_val(token, v_map)))
            i += 1
        elif cmd == "if":
            cond_str = " ".join(parts[1:])
            res = evaluate_condition(cond_str, v_map)
            i += 1
            
            yes_block, i = collect_block(lines, i, ("No", "end"))
            no_block = []
            
            if i < len(lines) and lines[i].strip() == "No":
                no_block, i = collect_block(lines, i + 1, ("end",))
            
            if i < len(lines) and lines[i].strip() == "end":
                i += 1
            
            if res:
                output += run(yes_block, v_map.copy())
            else:
                output += run(no_block, v_map.copy())
        elif cmd == "for":
            var, start, end = parts[1], parts[2], parts[3]
            start_val = get_val(start, v_map)
            end_val = get_val(end, v_map)
            
            block, i = collect_block(lines, i + 1, ("end",))
            
            if i < len(lines) and lines[i].strip() == "end":
                i += 1
                
            for val in range(start_val, end_val + 1):
                v_copy = v_map.copy()
                v_copy[var] = val
                output += run(block, v_copy)
        else:
            i += 1
    return output

def main():
    all_lines = [line.rstrip("\n") for line in sys.stdin]
    lines = [line for line in all_lines if line.strip()]

    if not lines:
         return
    
    vars_line = lines[-2].split()
    vals = list(map(int, lines[-1].split()))
    v_map = dict(zip(vars_line, vals))
    
    futuris_code = lines[:-2]
    result = run(futuris_code, v_map)
    
    if result:
        sys.stdout.write("\n".join(result))

if __name__ == "__main__":
    main()
