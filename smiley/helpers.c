#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // Change all black pixels to a color of your choosing
    for (int i = 0, n = height; i < n; i++)
    {
        for (int j = 0, m = width; j < m; j++)
        {
            if (RGBTRIPLE [i][j].rgbtBlue = 0x00 && RBGTRIPLE [i][j].rgbtGreen = 0x00 && RGBTRIPLE[i][j].rgbtRed = 0x00)
            {
                RGBTRIPLE [i][j].rgbtBlue = 0xf5
                RGBTRIPLE [i][j].rgbtGreen = 0xf3
                RGBTRIPLE [i][j].rgbtRed = 0xe3
            }
        }
    }
return 0;
}
