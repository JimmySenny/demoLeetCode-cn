#include <stdio.h>
#include <stdbool.h>

/*
 * 冒泡排序(BubbleSort)
 */
int bubbleSort(int* nums, int numsSize){
    int flag = false;
    int temp;

    for( int i = 0; i < numsSize - 1; i++ ){
        flag = false;

        for( int j = 0; j < numsSize - 1 - i; j++ ){
            if( nums[j+1] > nums[j] ){
                temp = nums[j+1];
                nums[j+1] = nums[j];
                nums[j] = temp;
                flag = true;
            }
        }

        if( false == flag ){
            break;
        }
    }
    
    return 0;
}
