#include <cs50.h>
#include <stdio.h>

int main(void)
{
  long n;

  do
  {
    n = get_long("Credit Card Number Please. ");
  }
  while (n<1 || n>);
}