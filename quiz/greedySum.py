def greedySum(L, s):
    if L == []:
        return 'no solution'
    elif s%L[0] == 0:
        return s//L[0]
    else:
        res = greedySum(L[1:], s%L[0])
        if res != 'no solution':
            return s//L[0] + res
        else: 
            return 'no solution'
