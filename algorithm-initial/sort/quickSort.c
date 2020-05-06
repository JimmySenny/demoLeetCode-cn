#include <stdio.h>
#include <stdbool.h>


/*
 * 快速排序(quickSort)
 */

// 挖坑填数
int quickSortAdjust(int* nums, int numsSize, int indx_left, int indx_right ){
//    int indx_left = 0;
//    int indx_right = numsSize - 1;
    int temp = nums[indx_left];

    while( indx_left < indx_right ){

        //从右向左找小于temp的数 
        while( indx_left < indx_right && nums[indx_right] >= temp ){
            indx_right--;
        }
        if( indx_left < indx_right ){
            nums[indx_left] = nums[indx_right];
            indx_left++;
        }

        while( indx_left < indx_right && nums[indx_left] < temp ){
            indx_left++;
        }
        if( indx_left < indx_right ){
            nums[indx_right] = nums[indx_left];
            indx_right--;
        }

    }
    // indx_left == indx_right
    nums[indx_left] = temp;

    return true;
}

// 分治
int quickSortSample(int* nums, int numsSize, int indx_left, int indx_right ){
    if( indx_left < indx_right ){
        int i = quickSortAdjust( nums, numsSize, indx_left, indx_right );
        quickSortSample( nums, numsSize, indx_left, i - 1 );
        quickSortSample( nums, numsSize, i + 1, indx_right );
    }
}

void quickSort( int* nums, int numsSize, int indx_left, int indx_right ){
    if( indx_left < indx_right ){
        //swap( nums[indx_left], nums[(indx_left + indx_right)/2];
        int i = indx_left, j = indx_right, x = nums[indx_left];

        while( i < j ){
            while( i < j && nums[j] >= x ){
                j--;
            }
            if( i < j ){
                nums[i++] = nums[j];
            }

            while( i < j && nums[i] < x ){
                i++;
            }
            if(i < j ){
                nums[j--] = nums[i];
            }
        }
        nums[i] = x;

        quickSort( nums, numsSize, indx_left, i-1);
        quickSort( nums, numsSize, i+1, indx_right );
    }
}
