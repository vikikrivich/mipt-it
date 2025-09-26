dnas = ['ATCCAGCT', 'GGGCAACT', 'ATGGATCT', 'AAGCAACC', 'TTGGAACT', 'ATGCCATT', 'ATGGCACT']

def find_consensus_and_profile(sequences):
    n = len(sequences[0])
    
    profile = {
        'A': [0] * n,
        'C': [0] * n,
        'G': [0] * n,
        'T': [0] * n
    }
    
    for sequence in sequences:
        for i, nucleotide in enumerate(sequence):
            profile[nucleotide][i] += 1
    
    consensus = []
    for i in range(n):
        max_count = 0
        max_nucleotide = ''
        for nucleotide in ['A', 'C', 'G', 'T']:
            if profile[nucleotide][i] > max_count:
                max_count = profile[nucleotide][i]
                max_nucleotide = nucleotide
        consensus.append(max_nucleotide)
    
    return ''.join(consensus)

consensus = find_consensus_and_profile(dnas)
print(consensus)
# ATGCAACT


# Кривич Виктория - 5