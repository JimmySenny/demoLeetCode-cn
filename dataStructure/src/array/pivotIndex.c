#include "ds_array.h"


int pivotIndex(int* nums, int numsSize){
    int i = 0, j = numsSize-1;
    int sum, leftsum, rightsum = 0;
    
    if (nums == NULL){
        return -1;
    }
    
    // 至少3个
    if ( numsSize <= 2 ){
        return -1;
    }

    /* 
     * leftsum + nums[i] + rightsum = sum 
     * if leftsum == rightsum => 2*leftsum + nums[i] = sum
     * 特例：全0=> i:1 
     */
    sum = 0;
    for( i = 0; i < numsSize; i++ ){
	    printf( "sum[%d]\n", sum );
        sum += nums[i];
    }
	printf( "sum[%d]\n", sum );

    leftsum = 0;
    for( i=0; i < numsSize; i++ ){
        if( (2*leftsum + nums[i])== sum ){
            return i;
        }
        leftsum += nums[i];
		printf( "leftsum[%d]i[%d]\n", leftsum, i );
    }

    return -1;
}
