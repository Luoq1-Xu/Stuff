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

    int j;

    float i;

    int valid;



    //calculating the number of digits in the credit card number (denoted by j)

    {

        n = get_long("Credit Card Number Please. ");


        float y = (float) n;

        j=0;

        for (j=0;y>=1;j++)
        {
            y = (y/10);
        }

        printf("%i\n",j);

        i = ( n/(10*(j-2)) );

        printf("%f\n",i);

        if ( ((i==34) || (i==37)) && j == 15)
        {
          valid = 1;
        }
        else if ( ((i>50) && (i<56)) && j == 16 )
        {
          valid = 2;
        }
        else if ( ((i>39) && (i<50)) && ((j ==13) || (j==16)) )
        {
          valid = 3;
        }
        else
        {
          valid = 0;
          printf("INVALID\n");
        }


    }



    return n;
    return j;
}