import re

def is_special(word):
    return '@' in word or word.startswith('http://') or word.startswith('https://')

def is_bullet(word):
    if word in ('*', '-'): return True
    if len(word) > 1 and word[:-1].isdigit():
        return word.endswith('.') or word.endswith(')')
    return False

def parse_command(cmd_line):
    parts = cmd_line.split()
    width_even, width_odd = 75, 75
    hyphenate = 'h' in parts
    
    args = {}
    for i in range(len(parts) - 1):
        if parts[i] in ('-w', '-w-e', '-w-o') and parts[i+1].isdigit():
            args[parts[i]] = int(parts[i+1])

    if '-w' in args:
        width_even = width_odd = args['-w']
    if '-w-e' in args:
        width_even = args['-w-e']
    if '-w-o' in args:
        width_odd = args['-w-o']
            
    return width_even, width_odd, hyphenate

def solve():
    N = int(input())
    lines = [input() for _ in range(N)]
    cmd_line = input()

    width_even, width_odd, hyphenate = parse_command(cmd_line)

    text_block = "\n".join(lines)
    raw_paras = re.split(r'\n\s*\n', text_block.strip())
    paragraphs = []
    
    for para in raw_paras:
        current_words = []
        words_from_line = para.split()
        for w in words_from_line:
            if is_bullet(w):
                current_words.append(w)
                continue
            
            if (w.startswith('*') or w.startswith('-')) and len(w) > 1 and not is_special(w):
                current_words.append(w[0])
                current_words.append(w[1:])
                continue

            match = re.match(r'^(\d+[.)])(\S+)', w)
            if match and not is_special(w):
                current_words.append(match.group(1))
                current_words.append(match.group(2))
            else:
                current_words.append(w)
        if current_words:
            paragraphs.append(current_words)

    output_lines = []
    current_line = ""
    line_index = 0

    for para_words in paragraphs:
        if current_line:
            output_lines.append(current_line)
            current_line = ""
            line_index += 1
            
        word_queue = para_words[:] 
        
        while word_queue:
            word = word_queue.pop(0)
            max_width = width_even if line_index % 2 == 0 else width_odd
            
            if is_bullet(word):
                if current_line:
                    output_lines.append(current_line)
                    line_index += 1
                current_line = word
                continue

            prefix = " " if current_line else ""
            needed_space = len(prefix) + len(word)
            
            if len(current_line) + needed_space <= max_width:
                current_line += prefix + word
                continue
            
            if is_special(word):
                if current_line:
                    output_lines.append(current_line)
                    line_index += 1
                output_lines.append(word)
                line_index += 1
                current_line = ""
                continue

            if not hyphenate:
                if current_line:
                    output_lines.append(current_line)
                    line_index += 1
                current_line = word
                continue
            
            space_left = max_width - len(current_line)
            chars_from_word = space_left - len(prefix) - 1
            
            if chars_from_word < 1:
                if current_line:
                    output_lines.append(current_line)
                    line_index += 1
                current_line = word
            else:
                part1 = word[:chars_from_word]
                part2 = word[chars_from_word:]
                current_line += prefix + part1 + "-"
                output_lines.append(current_line)
                line_index += 1
                current_line = ""
                word_queue.insert(0, part2)

    if current_line:
        output_lines.append(current_line)

    print("\n".join(output_lines))

solve()