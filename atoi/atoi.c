#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int convert(string input);

int main(void)
{
    string input = get_string("Enter a positive integer: ");

    for (int i = 0, n = strlen(input); i < n; i++)
    {
        if (!isdigit(input[i]))
        {
            printf("Invalid Input!\n");
            return 1;
        }
    }

    // Convert string to int
    printf("%i\n", convert(input));
}

int convert(string input)
{
    int output = 0;
    for (int i = 0; i < strlen(input); i++)
    {
        if(strlen(input) == 0)
        {
            return 0;
        }
        else
        {
            int mutiplier = 1;
            for (j = 0; j < strlen(input); j++)
            {
                multiplier *= 10;
            }
            output = input[strlen(input)]*multiplier;
        }
    }
}