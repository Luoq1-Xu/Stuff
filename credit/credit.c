#include <cs50.h>
#include <stdio.h>

int main(void)
{
  // Set Variable n to be the actual credit card number
  long n;

    do
    {
        n = get_long("Credit Card Number Please. ");
    }
    while((j<13) && (j==15) && (j>16));

  int j;
  float y = (float) n;
  for (j=0;y>1;j++)
  {
    y = (y/10);
  }

  j = j+1;


  // Set Variable M to be the length of the credit card number



  //j is the number of digits.



}