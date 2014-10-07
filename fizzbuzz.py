# Fizzbuzz
#
# Prints numbers from 1 to 100. If the number is divisible by 3, 'Fizz' is printed instead. If the number
# is divisible by 5, 'Buzz' is printed instead. If the number is divisible by both 3 and 5, 'Fizzbuzz' is
# printed instead.

i = 1

for i in range (1,101):
    if i%3 == 0 and i%5 == 0:
        print "Fizzbuzz"

    elif i%3 == 0:
        print "Fizz"

    elif i%5 == 0:
        print "Buzz"

    else:
        print i

    i += 1
