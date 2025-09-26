dna = 'GATGGAACTTGACTACGTAAATT'
rna = ''

for el in dna:
    if el == 'T':
        rna += 'U'
    else:
        rna += el

print(rna)
# GAUGGAACUUGACUACGUAAAUU
