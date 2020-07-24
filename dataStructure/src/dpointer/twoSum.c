#include "ds_dpointer.h"


/*
 * 暴力
 */

/**
 *  * Note: The returned array must be malloced, assume caller calls free().
 **/
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize){
    int index1 = 0, index2 = 0;
    int * pointer= NULL;

    *returnSize = 0;

    if( numbersSize < 2 ){
        return pointer;
    }

    for( index1 = 0; index1 < numbersSize - 1; index1++ ){
        for( index2 = index1 + 1; index2 < numbersSize; index2++ ){
            printf( "(index1,2)[%d,%d]\n", index1, index2 );
            if( numbers[index1] + numbers[index2] > target ){
                break;
            }
            if( target == numbers[index1] + numbers[index2] ){
                pointer = ( int* )malloc( sizeof( int ) * 2 );
                pointer[0] = index1+1;
                pointer[1] = index2+1;
                printf( "(index1,2)[%d,%d]\n", index1, index2 );
                *returnSize = 2;
                return pointer;
            }
        }
    }

    return pointer;
}

/*
 * 双指针
 */
int* twoSum2(int* numbers, int numbersSize, int target, int* returnSize){
    int index1 = 0, index2 = numbersSize - 1;
    int sum = 0;
    int * pointer= NULL;

    *returnSize = 0;
    while( index1 < index2 ){
        sum = numbers[index1] + numbers[index2];
        if( target == sum ){
            pointer = ( int* )malloc( sizeof( int ) * 2 );
            pointer[0] = index1+1;
            pointer[1] = index2+1;
            printf( "(index1,2)[%d,%d]\n", index1, index2 );
            *returnSize = 2;
            return pointer;
        }else 
            if( target > sum ){
                index1++;
            }else{
                index2--;
            }
    }

    return pointer;
}

/*
 * 二分
 */
int* twoSum3(int* numbers, int numbersSize, int target, int* returnSize){
    int i = 0;
    int index1 = 0, index2 = numbersSize - 1;
    int mid = index1 + index2 / 2;
    int * pointer= NULL;

    printf( "numbersSize[%d,%d]\n", numbersSize, target );
    for( i = 0; i < numbersSize - 1; i++ ){
        index1 = i;
        index2 = numbersSize - 1;
        printf( "(for index1,2)[%d,%d]\n", index1, index2 );
        while( index1 < index2 ){
            mid = index1 + ( ( index2 - index1 ) >> 1 );
            printf( "(index1,2)[%d,%d]m[%d]\n", index1, index2, mid );
            if( target == numbers[index1] + numbers[index2] ){
                pointer = ( int* )malloc( sizeof( int ) * 2 );
                pointer[0] = index1+1;
                pointer[1] = index2+1;
                printf( "(index1,2)[%d,%d]\n", index1, index2 );
                *returnSize = 2;
                return pointer;
            }else
            if( target < numbers[index1] + numbers[index2] ){
                index2 = mid - 1;
            }else{
                index1 = mid + 1;
            }

            /*
            if( target == numbers[index1] + numbers[index2] ){
                pointer = ( int* )malloc( sizeof( int ) * 2 );
                pointer[0] = index1+1;
                pointer[1] = index2+1;
                printf( "(index1,2)[%d,%d]\n", index1, index2 );
                *returnSize = 2;
                return pointer;
            }else
            if( (numbers[index1] + numbers[index2]) < target ){
                index1 = mid + 1;
            }else{
                index2 = mid;
            }
            */
        }
    }

    return pointer;
}
