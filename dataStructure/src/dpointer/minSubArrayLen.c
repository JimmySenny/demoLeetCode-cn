#include "ds_dpointer.h"

/*
 * 暴力 392ms
 */
int minSubArrayLen( int s, int * nums, int numsSize ){
    int i = 0, j = 0, count = 0;
    int sum = 0, iRet = numsSize + 1;

    for( i = 0; i < numsSize; i++ ){
        sum = 0;
        count = 0;
        for( j = i; j < numsSize; j++ ){
            sum += nums[j];
            count++;
            if( s <= sum ){
                if( count < iRet ){
                    iRet = count;
                }
                break;
            }
        }
    }

    return iRet==(numsSize + 1)?0:iRet;
}

/*
 * 双指针 8ms
 */
int minSubArrayLen1( int s, int * nums, int numsSize ){
    int count = 0, iRet = numsSize + 1;
    int start = 0, end = 0;
    int sum = 0;

    while( end < numsSize ){
        sum += nums[end];
        while( sum >= s ){
            count = end - start + 1;
            if( count < iRet ){
                iRet = count;
            }
            sum -= nums[start];
            start++;

        }
        end++;
    }

    return iRet==(numsSize + 1)?0:iRet;
}
