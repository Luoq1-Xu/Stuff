#include <cs50.h>
#include <stdio.h>

int get_creditnum(void);

int main(void)
{
  //Getting the creditcardnumber
  long n = get_creditnum();









}























int get_creditnum(void)
{
    long n;

    n = get_long("Credit Card Number Please. ");

    int j;

    int i;

    int valid;

    float y = (float) n;

    //calculating the number of digits in the credit card number (denoted by j)

    for (j=(-1);y>=1;j++)
    {
        y = (y/10);
    }

    if ((j<13) || (j==14) || (j>16))
    {

    do
    {

        n = get_long("Credit Card Number Please. ");

        valid = 100;

        y = n;

        i = 0;

        j=(-1);

        for (j=(-1);y>1;j++)
        {
            y = (y/10);
        }

        i = ( n/(10*(j-2)) );

        if ( ((i==34) || (i==37)) && j == 15)
        {
          valid = 1;
        }
        else if ( ((i>50) && (i<56)) && j == 16 )
        {
          valid = 2;
        }
        else if ( ((i>39) && (i<50)) && (j ==13 || j==16) )
        {
          valid = 3;
        }
        else
        {
          valid = 0;
        }


    }


    }
    return n;
    return j;
}