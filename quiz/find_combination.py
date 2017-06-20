def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """ 
    import numpy as np
    
    def findOptimal(choices, currentSum, total):
        if currentSum > total:
            return
        if choices == []:
            return ((),currentSum)
        
        tmp = choices[0]
        resWithout = findOptimal(choices[1:], currentSum, total)
        resWith = findOptimal(choices[1:], currentSum + tmp, total)
        
        if resWith is None:
            result = resWithout           
        else:
            if abs(total - resWith[1]) >  abs(total - resWithout[1]):
                result = resWithout
            else:
                result = (resWith[0] + (tmp,), resWith[1])
        return result
        
    ans, value = findOptimal(choices, 0, total)
    res = np.repeat(0,len(choices))
    for a in ans:
        for i in range(len(choices)): 
            if choices[i] == a and res[i] != 1:
                res[i] = 1
                break
    return res
