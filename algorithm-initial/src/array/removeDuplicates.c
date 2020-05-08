#include "alg_array.h"

int removeDuplicates( int* nums, int numsSize ){
    /*
     * i 遍历数组下标
     * j 删除重复后的数组下标
     */
    int i, j;

    /* IN 0 OUT 0
     * IN 1 OUT 1
     */
    if( nums == NULL || 2 > numsSize ){
        return numsSize;
    }

    for( i = 1,j = 0; i < numsSize; i++ ){
       if( nums[i] == nums[j] ){
           continue; 
       }
       j++;
       if( j != i ){ //优化条件 避免原地复制
           nums[j]=nums[i];
       }
    }
    return j+1;
}
