#include <cs50.h>
#include <stdio.h>

int main(void)
{
  // Set Variable n to be the actual credit card number
  long n;

    n = get_long("Credit Card Number Please. ");

    float y = (float) n;

  // Set Variable M to be the length of the credit card number
  int j;

  for (j=0;y>1;j++)
  {
    y = (y/10);
  }

  j = j+1;

  //j is the number of digits.



}