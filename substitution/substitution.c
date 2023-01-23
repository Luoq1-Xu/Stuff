#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>


int main(int argc, string argv[])
{

    if (argc != 2)
    {
         printf("Usage: ./substitution key\n");
        return 1;
    }
    else
    {
        int length = strlen (argv[1]);

        string x = argv[1]

        do
        {
        for (int i = 0, j = strlen(argv[1]); i < j; i++)
        {
             int y = isalpha(x[i]);
        }
        }

        if (length != 26)
        {
            printf("Key must contain 26 characters.\n");
            return 1;
        }


    }

    string plaintext = get_string("plaintext: \n");

}




//Program to read the input

