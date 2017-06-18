def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    import random
    balls = [-1, 1]*4
    times = 0
    
    for _ in range(numTrials):
        total = sum(random.sample(balls, 3))
        if total in (-3,3):
            times += 1 
    return(times/numTrials)

print(drawing_without_replacement_sim(1000))
