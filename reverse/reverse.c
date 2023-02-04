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
         return 3;
    }

    // Read header into an array
    // TODO #3
    WAVHEADER header;
    fread(&header, sizeof(WAVHEADER), 1, inptr);

    // Use check_format to ensure WAV format
    // TODO #4
    if (check_format(header) == 0)
    {
        printf("Invalid Format :(\n");
        return 4;
    }

    // Open output file for writing
    // TODO #5
    FILE *outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        printf("Failed to create output file.\n");
        return 5;
    }

    // Write header to file
    // TODO #6
    fwrite(&header, sizeof(WAVHEADER), 1, outptr);


    // Use get_block_size to calculate size of block
    // TODO #7
    int blocksize = get_block_size(header)

    // Write reversed audio to file
    // TODO #8
    temp[blocksize];
    int i = 0;
    do
    {
    fseek(*inptr, blocksize, SEEK_END);
    fread(temp, blocksize, 1, *inptr);
    fwrite(temp, blocksize, 1, *outptr);
    i++;
    }

}

int check_format(WAVHEADER header)
{
    // TODO #4
    if(header.format[0] == 'W' && header.format[1] == 'A' && header.format[2] == 'V' && header.format[3] == 'E')
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int get_block_size(WAVHEADER header)
{
    // TODO #7
    int blocksize = header.numChannels * (header.bitsPerSample/8)
    return blocksize;
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