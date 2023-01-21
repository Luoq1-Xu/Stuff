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

        int r = (int) n;


        float y = (float) n;

        j=0;

        for (j=0;y>=1;j++)
        {
            y = (y/10);
        }

        printf("%i\n",j);

        for (int u=0;u<(j-2);u++)
        {
          r = r/10;
        }




        printf("%i\n",r);

        if ( ((r==34) || (r==37)) && j == 15)
        {
          valid = 1;
        }
        else if ( ((r>50) && (r<56)) && j == 16 )
        {
          valid = 2;
        }
        else if ( ((r>39) && (r<50)) && ((j ==13) || (j==16)) )
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