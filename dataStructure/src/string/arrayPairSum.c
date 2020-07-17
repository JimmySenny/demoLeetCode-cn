#include "ds_string.h"

int arrayPairSum( int * nums, int numsSize ){
    int maxSum = 0;

    printNums( nums, numsSize );
    qsort( nums, numsSize, sizeof( nums[0] ), compi );
    for( int i = 0; i < numsSize; i+=2 ){
        maxSum += nums[i];
    }
    printNums( nums, numsSize );
    printf( "[%d]\n", maxSum );

    return maxSum;
}
