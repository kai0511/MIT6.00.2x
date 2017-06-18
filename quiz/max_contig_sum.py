def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    maxValue, tmpMax = L[0], L[0]
    
    for s in L[1:]:
        tmpMax = max(s, tmpMax + s)
        maxValue = max(tmpMax, maxValue)
    return maxValue
    
print(max_contig_sum([3, 4, -1, 5, -4]))
print(max_contig_sum([3, 4, -8, 15, -1, 2]))
