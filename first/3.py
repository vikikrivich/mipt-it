dna = 'AAAACCCGGT'

sec_dna = ''
for el in dna[::-1]:
    match el:
        case 'A':
            sec_dna += 'T'
        case 'T': 
            sec_dna += 'A'
        case 'G':
            sec_dna += 'C'
        case 'C':
            sec_dna += 'G'

print(sec_dna)
# ACCGGGTTTT