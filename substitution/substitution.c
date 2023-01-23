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


        if (length != 26 || k != 0)
        {
            printf("Key must contain 26 characters.\n");
            return 1;
        }
        else
        {
             string plaintext = get_string("plaintext: ");
             for (int v = 0, j = strlen(argv[1]); v < j; v++)
             {
                x[v] = tolower(x[v]);
             }
             printf("%s\n",x);

             string p = plaintext;
             for (int l = 0, r = strlen(p); l < r ; l++)
            {
                printf("before %i ",p[l]);
                if (isupper(p[l]))
                {
                      p[l] = tolower(p[l]);
                      p[l] = x[((p[l])-96)];
                      p[l] = toupper(p[l]);
                }
                else if (islower(p[l]))
                {
                    int test = ( (p[l]) - 96 );
                    printf("test is %i\n", test);
                    p[l] = x[test];
                }
                printf("after %i\n",p[l]);
            }
                 printf("ciphertext: %s\n",p);
    }






    }

}

