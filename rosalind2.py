""" This program transcribes a string type dna sequence to an rna sequence. """

s = 'TCACGTTGTTTAAGTAGCCTCCAGAGAGCATATTCCGGTATGGGCTAATCCAAGGGTGGTCGGTCCGGATAAGCGATAGGCGTAAAGTTGACACTGAGCCGTGAACGGGTTGAAACAACTCCAGCTGTCAAGAAGACAAAGACAATGTATCAATGCCGGTCTACGGTGTCGAACGATAAGTGAATATAACTCTATCAAGCAGTTCACGGTTATGTGATTGAGCCAATCTGAGTGACTTGCAGCGTTAGACACGTAGTGCATAGGAACATTGCAAGGTTTCCACTACGGTCCTACGGAATCGTATTTGAGTTACACCAGCATGCTGCGGAGTCACTCGTACAAGACTCGCCGACATTGGCAAGTGAATGCTATAACAAACCAGACGAGGATGACCAACCTGGCCGGTAAACATAAGCAGGGAATGGTCCTCTATATGAGAGGAAAATTTTTAGGGAGGTCATAGATGGTCCAACGGCCGTCCTATAATGGCATGCCAGTCTACCAATACATGATCGCTGTGGTCGAAAATCATTGGACTTTAGTCAATAACACTGCATCAGCTCGATGCAGAAGAATGTTTAGACCGGTCCCGTGCGTACCACACACGGCATGTGTTGGAAAAGCATGGAATGAGACGCTACCGGTCCCGTCATCGGTGACTCTTGTAATGAGATATTCGGTAGCGAATTATGCTCAAGAAATACTTTGCAATGGCATCACCTTCACCGTCCGTAACGGCGTGGGTCCGGAGGAGGATCGGGCGTAGGGGATGCGATCGTGATAGGACCCGACGACAGAATAGCTTGCCGGTCAGAAGCAACTAAACGGCATGATTGTCAAAACGCAGTTAGAATGCCGCACTCGTGTATGACGATAATCGTCCACACACTTGCTCGGCCTATTA'

def dr(dna):
    rna = ''
    for x in dna:
        if x != 'T':
            rna = rna + x
        else:
            rna = rna + 'U'
    return rna
    
output = dr(s)
print(output)
