#include "helpers.h"
#include <math.h>


void cornerpixel(int a, int b, int c, int d, int height, int width, RGBTRIPLE image[height][width], RGBTRIPLE newpixel[height][width]);
void boundaryrowpixel(int a, int b, int c, int d, int e, int height, int width, RGBTRIPLE image[height][width], RGBTRIPLE newpixel[height][width]);
void boundarycolumnpixel(int a, int b, int c, int d, int e, int height, int width, RGBTRIPLE image[height][width], RGBTRIPLE newpixel[height][width]);
void allotherpixels(int a, int b, int height, int width, RGBTRIPLE image[height][width], RGBTRIPLE newpixel[height][width]);


void centrepixeledge(int a, int b, int height, int width, RGBTRIPLE image[height][width], RGBTRIPLE newpixel[height][width])

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

            image[i][j].rgbtBlue = image[i][width-j-1].rgbtBlue;
            image[i][j].rgbtGreen = image[i][width-j-1].rgbtGreen;
            image[i][j].rgbtRed = image[i][width-j-1].rgbtRed;

            image[i][width-j-1].rgbtBlue = tempblue;
            image[i][width-j-1].rgbtGreen = tempgreen;
            image[i][width-j-1].rgbtRed = tempred;
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
                cornerpixel (a, b, c, d, height, width, image, newpixel);
            }
            //Top right pixel
            else if (i == 0 && j == width-1)
            {
                int a = 0;
                int b = width-1;
                int c = width-2;
                int d = 1;
                cornerpixel (a, b, c, d, height, width, image, newpixel);
            }
            //Top row pixel but not top corners
            else if (i == 0)
            {
                int a = 0;
                int b = j;
                int c = j - 1;
                int d = j + 1;
                int e = 1;
                boundaryrowpixel(a, b, c, d, e, height, width, image, newpixel);
            }
            //First column but not corners
            else if (j == 0 && i !=height-1)
            {
                int a = i;
                int b = 0;
                int c = i - 1;
                int d = i + 1;
                int e = 1;
                boundarycolumnpixel (a, b, c, d, e, height, width, image, newpixel);

            }
            //Last column but not corners
            else if (j == width - 1 && i !=height-1)
            {
                int a = i;
                int b = width - 1;
                int c = i - 1;
                int d = i + 1;
                int e = width - 2;
                boundarycolumnpixel (a, b, c, d, e, height, width, image, newpixel);
            }
            //Bottom left pixel
            else if (i == height-1 && j == 0)
            {
                int a = i;
                int b = j;
                int c = j+1;
                int d = i-1;
                cornerpixel (a,b,c,d, height, width, image, newpixel);
            }
            //Bottom Right pixel
            else if (i == height-1 && j == width-1)
            {
                int a = i;
                int b = j;
                int c = j-1;
                int d = i-1;
                cornerpixel (a,b,c,d, height, width, image, newpixel);
            }
            //Bottom row pixel but not corner
            else if (i == height-1)
            {
                int a = height - 1;
                int b = j;
                int c = j - 1;
                int d = j + 1;
                int e = height - 2;
                boundaryrowpixel (a, b, c, d, e, height, width, image, newpixel);
            }
            //Rest of pixels
            else
            {
                allotherpixels(i, j, height, width, image, newpixel);
            }
        }
    }
    for (int x = 0; x < height; x++)
    {
        for (int y = 0; y < width; y++)
        {
            image[x][y] = newpixel[x][y];
        }
    }


    return;
}



// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
             if (i == 0 && j ==0)
             {

             }
            else if (i == 0 && j == width-1)
            {

            }
            

            //non border, non corner pixels

        }
    }
    return;
}














//BLUR CORNER PIXEL (4 PIXELS TO LOOK AT) - > let this corner pixle be represented by cp
// a = cp y coordinate,  b = cp x coordinate,
void cornerpixel(int a, int b, int c, int d,int height, int width, RGBTRIPLE image[height][width], RGBTRIPLE newpixel[height][width])
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
void boundaryrowpixel(int a, int b, int c, int d, int e, int height, int width, RGBTRIPLE image[height][width], RGBTRIPLE newpixel[height][width])
{
    int tempblue = round((image[a][b].rgbtBlue + image[a][c].rgbtBlue + image[a][d].rgbtBlue + image[e][b].rgbtBlue + image[e][c].rgbtBlue + image [e][d].rgbtBlue)/6.0);
    newpixel[a][b].rgbtBlue = tempblue;
    int tempgreen = round((image[a][b].rgbtGreen + image[a][c].rgbtGreen + image[a][d].rgbtGreen + image[e][b].rgbtGreen + image[e][c].rgbtGreen + image [e][d].rgbtGreen)/6.0);
    newpixel[a][b].rgbtGreen = tempgreen;
    int tempred = round((image[a][b].rgbtRed + image[a][c].rgbtRed + image[a][d].rgbtRed + image[e][b].rgbtRed + image[e][c].rgbtRed + image [e][d].rgbtRed)/6.0);
    newpixel[a][b].rgbtRed = tempred;
    return;
}

void boundarycolumnpixel(int a, int b, int c, int d, int e, int height, int width, RGBTRIPLE image[height][width], RGBTRIPLE newpixel[height][width])
{
    int tempblue = round((image[a][b].rgbtBlue + image[c][b].rgbtBlue + image[d][b].rgbtBlue + image[a][e].rgbtBlue + image[c][e].rgbtBlue + image[d][e].rgbtBlue)/6.0);
    newpixel[a][b].rgbtBlue = tempblue;
    int tempgreen = round((image[a][b].rgbtGreen + image[c][b].rgbtGreen + image[d][b].rgbtGreen + image[a][e].rgbtGreen + image[c][e].rgbtGreen + image[d][e].rgbtGreen)/6.0);
    newpixel[a][b].rgbtGreen = tempgreen;
    int tempred = round((image[a][b].rgbtRed + image[c][b].rgbtRed + image[d][b].rgbtRed + image[a][e].rgbtRed + image[c][e].rgbtRed + image[d][e].rgbtRed)/6.0);
    newpixel[a][b].rgbtRed = tempred;
    return;
}

void allotherpixels(int a, int b, int height, int width, RGBTRIPLE image[height][width], RGBTRIPLE newpixel[height][width])
{
    int tempblue = round((image[a][b].rgbtBlue + image[a][b-1].rgbtBlue + image[a][b+1].rgbtBlue + image[a-1][b-1].rgbtBlue + image[a-1][b].rgbtBlue + image[a-1][b+1].rgbtBlue + image[a+1][b-1].rgbtBlue + image[a+1][b].rgbtBlue + image[a+1][b+1].rgbtBlue)/9.0);
    newpixel[a][b].rgbtBlue = tempblue;
    int tempgreen = round((image[a][b].rgbtGreen + image[a][b-1].rgbtGreen + image[a][b+1].rgbtGreen + image[a-1][b-1].rgbtGreen + image[a-1][b].rgbtGreen + image[a-1][b+1].rgbtGreen + image[a+1][b-1].rgbtGreen + image[a+1][b].rgbtGreen + image[a+1][b+1].rgbtGreen)/9.0);
    newpixel[a][b].rgbtGreen = tempgreen;
    int tempred = round((image[a][b].rgbtRed + image[a][b-1].rgbtRed + image[a][b+1].rgbtRed + image[a-1][b-1].rgbtRed + image[a-1][b].rgbtRed + image[a-1][b+1].rgbtRed + image[a+1][b-1].rgbtRed + image[a+1][b].rgbtRed + image[a+1][b+1].rgbtRed)/9.0);
    newpixel[a][b].rgbtRed = tempred;
    return;
}


void centrepixeledge(int a, int b, int height, int width, RGBTRIPLE image[height][width], RGBTRIPLE newpixel[height][width])
{
    int gxblue = round(((image[a][b-1].rgbtBlue)*(-2) + (image[a][b+1].rgbtBlue)*(2) + (image[a-1][b-1].rgbtBlue)*(-1) + image[a-1][b+1].rgbtBlue + (image[a+1][b-1].rgbtBlue)*(-1) + image[a+1][b+1].rgbtBlue));

    int gyblue = round(((image[a-1][b-1].rgbtBlue)*(-1) + (image[a-1][b].rgbtBlue)*(-2) + (image[a-1][b+1].rgbtBlue)*(-1) + image[a+1][b-1].rgbtBlue + (image[a+1][b].rgbtBlue)*(-2) + image[a+1][b+1].rgbtBlue));

    int finalblue = round(sqrt((gxblue^2))+((gyblue^2)));

    if (finalblue > 255)
    {
        finalblue = 255;
    }



    int gxgreen = round(((image[a][b-1].rgbtGreen)*(-2) + (image[a][b+1].rgbtGreen)*(2) + (image[a-1][b-1].rgbtGreen)*(-1) + image[a-1][b+1].rgbtGreen + (image[a+1][b-1].rgbtGreen)*(-1) + image[a+1][b+1].rgbtGreen));

    int gygreen = round(((image[a-1][b-1].rgbtGreen)*(-1) + (image[a-1][b].rgbtGreen)*(-2) + (image[a-1][b+1].rgbtGreen)*(-1) + image[a+1][b-1].rgbtGreen + (image[a+1][b].rgbtGreen)*(-2) + image[a+1][b+1].rgbtGreen));

    int finalgreen = round(sqrt((gxgreen^2))+((gygreen^2)));

    if (finalgreen > 255)
    {
        finalgreen = 255;
    }




    int gxred = round(((image[a][b-1].rgbtRed)*(-2) + (image[a][b+1].rgbtRed)*(2) + (image[a-1][b-1].rgbtRed)*(-1) + image[a-1][b+1].rgbtRed + (image[a+1][b-1].rgbtRed)*(-1) + image[a+1][b+1].rgbtRed));

    int gyred = round(((image[a-1][b-1].rgbtRed)*(-1) + (image[a-1][b].rgbtRed)*(-2) + (image[a-1][b+1].rgbtRed)*(-1) + image[a+1][b-1].rgbtRed + (image[a+1][b].rgbtRed)*(-2) + image[a+1][b+1].rgbtRed));

    int finalred = round(sqrt((gxred^2))+((gyred^2)));

    if (finalred > 255)
    {
        finalred = 255;
    }

    newpixel[a][b].rgbtBlue = finalblue;
    newpixel[a][b].rgbtGreen = finalgreen;
    newpixel[a][b].rgbtRed = finalred;

    return;
}
