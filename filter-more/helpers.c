#include "helpers.h"
#include <math.h>

void cornerpixel(int a, int b, int c, int d, int e);
void boundaryrowpixel(int a, int b, int c, int d, int e);
void boundarycolumnpixel(int a, int b, int c, int d, int e);

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
                int a = 0;
                int b = 0;
                int c = 1;
                int d = 1;
                cornerpixel (a, b, c, d, e);
            }
            //Top right pixel
            else if (i == 0 && j == width-1)
            {
                int a = 0;
                int b = width-1;
                int c = width-2;
                int d = 1;
                cornerpixel (a, b, c, d);
            }
            //Top row pixel but not top corners
            else if (i == 0)
            {
                int a = 0;
                int b = j;
                int c = j - 1;
                int d = j + 1;
                int e = 1;
                boundaryrowpixel(a, b, c, d, e)
            }
            //First column but not corners
            else if (j == 0)
            {
                int a = i;
                int b = 0;
                int c = i - 1;
                int d = i + 1;
                int e = 1;
                boundarycolumnpixel (a, b, c, d, e,)

            }
            //Last column but not corners
            else if (j == width - 1)
            {
                int a = i;
                int b = 


            }
            //Bottom left pixel
            else if (i == height-1 && j == 0 )
            {
                int a = height-1;
                int b = 0;
                int c = 1;
                int d = height-2;
                cornerpixel (a,b,c,d);

            }
            //Bottom Right pixel
            else if (i == height-1 && j == width-1)
            {
                int a = height-1;
                int b = width-1;
                int c = width-2;
                int d = height-2;
                cornerpixel (a,b,c,d)

            }
            //Bottom row pixel but not corner
            else if (i == height-1)
            {
                int a = height-1;
                int b = j;
                int c = j - 1;
                int d = j + 1;
                int e = height - 2;
                boundaryrowpixel (a, b, c, d, e)
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



//BLUR CORNER PIXEL (4 PIXELS TO LOOK AT) - > let this corner pixle be represented by cp
// a = cp y coordinate,  b = cp x coordinate,
void cornerpixel(int a, int b, int c, int d)
{
    int tempblue = round ((image[a][b].rgbtBlue + image[a][c].rgbtBlue + image[d][b].rgbtBlue + image[d][c].rgbtBlue)/4.0);
    newpixel[a][b].rgbtBlue = tempblue;
    int tempgreen = round ((image[a][b].rgbtGreen + image[a][c].rgbtGreen + image[d][b].rgbtGreen + image[d][c].rgbtGreen)/4.0);
    newpixel[a][b].rgbtGreen = tempgreen;
    int tempred = round ((image[a][b].rgbtRed + image[a][c].rgbtRed + image[d][b].rgbtRed + image[d][c].rgbtRed)/4.0);
    newpixel[a][b].rgbtRed = tempred;

    return;
}

//BLUR BOUNDARIES (6 PIXELS TO LOOK AT) - current pixle in question is represented by a,b
void boundaryrowpixel(int a, int b, int c, int d, int e)
{
    int tempblue = round((image[a][b].rgbtBlue + image[a][c].rgbtBlue + image[a][d].rgbtBlue + image[e][b].rgbtBlue + image[e][c].rgbtBlue + image [e][d].rgbtBlue)/6.0);
    newpixel[a][b].rgbtBlue = tempblue;
    int tempgreen = round((image[a][b].rgbtGreen + image[a][c].rgbtGreen + image[a][d].rgbtGreen + image[e][b].rgbtGreen + image[e][c].rgbtGreen + image [e][d].rgbtGreen)/6.0);
    newpixel[a][b].rgbtGreen = tempgreen;
    int tempred = round((image[a][b].rgbtRed + image[a][c].rgbtRed + image[a][d].rgbtRed + image[e][b].rgbtRed + image[e][c].rgbtRed + image [e][d].rgbtRed)/6.0);
    newpixel[a][b].rgbtRed = tempred;
}

void boundarycolumnpixel(int a, int b, int c, int d, int e)
{
    int tempblue = round((image[a][b].rgbtBlue + image[c][b].rgbtBlue + image[d][b].rgbtBlue + image[a][e].rgbtBlue + image[c][e].rgbtBlue + image [d][e].rgbtBlue)/6.0);
    newpixel[a][b].rgbtBlue = tempblue;
    int tempgreen = round((image[a][b].rgbtGreen + image[c][b].rgbtGreen + image[d][b].rgbtGreen + image[a][e].rgbtGreen + image[c][e].rgbtGreen + image [d][e].rgbtGreen)/6.0);
    newpixel[a][b].rgbtGreen = tempgreen;
    int tempred = round((image[a][b].rgbtRed + image[c][b].rgbtRed + image[d][b].rgbtRed + image[a][e].rgbtRed + image[c][e].rgbtRed + image [d][e].rgbtRed)/6.0);
    newpixel[a][b].rgbtRed = tempred;
}