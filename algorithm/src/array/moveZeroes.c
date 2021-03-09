#include "alg_array.h"

/*
 * 暴力
 */
void moveZeroes( int * nums, int numsSize ){
    int i = 0, j = 0, k = 0;
    for( i = 0; i < numsSize - k; i++ ){
        printf( "i,j, k[%d,%d,%d]\n", i, j, k );
        if( 0 == nums[i] ){
            printf( "=i,j, k[%d,%d,%d]\n", i, j, k );
            k++; // 0的个数
            for( j = i; j < numsSize - 1; j++ ){
                nums[j] = nums[j+1];
            }
            i--;   // 连续0的情况
            nums[numsSize - k] = 0; // 发现的0，结尾为0;
        }
        printNums( nums, numsSize );
    }

    /*
    for( j = 0; j < k; j++ ){
        nums[i++] = 0;
    }
    */
}

/*
 * 双指针
 */
void moveZeroes1( int * nums, int numsSize ){
    int i = 0, j = 0, k = numsSize;

    while( i < numsSize ){
        if( 0 == nums[i] ){
            i++;
            k--;
        }else{
            if( i == j ){
                i++;
                j++;
            }else{
                nums[j++] = nums[i];
                nums[i++] = 0;
            }
        }
        printNums( nums, numsSize );
    }
    while( j < numsSize ){
        nums[j++] = 0;
    }
}
