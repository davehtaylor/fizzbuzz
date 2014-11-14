# Fizzbuzz
#
# Prints numbers from 1 to 100. If the number is divisible by 3, 'Fizz'
# is printed instead. If the number is divisible by 5, 'Buzz' is 
# printed instead. If the number is divisible by both 3 and 5, 
# 'Fizzbuzz' is printed instead.

for i in xrange (1,101):       # Print out the numbers from 1 - 100.

    if i%3 == 0 and i%5 == 0:  # Evaluate if the number is divisible by 
        print "Fizzbuzz"       # both 3 and 5. Need to do this first, or 
                               # this condition would never evaluate.

    elif i%3 == 0:             # Evaluate if the number is divisible by 3
        print "Fizz"

    elif i%5 == 0:             # Evaluate if the number is diivisble by 5
        print "Buzz"

    else:                      # Otherwise, just print out the number
        print i
