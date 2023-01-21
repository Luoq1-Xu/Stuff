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

    int x = 4;

    int y = 4 + (2*(h-1));

    int i = 0;

    while (i<y)
    {
        while (i<(y+2))
        {
            printf("#");
            i++;
        }
        while (i == (y/2) || i == ((y/2)+1) )
        {
            printf(" ");
            i++;
        }
        if (i > ( (y/2)+1 ))
        {
            printf("#");
            i++;
        }


        }

        printf("\n");






}