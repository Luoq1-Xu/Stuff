#include <cs50.h>
#include <stdio.h>

int main(void)
{
  // Set Variable n to be the actual credit card number
  long n;

    n = get_long("Credit Card Number Please. ");

    int j;

    float y = (float) n;

    //calculating the number of digits in the credit card number
    
    for (j=(-1);y>1;j++)
    {
        y = (y/10);
    }


    do
    {
        n = get_long("Credit Card Number Please. ");
    }
    while((j<13) || (j==14) || (j>16));






  // Set Variable M to be the length of the credit card number



  //j is the number of digits.



}