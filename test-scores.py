# Prompt user to enter test score
# Compare scores to our grading system
# Spit out what grade that is


for prompt in range(0, 5):

    print "Enter a score between 60 and 100"
    userGuess = input()

    if userGuess >= 60 and userGuess <= 69:
        print "Score: {}. Your grade is D".format(userGuess)

    elif userGuess >= 70 and userGuess <= 79:
        print "Score: {}. Your grade is C".format(userGuess)

    elif userGuess >= 80 and userGuess <= 89:
        print "Score: {}. Your grade is B".format(userGuess)

    elif userGuess >= 90 and userGuess <= 100:
        print "Score: {}. Your grade is A".format(userGuess)

    else:
        print "That grade is too low!"

print "End of the Program. Bye!"
