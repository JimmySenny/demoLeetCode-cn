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

/*
 * 排序后处理
 */
int containsDuplicate1(int* nums, int numsSize){
    
    return false;
}

