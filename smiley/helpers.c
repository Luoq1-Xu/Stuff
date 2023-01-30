#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // Change all black pixels to a color of your choosing
    // Cycle through rows
    for (int i = 0, n = height; i < n; i++)
    {
        // Cycling through each pixel in each row
        for (int j = 0, m = width; j < m; j++)
        {
            // If pixel is black (all values of rgb will be zero)
            if (image[i][j].rgbtBlue == 0x00 && image[i][j].rgbtGreen == 0x00 && image[i][j].rgbtRed == 0x00)
            {
                //Change each pixel rgb values
                image[i][j].rgbtBlue = 0xff;
                image[i][j].rgbtGreen = 0x00;
                image[i][j].rgbtRed = 0x00;
            }
        }
    }
}
