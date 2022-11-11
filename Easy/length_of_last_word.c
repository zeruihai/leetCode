#include <stdio.h>
/*  Online Solution  100% */ 
int lengthOfLastWord(char * s){
    int i,j = 0;
    for ( i = strlen(s)-1; i >= 0; i--)
    {
        if (s[i] == ' ' && j != 0)
        {
            break;
        }

        if (s[i] != ' ')
        {
            j++;
        }
        
        
    }
    
    return j;
}