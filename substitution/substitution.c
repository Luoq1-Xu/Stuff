#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

string get_plaintext(void);

int main(int argc, string argv[])
{

  string plaintext = get_plaintext();

}




//Program to check if key is valid and subsequently getting the plaintext (if key is valid)

string get_plaintext(void)
{
    if (argc != 2)
    {
         printf("Usage: ./substitution key\n");
        return 1;
    }

    else
    {
        int length = strlen (argv[1]);

        string x = argv[1];

        int y;
        int k=0;

        for (int i = 0, j = strlen(argv[1]); i < j; i++)
        {
            y = isalpha(x[i]);
            if (y == 0)
            {
                k++;
            }
        }


        if (length != 26 || k != 0)
        {
            printf("Key must contain 26 characters.\n");
            return 1;
        }
        else
        {
             string plaintext = get_string("plaintext: \n");
        }

    }
    return plaintext;
}

