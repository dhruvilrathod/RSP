# This returns the bit at given position in a numebr
# Time complexity: O(1)
def get_bit(num, position):
    return 0 if num & (1 << position) == 0 else 1

# This will flip the bit at given position to 1
# Time complexity: O(1)
def set_bit(num, position, bit):
    return num | (1 << position)

# This will flip the bit at given position to 0
# Time complexity: O(1)
def clear_bit(num, position):
    return num & ~(1 << position)


def update_bit(num, position, bit):
    return clear_bit(num, position) if bit == 0 else set_bit(num,position)

# Time Complexity: O(1)
def insert_into_number(n,m,i,j):
    all_ones = ~0
    left = all_ones << j+1
    right = (1 << i) - 1 # this will make the maks in 2^n - 1 till ith position
    mask = left | right # in this, middle elements will be zero, as this is not created from N or M
    n = n & mask
    m = m << i
    return n | m

