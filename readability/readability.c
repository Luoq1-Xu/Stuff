#include <cs50.h>
#include <stdio.h>

int count_letters(string text);

int count_words(string text);

int count_sentences(string text);

int main(void)
{
   string text = get_string("Text: ");

   int letters = count_letters(text);

   int words = count_words(text);

   int sentences = count_sentences(text);


   printf("%i letters\n",letters);

   printf("%i words \n", words);

   printf("%i sentences \n", sentences);

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


int count_words(string text)
{
    int words = 1;

    for (int i=0;text[i] != '\0'; i++)
    {
        if (text[i]==32)
        {
            words ++;
        }
    }
    return words;

}



int count_sentences(string text)
{
    int sentences = 0;

    for (int i=0;text[i] != '\0'; i++)
    {
        if ((text[i] == 46) || (text[i] == 33) || (text[i] == 63))
        {
            sentences++;
        }
    }
    return sentences;

}