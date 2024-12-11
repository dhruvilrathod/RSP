text1="""125 17"""

text = """5 89749 6061 43 867 1965860 0 206250"""


# this will not work for large blinks, just exeeds the memory space
def get_total_stone(text, max_blinks):
    stones = text.split(" ")
    print(stones)
    count = 0
    while count < max_blinks:
        stones = update_stones(stones)
        count+=1
    return len(stones)


def update_stones(stones):
    new_stones = []
    for s in stones:
        if int(s) == 0:
            new_stones.append("1")
        elif len(s) % 2 == 0:
            mid = len(s) // 2
            first = int(s[:mid])
            second = int(s[mid:])
            new_stones.append(str(first))
            new_stones.append(str(second))
        else:
            new_stones.append(str(int(s)*2024))
    return new_stones



# this will work for large blinks
def get_total_stone_fast(text, num_blinks):
    initial_stones = text.split(" ")

    freq = {}
    
    for stone in initial_stones:
        freq[stone] = 1

    for i in range(num_blinks):
        new_freq = {}
        for stone in freq:
            new_stones = update_stones_fast(stone)
            for new_stone in new_stones:
                if not new_freq.get(new_stone):
                    new_freq[new_stone] = freq[stone]
                else:
                    new_freq[new_stone] += freq[stone]
        freq = new_freq
    total_stones = 0

    for f in freq:
        total_stones += freq[f]

    return total_stones


def update_stones_fast(stone):
    if stone == '0':
        return ['1']
    if len(stone) % 2 == 0:
        mid = len(stone) // 2
        left = stone[:mid]
        right = stone[mid:]
        right = str(int(right))
        return [left, right]
    else:
        return [str(int(stone) * 2024)]


total = get_total_stone(text, 25)
print("total stones after 25: ", total)

total2 = get_total_stone_fast(text, 75)
print("total stones after 75: ", total2)