#include "ds_dpointer.h"

/*
 * 暴力 滑动窗口
 */
int findMaxConsecutiveOnes( int * nums, int numsSize ){
    int i = 0, j = 0;
    int start = -1, end = -1;
    int width = 0, max = 0; 

    for( int i = 0; i < numsSize; i++ ){
        if( 0 == i && 1 == nums[i] ){
            start = i;
        }else if( 0 == i && 1 != nums[i] ){
            continue;
        }else if( 0 == nums[i-1] && 1 == nums[i] ){
            start = i;
        }

        if( numsSize - 1 == i && 1 == nums[i] ){
            end = i;
        }else if( numsSize - 1 == i && 1 != nums[i] ){
            break;
        }else if( 1 == nums[i] && 1 != nums[i+1] ){
            end = i;
        }

        if( start <= end && end == i ){
            width = end - start + 1;
            printf( "(start,end,width)[%d,%d,%d]\n", start, end, width );

            if( width > max ){
                max = width;
            }
        }
    }

    return max;
}

/*
 * 
 */
int findMaxConsecutiveOnes1( int * nums, int numsSize ){
    int start = -1, end = -1;
    int idx = 0;
    int max = 0;

    for( start = 0; start < numsSize; start++ ){
        if( 1 == nums[start] ){ // 每个开始
            end = start;
            while( end < numsSize && nums[end] != 0 ){
                end++;
            }

            printf( "(start,end,len)[%d,%d,%d]\n", start, end, end - start );
            if( end - start > max ){
                max = end - start;
            }

            start = end;
        }
    }

    return max;
}
