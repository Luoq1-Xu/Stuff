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

   float L = (( (float) letters/words)*100.0);

   printf("%f\n", L);

   float S = (( (float) sentences/words)*100.0);

   printf("%f\n", S);

   float result = 0.0588 * L - 0.296 * S - 15.8;

   printf("%f\n", result);

   int index = (int) result;

   if (index > 16)
   {
    printf("Grade 16+\n");
   }

   else if (index >=1 && index <=16)
   {
    printf("Grade %i\n", index);
   }

   else if (index < 1)
   {
    printf("Before Grade 1\n");
   }



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