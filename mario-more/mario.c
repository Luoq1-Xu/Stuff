#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int h;
    do
    {
         h = get_int("Height: ");
    }
    while ( h<1 || h>8);

    int y = 4 + (2*(h-1));

    int i = 0;

    int l = (h-1);

    int k = 0;

    while (k<h)
    {
        while (i<l)
        {
            printf(" ");
            i++;
        }
        while (((l-1) < i) && (i < ((y/2)-1)) )
        {
            printf("#");
            i++;
        }
        while ( (((y/2)-2) < i) && (i < ((y/2)+1)) )
        {
            printf(" ");
            i++;
        }
        while ( ((y/2)<i) && (i< (y-l)) )
        {
            printf("#");
            i++;
        }
        printf("\n");
        k++;
        i = 0;
        l = (l-1);

    }

}





