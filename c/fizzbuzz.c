/* Fizzbuzz:
 * Print numbers 1-100. If divisible by three, print "Fizz". If divisible
 * by 5, print "Buzz". If difisible by both 3 and 5, print "Fizzbuzz". */

#include <stdio.h>

int main(void)
{
    int i;
    for (i=0; i<=100; i++)
    {
        if (i % 3 == 0 && i % 5 == 0)
        {
            printf("Fizzbuzz\n");
        }
        else if (i % 3 == 0)
        {
            printf("Fizz\n");
        }
        else if (i % 5 == 0)
        {
            printf("Buzz\n");
        }
        else
        {
            printf("%d\n", i);
        }
    }
    return 0;
}
