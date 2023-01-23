#include <cs50.h>
#include <stdio.h>

int get_creditnum(long n);

int get_validity(long creditnum);

int main(void)
{

  long n;

  //Requesting Number to check.
  n = get_long("Number: ");

  //Checking whether Card qualifies as AMEX, MASTERCARD, VISA or none of them.
  int valid = get_creditnum(n);

  //Function to check checksum is correct. c is 1 if checksum is valid and 0 if checksum is invalid.
  int c = get_validity(n);


  //Final classification of which brand card id or invalid(due to wrong length of number like 14 digits).
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























int get_creditnum(long n)
{
    //j denotes the number of digits of the number entered
    int j;
    //valid classifies whether the card could one of AMEX, MASTERCARD, VISA, or is an INVALID number
    int valid;


        long r = n;


        float y = (float) n;

        j=0;

        for (j=0;y>=1;j++)
        {
            y = (y/10);
        }

        for (int u=0;u<(j-2);u++)
        {
          r = (r/10);
        }

        // Classifying into AMEX, MASTERCARD, VISA, or INVALID by checking the first 2 digits of the number
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
        }

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

  //calculating the total sum of the digits of the products of the alternating digits multiplied by 2.
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
   v = (v/10);

  }


  //sumofremaindigit denotes the sum of the remaining digits that weren't multiplied by 2.
  int sumofremaindigit = 0;



  while(e>=1)
  {

    sumofremaindigit = sumofremaindigit + (e % 10);
    e = e/10;
    e = e/10;

  }


  //o denotes the final sum of all relevant digits. Checking if last digit of o is zero or not.
  int o = totalsumofproductdigit + sumofremaindigit;

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



