#include "include/algorithm_initial.h"

/*
 * 暴力
 */
int compi( const void * a, const void * b ){
    const int * p = a;
    const int * q = b;

    return *p - *q;
}

int* twoSum(int * nums, int numsSize, int target, int* returnSize){
    int i = 0, j = 0, flag = false;

//    qsort( nums, numsSize, sizeof(nums[0]), compi );

    for( i = 0; i < numsSize - 1; i++ ){
        if( flag ){
            break;
        }

        for( j = i+1; j < numsSize; j++ ){

            if( target == nums[i] + nums[j] ){
                printf( "[%d-%d]\n", nums[i], nums[j] );
                nums[0] = i;
                nums[1] = j;
                flag = 1;
                break;
            }
        }
    }
    *returnSize = 2;

    return nums;
}
