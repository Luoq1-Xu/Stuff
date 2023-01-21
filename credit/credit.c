#include <cs50.h>
#include <stdio.h>

int main(void)
{
  // Set Variable n to be the actual credit card number
  long n;

  //Get a variable for the numberof digits of the credit card number (n)

  do
  {
    n = get_long("Credit Card Number Please. ");
  }
  while ((n<1) && (n<13) && (n==14) && (n>16));
}