#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>


int main(int argc, string argv[])
{

    //Rejecting key if more or less than 1 string.
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    else
    {
        //Forcing key to all lowercase and then checking if string is valid.
        int length = strlen(argv[1]);

        string x = argv[1];

        int y;
        int k = 0;
        int b = 0;
        int j = length;
        int counter = 0;

        for (int v = 0 ; v < j; v++)
        {
            x[v] = tolower(x[v]);
        }

        //This part is checking if all characters are alphabets - k is non zero if there are non-alphabet characters.
        for (int i = 0 ; i < j; i++)
        {
            y = isalpha(x[i]);
            if (y == 0)
            {
                k++;
            }
        }

        //Checking if there are duplicate characters. Individually take each character and check if it matches with every character in the string
        //By right every character should match exactly once if there are no duplicates, thus the counter should be 26.
        for (int w = 0; w < j; w++)
        {
            for (int e = 0; e < j; e++)
            {
                if (x[w] == x [e])
                {
                    counter ++;
                }
            }
        }



        //Rejecting the key if not 26 characters OR not all alphabets OR duplicated characters
        if (length != 26 || k != 0 || counter != 26)
        {
            printf("Key must contain 26 characters.\n");
            return 1;
        }

        //Taking each character and changing it to follow the equivalent value of the key (forcing everything to lowercase for easy manipulation then changing back later if required)
        //Example: alphabet a in the plaintext will take on the value of the ((ASCII NUMBER:97)-97)th char in the key so a becomes the first character in the key
        else
        {
            string plaintext = get_string("plaintext:  ");

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
            printf("ciphertext: %s\n", p);
            return 0;
        }

    }

}

