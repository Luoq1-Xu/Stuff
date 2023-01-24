string encrypt(string plaintext)
{
    string p = plaintext;
    string x = argv[1];
    for (int l = 0, r = strlen(p); l < r ; l++)
    {
        if (isupper(p[l]))
        {
            p[l] = x[l];
            p[l] = toupper(p[l]);
        }
        else
        {
            p[l] = x[l];
        }
    }
    return p;

}











for (int v = 0 ; v < j; v++)
             {
                x[v] = tolower(x[v]);
             }