# Generate random number
# Round it
# if 0, Head
# else Tails
# Do this 5,000 times
countHead = 0
countTails = 0

for iterration in range(1, 6):

    import random
    coinToss = round(random.random())

    if coinToss < 1:
        countHead = countHead + 1
        print "Attempt #{}: Throwing a coin... It's a head! ... Got {} head(s) so far and {} tail(s) so far".format(iterration, countHead, countTails)
    else:
        countTails = countTails + 1
        print "Attempt #{}: Throwing a coin... It's a head! ... Got {} head(s) so far and {} tail(s) so far".format(iterration, countHead, countTails)
