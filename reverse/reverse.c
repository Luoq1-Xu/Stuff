#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include "wav.h"

int check_format(WAVHEADER header);
int get_block_size(WAVHEADER header);
int checkwav(char input[]);

int main(int argc, char *argv[])
{
    // Ensure proper usage
    // TODO #1
    if (argc != 3)
    {
        printf("Usage: ./reverse input.wav output.wav\n");
        return 1;
    }
    if ((checkwav(argv[1])) == 0)
    {
        printf("Input is not a WAV file.\n");
        return 2;
    }

    char *infile = argv[1];
    char *outfile = argv[2];
    // Open input file for reading
    // TODO #2
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
         printf("Could not open %s.\n", infile);
         return 1;
    }

    // Read header into an array
    // TODO #3
    fread()

    // Use check_format to ensure WAV format
    // TODO #4

    // Open output file for writing
    // TODO #5

    // Write header to file
    // TODO #6

    // Use get_block_size to calculate size of block
    // TODO #7

    // Write reversed audio to file
    // TODO #8
}

int check_format(WAVHEADER header)
{
    // TODO #4
    return 0;
}

int get_block_size(WAVHEADER header)
{
    // TODO #7
    return 0;
}

int checkwav(char input[])
{
    int temp = 0;
    int i = 0;
    do
    {
        if (input[i] == '.')
        {
            temp = i;
        }

        i++;
    }
    while (input[i] != '\0');

    if (input[temp + 1] == 'w' && input[temp + 2] == 'a' && input[temp + 3] == 'v' && input [temp + 4] == '\0')
    {
        return 1;
    }
    else
    {
        return 0;
    }
}