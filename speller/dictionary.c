// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include <string.h>
#include <math.h>

#include "dictionary.h"

bool loadfinish = false;
int words = 0;

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

void destroy(node *list);

// TODO: Choose number of buckets in hash table
const unsigned int N = 7393;

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

    //If no word at the root of the table at all, means no words there, thus no hit,
    if (trav == NULL)
    {
        return false;
    }
    else
    {
        //For pointer to keep travelling along the linked list
        while (trav->next != NULL)
        {
            //If a match is found immediately end search
            if (strcasecmp(word, trav->word) == 0)
            {
                return true;
            }
            //If current node no hit, go to the next node and keep searching
            else
            {
                trav = trav->next;
            }
        }
        //End of the list, here is the last node (where trav->next == NULL)
        if (strcasecmp(word, trav->word) == 0)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    //Hash function
    int counter = 0;
    for (int i = 0, j = strlen(word); i < j; i ++)
    {
        {
            counter += tolower(word[i]) * tolower(word[i]) * 83;
        }
    }
    unsigned int key = round(((counter * strlen(word))) % 7393);
    return key;
}


// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    //Open dictionary for reading
    FILE *inptr = fopen(dictionary, "r");
    if (inptr == NULL)
    {
        return false;
    }

    char c;
    char tempword[LENGTH + 1];
    int counter = 0;
    int key = 0;

    //Read character by character, the file onto an array (temporary storage for the current word)
    while (fread(&c, sizeof(char), 1, inptr))
    {
        if (c != '\n')
        {
            tempword[counter] = c;
            counter++;
        }
        //Once hit end of the line, stop reading and terminate current word. tempword is now the current word in entirety
        else if (c == '\n')
        {
            tempword[counter] = '\0';
            key = hash(tempword);

            //Check if the current root of the table is already occupied or not
            if (table[key] == NULL)
            {
                node *temp = malloc(sizeof(node));
                if (temp == NULL)
                {
                    return false;
                }
                table[key] = temp;
                table[key]->next = NULL;

                for (int i = 0; i < counter + 1; i++)
                {
                    temp->word[i] = tempword[i];
                }
                words++;
                counter = 0;
            }
            //If current root of table is already occupied, just add on a new node storing the current word, to become the new root
            else
            {
                node *temp = malloc(sizeof(node));
                if (temp == NULL)
                {
                    return false;
                }
                temp->next = table[key];
                table[key] = temp;

                for (int i = 0; i < counter + 1; i++)
                {
                    temp->word[i] = tempword[i];
                }
                counter = 0;
                words++;
            }

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
    if (loadfinish == false)
    {
        return 0;
    }
    else
    {
        return words;
    }
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        destroy(table[i]);
    }
    return true;
}









void destroy(node *list)
{
    if (list == NULL)
    {
        return;
    }
    else if (list->next == NULL)
    {
        free(list);
        return;
    }
    else
    {
        destroy(list->next);
        free(list);
        return;
    }
}

