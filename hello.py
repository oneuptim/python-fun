# Varibale to set our greeting message
greeting = "What's up,"

# Screen prompt to ask user for their name
print 'What is your name?'

# Input for user to enter their name
name = raw_input()

# Screen instruction to ask for user's age
print 'How old are you?'

# Prompt input to ask user for their age
age = input()

# Return statements to give user feedback on what they have entered!
if age > 30:
    print greeting, name + '!', 'Being', age, 'must feel really old, huh?'
elif age == 30:
    print "Damn! You're getting old", name + '!'
else:
    print "Ahhh, you're just a youngin'", name + '!'

# Add some space for readability
print "------------------------------------------------------"
print "------------------------------------------------------"

# Trying out string interpolation!
print "This is an interpolated greetint '{}' but hold up! {}, are you really {}?".format(greeting, name, age)

# Prompt user for input whether they are really the age they asay they are
response = raw_input()

# Spit this back!
print "You said {}".format(response), "and I gotta believe you cuz- women lie, men lie, numbers don't lie!"
