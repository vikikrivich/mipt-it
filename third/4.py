class Crypto:
    def __init__(self, key):
        self.arr = [[0,1,2,3,4,5,6],
                   [1,4,0,2,6,3,5],
                   [2,0,3,5,1,6,4],
                   [3,2,5,6,0,4,1],
                   [4,6,1,0,5,2,3],
                   [5,3,6,4,2,1,0],
                   [6,5,4,1,3,0,2]]
        self.key = key
    
    def codify(self, m):
        if self.key == 0:
            return 0
        
        result = m
        for i in range(1, self.key):
            result = self.arr[m][result]
        
        return result

# 4.2
A = Crypto(key=3)
B = Crypto(key=4)

# 4.4
m = 1
mA = A.codify(m)
mB = B.codify(m)

print(f"mA: {mA}")
print(f"mB: {mB}")

# 4.5
result1 = B.codify(mA)
result2 = A.codify(mB)

print(f"B.codify(mA): {result1}")
print(f"A.codify(mB): {result2}")

# 5.1
arr_0 = [0, 1, 2, 3, 4, 5, 6]
encoded_A = [A.codify(x) for x in arr_0]
print(f"arr[0] by A: {encoded_A}")
encoded_B = [B.codify(x) for x in arr_0]
print(f"arr[0] by B: {encoded_B}")

# 5.2
res_list = [0, 3, 4, 5, 6, 2, 1]