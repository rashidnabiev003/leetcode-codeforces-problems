def minimumRecolors(blocks: str, k: int) -> int:
    b_blocks_count = blocks[:k].count('B')
    min_count = k - b_blocks_count
    l_prev = blocks[0]
    l = 0
    r = k - 1
    while r < len(blocks) - 1:
        l += 1
        r += 1
        if l_prev == 'B':
            b_blocks_count -= 1
        if blocks[r] =='B':
            b_blocks_count += 1
        l_prev = blocks[l]
        min_count = min(min_count, k - b_blocks_count)
    
    return min_count

print(minimumRecolors(blocks = "WBWBBBW", k = 2))