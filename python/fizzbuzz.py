# Fizzbuzz
#
# Prints numbers from 1 to 100. If the number is divisible by 3, 'Fizz'
# is printed instead. If the number is divisible by 5, 'Buzz' is
# printed instead. If the number is divisible by both 3 and 5,
# 'Fizzbuzz' is printed instead.

for number in xrange(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print "Fizzbuzz"
    elif number % 3 == 0:
        print "Fizz"
    elif number % 5 == 0:
        print "Buzz"
    else:
        print number
