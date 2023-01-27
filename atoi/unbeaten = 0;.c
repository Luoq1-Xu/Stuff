unbeaten = 0;
            currentunbeaten = 0;
            counter = 0;
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