// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "dictionary.h"

bool loadfinish = false;

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

void destroy(node *list);

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
    int key = hash(word);
    trav = table[key];
    while (trav->next != NULL)
    {
        if (strcasecmp(word, trav->word) == 0)
        {
            return true;
        }
        else
        {
            trav = trav->next;
        }
    }
    if (strcasecmp(word, trav->word) == 0)
    {
        return true;
    }
    else
    {
        return false;
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
    int key = 0;


    while (fread(&c, sizeof(char), 1, inptr))
    {
        if (c != '\n')
        {
            tempword[counter] = c;
            counter++;
        }
        else if (c == '\n')
        {
            key = hash(tempword);
            point = table[key];


            node *temp = malloc(sizeof(node));
            if (temp == NULL)
            {
                return false;
            }
            temp->next = table[key];
            table[key] = temp;

            for (int i = 0; i < counter; i++)
            {
                temp->word[i] = tempword[i];
            }
            counter = 0;
        }

    }
    fclose(inptr);
    loadfinish = true;
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    int words = 0;
    node *point;

    if (loadfinish == false)
    {
        return 0;
    }
    else
    {
        for (int i = 0; i < N; i++ )
        {
            point = table[i];
            while (point->next != NULL)
            {
                words++;
                point = point->next;
            }
            if (isalpha(point->word[0]) != 0)
            {
                words++;
            }
        }
        return words;
    }
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N + 1; i++)
    {
        destroy(table[i]);
    }
    for (int j = 0; j < N + 1; j++)
    {
        if (table[j] != NULL)
        return false;
    }
    return true;
}









void destroy(node *list)
{
    if(list->next == NULL)
    {
        free(list);
        return;
    }
    else
    {
        destroy(list->next);
    }
}

