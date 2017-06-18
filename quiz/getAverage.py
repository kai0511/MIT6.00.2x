def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated to 3 decimal places
    """
    res = []
    for _ in range(numTrials):
        trial = [die.roll() for _ in range(numRolls)]
        
        count, tmp, maxValue = 1, trial[0], 1
        l = len(trial[1:])
        for i in range(l):
            if trial[i+1] == tmp:
                count += 1
                if i == l-1:
                    maxValue = max(maxValue, count) 
            else:
                maxValue = max(maxValue, count)
                tmp, count = trial[i+1], 1
                
        res.append(maxValue)
    makeHistogram(res, 10, 'the longest run', 'frequency')
    return sum(res)/numTrials
