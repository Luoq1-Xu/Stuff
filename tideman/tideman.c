#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
}
pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);


int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);

        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}




// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    // TODO
    for (int y = 0; y < candidate_count; y++)
    {
        if (strcmp (name, candidates[y]) == 0)
        {
            ranks[rank] = y;
            return true;
        }
    }
    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = i + 1; j < candidate_count; j++)
        {
             preferences[ranks[i]][ranks[j]]++;
        }
    }
    // TODO
    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    // TODO
    for (int i = 0; i < candidate_count ; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            if (preferences[i][j] > preferences[j][i])
            {
                pairs[pair_count].winner = i;
                pairs[pair_count].loser = j;
                pair_count++;
            }
        }
    }
    return;
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    // TODO
    pair small;
    pair big;
    for (int i = 0; i < pair_count; i++)
    {
        for (int j = 0; j < pair_count; j++)
        {
            if ((preferences[pairs[i].winner][pairs[i].loser]) > (preferences[pairs[j].winner][pairs[j].loser]))
            {
                big = pairs[i];
                small = pairs[j];
                pairs[i] = small;
                pairs[j] = big;
            }
        }
    }

    return;
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    // TODO
    int unbeaten = 0;
    int counter = 0;
    int currentunbeaten = 0;
    for (int i = 0; i < pair_count; i++)
        {
            unbeaten = 0;
            currentunbeaten = 0;
            counter = 0;
            //Checking for unbeaten candidates
            for (int j = 0; j < candidate_count; j++)
            {
                for (int k = 0; k < candidate_count; k++)
                {
                    if (locked[k][j] == false)
                    {
                        counter++;
                    }
                }
                if (counter == candidate_count)
                {
                    unbeaten++;
                    counter = 0;
                }
                if (counter == candidate_count && unbeaten == 0)
                {
                    unbeaten++;
                    currentunbeaten = j;
                    counter = 0;
                }
                else
                {
                    counter = 0;
                }
             }

            if (unbeaten > 1)
            {
                locked[pairs[i].winner][pairs[i].loser] = true;
            }
            else if (unbeaten == 1)
            {
                if (pairs[i].loser != currentunbeaten)
                {
                    locked[pairs[i].winner][pairs[i].loser] = true;
                }
            }
        }
    return;
}

// Print the winner of the election
void print_winner(void)
{
    // TODO
    int counter = 0;
    int winner = 0;
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            if (locked[j][i] == true)
            {
                counter++;
            }
        }
        if (counter == 0)
        {
            winner = i;
            i = candidate_count;
        }
        else
        {
            counter = 0;
        }
    }
    printf("%s\n",candidates[winner]);
    return;
}


int checkbase(int currentloser)
{
    int counter = 0;
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            if (locked[j][i] == false)
            {
                counter++
            }
        }
    }
}