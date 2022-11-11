#include <stdio.h>
#include <stdlib.h>
char * longestCommonPrefix(char ** strs, int strsSize){
     if (strsSize == 0) return "";
    if (strsSize == 1) return strs[0];
    int min = strlen(strs[0]);
    for (int i = 0; i < strsSize; i++)
    {
        if (strlen(strs[i])<min)
        {
            min = strlen(strs[i]);
        }
        
    }
    int len = 0;
    for (size_t i = 0; i < min; i++)
    {
        char tmp = strs[0][i];
        for (int j = 0; j< strsSize; j++)
        {
            if (strs[j][i] != tmp)
            {
                goto br;
            }else if (strs[j][i] == tmp && j == strsSize-1)
            {
                len++;
            }
            
            
        }
        
        
    }
    br:
    if (len > 0) {       
        strs[0][len] = '\0';
        return strs[0];
    }else{
        return "";
    }
}