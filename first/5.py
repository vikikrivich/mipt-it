dna1 = 'GAGCCTACTAACGGGAT'
dna2 = 'CATCGTAATGACGGCCT'

mutations_count = 0
for i in range(0,len(dna1)):
    if dna1[i] != dna2[i]:
        mutations_count += 1

print(mutations_count)
# 7