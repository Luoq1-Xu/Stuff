#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>


int main(int argc, string argv[])
{

    int length = strlen (argv[1]);

    if (argc != 2)
    {
         printf("Usage: ./substitution key\n");
        return 1;
    }
    else if ( length != 26)
    {
         printf("Key must contain 26 characters.\n");
        return 1;
    }

    string plaintext = get_string("plaintext: \n");

}




//Program to read the input

