n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

sbox_s = [
    [10, 14, 13, 5, 9, 7, 0, 6, 15, 4, 11, 8, 2, 12, 1, 3],
    [0, 2, 11, 6, 8, 10, 5, 13, 15, 9, 12, 7, 1, 3, 14, 4],
    [9, 3, 13, 5, 7, 11, 8, 6, 2, 4, 14, 15, 12, 0, 1, 10],
    [7, 8, 5, 15, 11, 3, 9, 6, 2, 12, 1, 4, 14, 0, 10, 13],
    [13, 12, 5, 15, 4, 0, 10, 9, 7, 8, 3, 2, 11, 6, 1, 14]
]


def print_state(state, title):
    print(f"\n{title}:")
    for row in state:
        print(row)


def list_to_state(input_list):
    state = []
    for i in range(4):
        row = []
        for j in range(4):
            row.append(input_list[i + j*4])
        state.append(row)
    return state


def sub_bytes(state, sbox):
    new_state = []
    for row in state:
        new_row = []
        for value in row:
            new_row.append(sbox[value])
        new_state.append(new_row)
    return new_state


def shift_rows(state):
    new_state = []
    for i, row in enumerate(state):
        new_row = row[i:] + row[:i]
        new_state.append(new_row)
    return new_state



def xtime(a):
    result = a << 1
    if result & 0x100:
        result ^= 0x11B
    return result


def gf_multiply(a, b):
    result = 0
    for i in range(8):
        if b & 1:
            result ^= a
        a = xtime(a)
        b >>= 1
    return result


def mix_columns(state):
    new_state = [[0]*4 for _ in range(4)]
    
    for col in range(4):
        column = [state[row][col] for row in range(4)]
        
        new_state[0][col] = gf_multiply(0x02, column[0]) ^ gf_multiply(0x03, column[1]) ^ column[2] ^ column[3]
        new_state[1][col] = column[0] ^ gf_multiply(0x02, column[1]) ^ gf_multiply(0x03, column[2]) ^ column[3]
        new_state[2][col] = column[0] ^ column[1] ^ gf_multiply(0x02, column[2]) ^ gf_multiply(0x03, column[3])
        new_state[3][col] = gf_multiply(0x03, column[0]) ^ column[1] ^ column[2] ^ gf_multiply(0x02, column[3])
    
    return new_state


def add_round_key(state, round_key):
    new_state = [[0]*4 for _ in range(4)]
    
    key_matrix = list_to_state(round_key)
    
    for col in range(4):
        for row in range(4):
            new_state[row][col] = state[row][col] ^ key_matrix[row][col]
    
    return new_state


print(f"n = {n}")

state = list_to_state(n)
print_state(state, "1. Init")

state_after_subbytes = sub_bytes(state, sbox_s[0])
print_state(state_after_subbytes, "2. SubBytes")

state_after_shiftrows = shift_rows(state_after_subbytes)
print_state(state_after_shiftrows, "3. ShiftRows")

state_after_mixcolumns = mix_columns(state_after_shiftrows)
print_state(state_after_mixcolumns, "4. MixColumns")

state_after_addroundkey = add_round_key(state_after_mixcolumns, sbox_s[0])
print_state(state_after_addroundkey, "5. AddRoundKey")
