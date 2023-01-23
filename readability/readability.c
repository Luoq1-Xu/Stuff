#include <cs50.h>
#include <stdio.h>
#include <math.h>

int count_letters(string text);

int count_words(string text);

int count_sentences(string text);

int main(void)
{

    // Asking user for string input
    string text = get_string("Text: ");

    //Calling each variable

    int letters = count_letters(text);

    int words = count_words(text);

    int sentences = count_sentences(text);


    //Calculating the grade level using the Coleman-Liau formula.

    float L = (((float) letters / words) * 100.0);

    float S = (((float) sentences / words) * 100.0);

    float result = 0.0588 * L - 0.296 * S - 15.8;

    //Rounding the result to the nearest integer

    int index = round(result);

    //Printing out the grade result

    if (index > 16)
    {
        printf("Grade 16+\n");
    }

    else if (index >= 1 && index <= 16)
    {
        printf("Grade %i\n", index);
    }

    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }



}







//Function to count letters by checking whether the ASCII number of each char in the string (which is an array itself) falls within the numbers that represent alphabets


int count_letters(string text)
{
    int letters = 0;

    for (int i = 0; text[i] != '\0'; i++)
    {
        if (((text[i] >= 65) && (text[i] <= 90)) || ((text[i] >= 97) && (text[i] <= 122)))
        {
            letters ++;
        }
    }
    return letters;
}


// Function to count number of words by counting number of spaces (and adding 1 because total number of words is one more than number of spaces).

int count_words(string text)
{
    int words = 1;

    for (int i = 0; text[i] != '\0'; i++)
    {
        if (text[i] == 32)
        {
            words ++;
        }
    }
    return words;

}


// Function to count number of sentences by counting the number of periods, exclamation marks, question marks.

int count_sentences(string text)
{
    int sentences = 0;

    for (int i = 0; text[i] != '\0'; i++)
    {
        if ((text[i] == 46) || (text[i] == 33) || (text[i] == 63))
        {
            sentences++;
        }
    }
    return sentences;

}