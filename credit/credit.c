#include <cs50.h>
#include <stdio.h>

long get_creditnum(void);

int get_validity(long creditnum);

int main(void)
{
  //Getting the creditcardnumber
  long n = get_creditnum();

  //Function to check checksum
  int c = get_validity(n);


  //
  printf("%i\n",c);
  
  if ((valid == 1) && c==1)
  {
    printf("AMEX\n");
  }
  else if ((valid == 2) && c==1)
  {
    printf("MASTERCARD\n");
  }
  else if ((valid ==3) && c==1)
  {
    printf("VISA\n");
  }
  else
  {
    printf("INVALID\n");
  }











}























long get_creditnum(void)
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

}


int get_validity(long creditnum)
{
  long v = creditnum;
  long e = creditnum;
  int q = 0;
  int b;
  int sumofcurrentproduct=0;
  int totalsumofproductdigit =0;


  for(int counter=0;v>=1;counter++)
  {
    v = (v/10);
    q = ((v % 10)*2);
    printf("%i\n",q);

    for (int count=0;q>=1;count++)
    {

      sumofcurrentproduct = sumofcurrentproduct + (q % 10);
      q = q/10;

    }

   totalsumofproductdigit = totalsumofproductdigit + sumofcurrentproduct;
   sumofcurrentproduct = 0;
   v = (v/10);

  }
  printf("%i\n",totalsumofproductdigit);

  int sumofremaindigit = 0;

  while(e>=1)
  {

    sumofremaindigit = sumofremaindigit + (e % 10);
    e = e/10;
    e = e/10;
    printf("%i\n",sumofremaindigit);

  }

  int o = totalsumofproductdigit + sumofremaindigit;
  printf("%i\n",o);

  int c;

  if ((o % 10)==0)
  {
     c = 1;
  }
  else
  {
     c = 0;
  }

  return c;
}



