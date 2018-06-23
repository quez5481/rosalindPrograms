""" Prints number of pairs after n months and each pair as k pairs of offspring. """

n = 33
k = 5

seq = [1, 1]

for x in range(2, n):
    seq.append((k*seq[x-2]) + seq[x-1])
    
print(seq[n-1])

