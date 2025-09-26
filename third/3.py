def codify(m, key):
    arr = [[0,1,2,3,4,5,6],
           [1,4,0,2,6,3,5],
           [2,0,3,5,1,6,4],
           [3,2,5,6,0,4,1],
           [4,6,1,0,5,2,3],
           [5,3,6,4,2,1,0],
           [6,5,4,1,3,0,2]]
    
    if key == 0:
        return 0
    
    result = m
    for i in range(1, key):
        result = arr[m][result]
    
    return result

print(codify(1, 3))