dna1 = 'GATATATGCATATACTT'
dna2 = 'ATAT'

def find_mdna_positions(dna, mdna):
    positions = []
    motif_length = len(mdna)
    
    for i in range(len(dna) - motif_length + 1):
        if dna[i:i+motif_length] == mdna:
            positions.append(i + 1)
    
    return positions

positions = find_mdna_positions(dna1, dna2)
print(*positions)

# 2 4 10