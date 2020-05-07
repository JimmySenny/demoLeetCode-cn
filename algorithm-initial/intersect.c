#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "include/sort.h"

/*
 * 暴力
 */
int compi( const void *a, const void *b ){
    const int* p = a;
    const int* q = b;

    return *p - *q;
}
int* intersect(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize){
    int k = 0;
    static int j = 0;
    int * nums = NULL;
    *returnSize = 0;

    if( nums1Size > nums2Size ){
        nums = nums2;
        nums2 = nums1;
        nums1 = nums;
        nums = NULL;
        
        int tmp = nums1Size;
        nums1Size = nums2Size;
        nums2Size = tmp;
    }

    printf( "nums1Size[%d]nums2Size[%d]\n", nums1Size, nums2Size );
    nums = (int*)malloc( sizeof(int) * nums1Size + 1 );

    memset( nums, 0x00, sizeof( int ) );
    
    qsort( nums1, nums1Size, sizeof(nums1[0]), compi );
    qsort( nums2, nums2Size, sizeof(nums2[0]), compi );

    for( int i = 0; i < nums1Size; i++ ){
        for( ; j < nums2Size; j++ ){
            printf( "i[%d-%d]j[%d-%d]\n", i, nums1[i], j, nums2[j]);
            if(nums1[i] == nums2[j] ){
                (*returnSize)++;
                nums[k] = nums1[i];
                k++;
                j++;
                break;
            }
            /* nums1 中最后一个小于nums j，后面不用再比较 */
            if( nums1Size - 1 == i && 
                nums1[i] < nums2[j] ){
                return nums;
            }
            if( nums1[i] < nums2[j] ||
                nums2[j] > nums1[i] ){
                break;
            }
        }
    }

    return nums;
}

/*
 * 双指针
 */
int* intersect1(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize){
    int i = 0, j = 0, k = 0;

    qsort( nums1, nums1Size, sizeof(nums1[0]), compi );
    qsort( nums2, nums2Size, sizeof(nums2[0]), compi );
    /*
    quickSort(nums1, nums1Size, 0, nums1Size - 1 );
    quickSort(nums2, nums2Size, 0, nums2Size - 1 );
    */

    while( i < nums1Size && j < nums2Size ){
        printf( "nums1[%d][%d]nums2[%d][%d]\n", i, nums1[i], j, nums2[j] );
        if( nums1[i] < nums2[j] ){
            i++;
        }else if( nums1[i] > nums2[j] ){
            j++;
        }else {
            nums1[k++] = nums1[i];
            i++;
            j++;
        }
    }
    *returnSize = k;
    return nums1;
}
