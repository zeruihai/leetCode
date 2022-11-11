/*  Online Solution  */
int maxSubArray(int* nums, int numsSize){
    int i, tmp, max;
    for ( i = 0, tmp = 0, max = nums[0]; i < numsSize; i++)
    {
        tmp += nums[i];

        if (tmp>max)
        {
            max = tmp;
        }

        if (tmp < 0)
        {
            tmp = 0;
        }
        
        
        
    }
    return  max;
}

/*  Online Solution  */
static int midCrossMax(int* arr, int size)
{
    int lmax, rmax, tmp, i, m = (size / 2) - 1;
    
    for (i = m, tmp = 0, lmax = arr[m]; i >= 0; i--) {
        tmp += arr[i];
        lmax = tmp > lmax ? tmp : lmax;
    }
    
    for (i = m + 1, tmp = 0, rmax = arr[m + 1]; i < size; i++) {
        tmp += arr[i];
        rmax = tmp > rmax ? tmp : rmax;
    }

    return lmax + rmax;
}

int maxSubArray(int* nums, int numsSize)
{
    int m = numsSize / 2;
    int max, l, r, c;
    
    if (numsSize == 1)
        return *nums;
    
    l = maxSubArray(nums, m);
    r = maxSubArray(nums + m, numsSize - m);
    c = midCrossMax(nums, numsSize);
    
    max = l > r ? l : r;
    max = max > c ? max : c;

    return max;
    
}