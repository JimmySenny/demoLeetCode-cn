#include "ds_util.h"

void reverseNums( int * nums, int numsSize ){
    int i = 0, j = 0, tmp = 0;

    tmp = nums[0];
    for( i = 0, j = numsSize - 1; j > 0; i++, j-- ){
        nums[i] = nums[j];
    }
    nums[i] = tmp;

    return;
}

