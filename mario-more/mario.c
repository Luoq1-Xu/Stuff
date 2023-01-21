#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int Rows;
    do
    {
         Rows = get_int("Please pick a number between 1 and 8. ");
    }
    while ( Rows<1 || Rows>8);
    
}