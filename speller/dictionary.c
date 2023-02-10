// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>

#include "dictionary.h"

bool stringcompare(char *primaryword, char *string2);

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Traversing pointer
node *trav;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    if (trav->next == NULL)
    {
        if (!stringcompare(word, trav->word))
        {
            return false;
        }
        else
        {
            return true;
        }
    }
    else if
    {
        if(!stringcompare(word, trav->word))
        {
            check(word);
        }
        else
        {
            return true;
        }
    }


}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *inptr = fopen(dictionary, "r");
    if (inptr == NULL)
    {
        return false;
    }

    char c;
    char tempword[LENGTH + 1];
    int counter = 0;
    int key = NULL;
    node *point;
    point = table;



    while (fread(&c, sizeof(char), 1, inptr))
    {
        if (c != '\n')
        {
            tempword[counter] = c;
            counter++;
        }
        else if (c == '\n')
        {
            tempword[counter + 1] = '\0'
            key = hash(word);
            point = table[key];

            while (point->next != NULL)
            {
                point = point->next;
            }

            if (point->word[0] < 97 || point->word[0] > 122)
            {
                for(int i =0; i < counter + 2; i++)
                {
                    point->word[i] = tempword[i];
                }
                counter = 0;
            }
            else
            {
                node *temp = malloc(sizeof(node));
                if (temp == NULL)
                {
                    return false;
                }
                temp->next = point;
                point = temp;
            }
            
        }

    return false;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    return false;
}








bool stringcompare(char *primaryword, char *string2)
{
    int i = 0;
    do
    {
        if(primaryword[i]!= string2[i])
        {
            return false;
        }
        i++
    }
    while (primaryword[i] != '\0');

    if (string2[i] != '\0')
    {
        return false;
    }
    else
    {
        return true;
    }
}

