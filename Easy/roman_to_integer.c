unsigned int table[90] = {
    ['I'] = 1,
    ['V'] = 5,
    ['X'] = 10,
    ['L'] = 50,
    ['C'] = 100,
    ['D'] = 500,
    ['M'] = 1000
};

int romanToInt(char * s){
    int res = 0;
    char next;
    while (*s != '\0')
    {
        next = *(s+1);
        if (table[*s]<table[next])
        {
            res -= table[*s];
        }else{
            res += table[*s];
        }
        s++;
        
    }
    return res;
}