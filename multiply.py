# Function that takes in a list and multiplies each element with 5
a = [2,4,10,16]
def multiply(array):
    for i in range(len(array)):
        array[i] = array[i] * 5
    return array

b = multiply(a)
print b
