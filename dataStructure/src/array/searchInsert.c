#include "ds_array.h"

/*
 * 暴力
 */
int searchInsert(int* nums, int numsSize, int target){
    int indx = 0;

    for( indx = 0; indx < numsSize; indx++ ){
        if( nums[indx] >= target ){
            break;
        }
    }

    return indx;
}


/*
 * 二分
 * 二分查找的思路不难理解，但是边界条件容易出错
 */
int searchInsert1( int* nums, int numsSize, int target ){
    int indx = 0;
    int left = 0, right, mid;

    right = numsSize - 1; //init right = length - 1

    while( left <= right ){
        mid = ( left + right ) / 2;
        if( nums[mid] >= target ){  //left  need equal
            right = mid - 1; // plus -1
        }else{
            left = mid + 1;  // plus  1
        }

        printf( "left[%d]:%d mid[%d]:%d right[%d]:%d\n", left, nums[left], mid, nums[mid], right, nums[right] );
    }

    indx = left;

    return indx;
}


