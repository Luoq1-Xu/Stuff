#include <cs50.h>
#include <stdio.h>

int count_letters(string text);

int main(void)
{
   string text = get_string("Text: ");

   int letters = count_letters(text);

   printf("%i letters\n",letters);
}










int count_letters(string text)
{
    int letters=0;

    for (int i=0;text[i] != '\0'; i++)
    {
        if (((text[i] >= 65) && (text[i] <= 90)) || ((text[i] >=97) && (text[i] <=122)))
        {
            letters ++;
        }
    }
    return letters;
}


