# Loops
for count in range(0, 1):
    print "Count - ", count

# While Loops
count = 0 # Starting point
while count < 1: # Condition
    print "Number", count # Output
    count += 1 # Increments

# Breaking Loops- run loop intil you find a value set then break!
# for val in "Timothy":
#     if val == "y":
#         break
#     print(val)

# Continue
# for val in "Timothy":
#     if val == "o":
#         continue
#     elif val == "h":
#         break
#     print(val)

# Test
x = 3
y = x
while y < 10:
    print y
    y = y + 1
    if y == 5:
        print "Final else statement"
