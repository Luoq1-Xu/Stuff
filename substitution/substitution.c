#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

string encrypt(string plaintext);


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

        int u = 0;

        for (i = 0, j = strlen(argv[1]); i < j; i++)
        {
            if
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
             string plaintext = get_string("plaintext:  ");
             for (int v = 0, j = strlen(argv[1]); v < j; v++)
             {
                x[v] = tolower(x[v]);
             }

             string p = plaintext;
             for (int l = 0, r = strlen(p); l < r ; l++)
            {
                if (isupper(p[l]))
                {
                      p[l] = tolower(p[l]);
                      p[l] = x[((p[l]) - 97)];
                      p[l] = toupper(p[l]);
                }
                else if (islower(p[l]))
                {
                    p[l] = x[((p[l]) - 97)];
                }
            }
                 printf("ciphertext: %s\n",p);
                 return 0;
    }

    }

}

