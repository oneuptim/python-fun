# Function should return the sum of this list
def listSum(numList):
    if len(numList) == 1: #Check if the length of the list has only one element
        return numList[0] # If that's the case, the sum is just that element, index 0
    else:
        return numList[0] + listSum(numList[1:]) #

print(listSum([1, 2, 5, 10, 255, 3]))
# Expected output 276
