#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //Prompt for start size

    int j = get_int("Enter Population Start Size ");

    while(j<9)
    {
        j = get_int("Bro it has to be at least 9. ");
    }

    //Prompt for End size

    int y = get_int("Enter Population End Size: ");

    while(y<j)
    {
        y = get_int("Hey dude end size can't be less than start size. Try again. ");
    }


    // TODO: Calculate number of years until we reach threshold
    int n = 0;

    for (; j<y ; n++)
    {
         j = j + (j/3 - j/4);
    }
    // TODO: Print out answer
    printf("Years: %i", n);
}