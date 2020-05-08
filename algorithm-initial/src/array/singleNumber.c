#include "alg_array.h"

/*
 * 暴力
 */
int singleNumber( int * nums, int numsSize ){
    int singleFlag = true;
    int num = -1;
    

    for( int i = 0; i < numsSize; i++ ){
        singleFlag = true;
        for( int j = 0; j < numsSize; j++ ){
            if( i == j ){
                continue;
            }
            if( nums[i] == nums[j] ){
                singleFlag = false;
            }
        }
        if( true == singleFlag ){
            num = nums[i];
            break;
        }
    }

    return num;
}


/*
 * 排序后比较
 */
int compi( const void *a, const void *b ){
    const int* p = a;
    const int* q = b;

    return *p - *q;
}
int singleNumber1( int * nums, int numsSize ){

    if( numsSize < 2 ){
        return nums[0];
    }

    qsort( nums, numsSize, sizeof(nums[0]), compi );

    /* 首 尾 */
    if( nums[0] != nums[1] ){
        return nums[0];
    }

    if( nums[numsSize - 1] != nums[numsSize - 2] ){
        return nums[numsSize-1];
    }

    for( int i = 1; i < numsSize - 1; i++ ){
        if( nums[i-1] != nums[i] &&
            nums[i] != nums[i+1] ){
            return nums[i];
        }
    }

    return -1;
}

/*
 * 哈希
 */



/*
 * XOR 异或操作 满足交换律和结合率
 * a XOR 0 = a 
 * a XOR a = 0
 * a XOR b XOR a = (a XOR a ) XOR b = 0 XOR b = b
 */
int singleNumber3( int * nums, int numsSize ){
    int tmp = 0;


    for( int i = 0; i < numsSize; i++ ){
        tmp ^= nums[i];
    }

    return tmp;
}
