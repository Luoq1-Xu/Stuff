#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int w = 0; w < width; w++)
        {
            if ((image[i][w].rgbtBlue + image[i][w].rgbtGreen + image[i][w].rgbtRed)!=0)
            {
                float average1 = (image[i][w].rgbtBlue + image[i][w].rgbtGreen + image[i][w].rgbtRed)/3.0;
                int average = round(average1);
                image[i][w].rgbtBlue = average;
                image[i][w].rgbtGreen = average;
                image[i][w].rgbtRed = average;
            }
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width/2 ; j++)
        {
            int tempblue;
            int tempgreen;
            int tempred;

            tempblue = image[i][j].rgbtBlue;
            tempgreen = image[i][j].rgbtGreen;
            tempred = image[i][j].rgbtRed;

            image[i][j].rgbtBlue = image[i][width-j].rgbtBlue;
            image[i][j].rgbtGreen = image[i][width-j].rgbtGreen;
            image[i][j].rgbtRed = image[i][width-j].rgbtRed;

            image[i][width-j].rgbtBlue = tempblue;
            image[i][width-j].rgbtGreen = tempgreen;
            image[i][width-j].rgbtRed = tempred;
        }
    }

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    //Create an array to store the values of the new pixel values.
    RGBTRIPLE newpixel[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //Top left pixel
            if (i == 0 && j ==0)
            {
                int tempblue = round ()
            }
            //Top right pixel
            else if ()
            {

            }
            //Top row pixel but not top corners
            else if ()
            {

            }
            //First column but not corners
            else if ()
            {

            }
            //Last column but not corners
            else if ()
            {

            }
            //Bottom left pixel
            else if (i == height-1 && j == 0 )
            {

            }
            //Bottom Right pixel
            else if ()
            {

            }
            //Bottom row pixel but not corner
            else if ()
            {

            }
            //Rest of pixels
            else
            {

            }
        }
    }


    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
