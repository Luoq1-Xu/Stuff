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
        
    }

    return false;
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
