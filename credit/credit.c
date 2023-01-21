#include <cs50.h>
#include <stdio.h>

int get_creditnum(void);

int get_validity(long creditnum);

int main(void)
{
  //Getting the creditcardnumber
  long n = get_creditnum();

  //Function to check checksum
  int o = get_validity(n);









}























int get_creditnum(void)
{
    long n;

    int j;

    int valid;



    //calculating the number of digits in the credit card number (denoted by j)

    {

        n = get_long("Credit Card Number Please. ");

        long r = n;


        float y = (float) n;

        j=0;

        for (j=0;y>=1;j++)
        {
            y = (y/10);
        }

        printf("%i\n",j);

        for (int u=0;u<(j-2);u++)
        {
          r = (r/10);
        }


        printf("%li\n",r);

        if ( ((r==34) || (r==37)) && j == 15)
        {
          valid = 1;
          printf("AMEX\n");
        }
        else if ( ((r>50) && (r<56)) && j == 16 )
        {
          valid = 2;
          printf("MASTERCARD\n");
        }
        else if ( ((r>39) && (r<50)) && ((j ==13) || (j==16)) )
        {
          valid = 3;
          printf("VISA\n");
        }
        else
        {
          valid = 0;
          printf("INVALID\n");
        }


    }



    return n;
    return j;
    return valid;
    printf("%li\n",n);
}


int get_validity(long creditnum)
{
  long v = creditnum;
  int q = 0;
  int b;
  int sumofcurrentproduct=0;
  int totalsumofproductdigit =0;

  printf("%li\n",creditnum);

  for(int counter=0;v>=1;counter++)
  {
    v = (v/10);
    q = ((v % 10)*2);
    for (int count=0;q>=1;count++)
    {

      sumofcurrentproduct = sumofcurrentproduct + (q % 10);
      q = q/10;

    }

   totalsumofproductdigit = totalsumofproductdigit + sumofcurrentproduct;
   sumofcurrentproduct = 0;
   printf("%i\n",totalsumofproductdigit);


  }
  int o = totalsumofproductdigit;
  return o;
}



