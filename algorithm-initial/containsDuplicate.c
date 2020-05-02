#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

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
extern int quickSort( int* nums, int numsSize, int l, int r );

bool compi( const void *a, const void *b ){
    const int* p = a;
    const int* q = b;

    return *p - *q;
}

/*
 * 排序后处理
 */
int containsDuplicate1(int* nums, int numsSize){
    
//    bubbleSort( nums, numsSize );
//    quickSort( nums, numsSize, 0, numsSize - 1 );
    
    qsort( nums, numsSize,sizeof(nums[0]), compi );

    for( int i = 0; i < numsSize - 1; i++ ){
        if( nums[i] == nums[i+1] ){
            return true;
        }
    }
    
    return false;
}

/*
 * 哈希处理
 */
int containsDuplicate1(int* nums, int numsSize){

}
