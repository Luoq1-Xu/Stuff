#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

string = encrypt(string plaintext);


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

        string x = argv[1];

        int y;
        int k = 0;

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
             for (i = 0, j = strlen(argv[1]); i < j; i++)
             {
                x[i] = tolower(x[i]);
             }
             string p;
             string p = encrypt(string plaintext);
             printf("ciphertext:%s\n", p);
        }
    }






}



//Program to encrypt cipher

string = encrypt(string plaintext)
{
    string p = plaintext
    for (int l = 0, r = strlen(p); l < p; l++)
    {
        if (isupper(p[l]))
        {
            p[l] = x[l];
            p[l] = toupper(p[l]);
        }
        else
        {
            p[l] = x[l];
        }
    }
    return p;

}

