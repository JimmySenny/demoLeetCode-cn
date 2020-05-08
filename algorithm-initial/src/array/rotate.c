#include "alg_array.h"


/*
 * 暴力解法
 */
void rotate( int* nums, int numsSize, int k ){
    int i,j, temp = 0;

    if( NULL == nums || 2 > numsSize ||  0 == k || k == numsSize ){
        return;
    }

    for( i = 0; i < k; i++ ){
        temp = nums[numsSize - 1];
        for( j = numsSize - 1; j > 0; j-- ){
            nums[j] = nums[j-1];
        }
        nums[0] = temp;
    }

    return;
}

/*
 * 逆序后再分段逆序
 */
void reverse( int* nums, int start, int end ){
    int i, j, temp = 0;

    for( i = start; i < (end - start)/2; i++ ){
        temp = nums[i];
        j = end - i - 1;
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
void rotate1( int* nums, int numsSize, int k ){

    if( NULL == nums || 2 > numsSize ||  0 == k || k == numsSize ){
        return;
    }

    reverse( nums, 0, numsSize );
    printNums( nums, numsSize );

    reverse( nums, 0, k );
    printNums( nums, numsSize );

    reverse( nums, k+1, numsSize );
    printNums( nums, numsSize );

    return;
}


extern int gcd(int a,int b);

void rotate2( int* nums, int numsSize, int k ){
    int i, j, size, temp1, temp2 = 0;

    if( NULL == nums || 2 > numsSize ||  0 == k || k == numsSize ){
        return;
    }

    size = gcd(k, numsSize);
    printf( "size[%d]\n", size );
    for( i = 0; i < size; i++ ){
        j = (i + k)%numsSize;
        temp1 = nums[i];
        while( j != i){
            temp2 = nums[j];
            nums[j] = temp1;
            j = (j + k)%numsSize; 
            temp1 = temp2;

        }
        nums[i] = temp1;

        printNums( nums, numsSize );
    }

    return;
}
