#include <stdio.h>
#include <stdbool.h>

/*
 * 暴力
 */
int containsDuplicate(int* nums, int numsSize){
    int  i, j = 0;

    if( NULL == nums || 2 > numsSize ){
        return false;
    }

    for( i = 0; i < numsSize; i++ ){
        for( j = i+1; j < numsSize; j++){
            if( nums[i] == nums[j] ){
                return true;
            }
        }
    }

    return false;
}

extern int bubbleSort( int* nums, int numsSize );

/*
 * 排序后处理
 */
int containsDuplicate1(int* nums, int numsSize){
    
    bubbleSort( nums, numsSize );

    for( int i = 0; i < numsSize - 1; i++ ){
        if( nums[i] == nums[i+1] ){
            return true;
        }
    }
    
    return false;
}

