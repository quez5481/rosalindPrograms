seq1 = 'TCTATTCGCGTTCAGCTCGTACGCGAACCGTTGAGAATTTTCTACGCCTGAGTTAGGAGCGGTTCCAATTTGGTGTTCAAAGAGCTTATCAACGATAGTGTGCGTCATTGCTTACTCCGGACGACTCCGCGGATGATGAAGTACCTTTGAACCACGCCCATATGTAGGAAGACCCTGTAAGGTCAAGCCGAAGAGCTAGGAGACTTCAGCTTGAGATTATTGGCCCGATGGTGTTTAGCGATCGCACTGGTATGGTGATAAATGGTTTCTCAAAGTTCACGAGGAGGACGGTTCGTTTTGTCTATTGCGGCGGGATGAACATGGACGAGATGCCCTTATCTGCAGAATAGTAACATATCTCTTAGCGCAAACGTGGTACGCCAACCCTCTGATTTCTCAGTCGTTGAAATCGGATCGTGCCCTTCATTCCTGGTAGCGTCCTACGTTACCGGTGAGGTGGTGGCATCCAAGATTCTAAGGCCACCTGGCAATTGTCTGAAGGTGGTAGATTCAGCAGTAATTGTACTAGTGGTTATACGATTCCAAACCAGGTTCGGGAATGGAGCGGTCGGGAAAGTTACCGGGGTTCGGGCTCGGCAATGGCGGATGGTGTCCTTAGTTAACCAGCGCTTGCCGTGCCCCGTCCGCGGCTGTCACAAATAACGATGGTAGTTATCTCCATTCAGTGGAGCCAACAAAAAAACTGCGGATGGGCTATAGCACGTACGCGGGAGAATACCCCCCCTCGAGCACACTTGGATCTCACGGTCATATGCACTAAACTAGGAGCACCGTGCAAGGCTAGCTGAGCAAAGAGGGCAAACTGGACACCCCTTCTCAACGCCGCCCAGTGACGGACACTCCATCAGGACAGCATCTAGAATCGTGGCTTTCAATCTTGCC'
seq2 = 'TGGCTGAGCGTTCTGGCGGTAGGCGAATCGGTACACGCGTTCAGTGGTAGAGCGTAGTTGGTTCCAATAGTGGCTTTCGATGGGCTAGTCCCGTGCAGGGTGGAACTCAGTCTACTCGCGATGTAACCTCGGATCAGGAATAAGCTCGGAGCCATGCCCAATGTTCGTGTGACATTTGATGACCCAGCATAAGAAGTTAGACCAACCGGTCCGAAGTAGATACGATGACGGTGTTTACTCAGTGTACTGTATTTATGTTAAATGGTTTAAGGTAGTTCACCAGGCGCATTCTGCGTGAGGGCTAGTGCGAAGCGATGAACTCTGACCCTCAGACCATAACTCTTCTACGCTCGTATACAGCTTCTCAGCATCTTAAGGGACCAGCCTCCTGGTATCTTATTCGTCGAGTCGACCTCGGGCGTTCTCTTTGTTGTATCCTCTATCGCACCCGCAGATAGAGTGCCATCCTATGTTTAATGCACTCTCACCAATCAACTGAGTTTTAGATCTTCAACCCAATCTAGTATGCGCGTTCAACAAGTTTTAATCACAAACTCGAATATAAACGTCTGACGAGTTAATGTGCCTCTCGCGTGTCAATGACTCGAACAACACGACTGAAGCACTCAGAGTCCGTGCCTTGTCCTCTTCGAACACGAATAACGATAATAATTATCTCCCGTTCATGTTGAGTGTAATACAACGTTGGAGGGCCTACCGGAAGTAGGAGTACGTATGCGCCCCAACACGCGCACGGGCTTATACCATTCAAAGCCATCAAACGAAGAGGTGCATGATACGATTTCTAAGTAATGACCGCACTCGAGTCCCGATTGGCTCATGCCCTCATAACACCGAAACCTGCTCAGCACAGGTTCCTGCATGAGAGAATACCCCCTTGTC'

def hamming(s1, s2):
    count = 0
    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            count = count + 1
    return count
if len(seq1) == len(seq2):
    print('Both sequences of have same number of elements. Number of elements: ' + str(len(seq1)))
    print('Hamming Distance = ' + str(hamming(seq1, seq2)))
    
else:
    print('Sequences have different number of elements')
    
