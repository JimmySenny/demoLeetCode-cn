#include "ds_dpointer.h"

void tst_arrayPairSum( void ){
    int numsSize = 1;
    int nums[] = { 1, 4, 3, 2 };

    numsSize = 4;

    arrayPairSum( nums, numsSize );

    return;
}

void tst_twoSum( void ){
    int nums[] = {2, 7, 11, 15};
    int numsSize = 4;
    int target = 9;
    int returnSize = 0;
    int * prt = NULL;

    printNums( nums, numsSize );
    printf( "target[%d]\n", target );
    prt = twoSum3( nums, numsSize, target, &returnSize );
    printNums( prt, returnSize );

    int nums1[] = {5, 25, 75};
    numsSize = 3;
    target = 100;

    printNums( nums1, numsSize );
    printf( "target[%d]\n", target );
    prt = twoSum3( nums1, numsSize, target, &returnSize );
    printNums( prt, returnSize );

    int nums2[] = {-1, 0, 1};
    target = 0;
    printNums( nums2, numsSize );
    printf( "target[%d]\n", target );
    prt = twoSum3( nums2, numsSize, target, &returnSize );
    printNums( prt, returnSize );

    int nums3[] = {3,24,50,79,88,150,345};
    numsSize = 7;
    target = 200;
    printNums( nums3, numsSize );
    printf( "target[%d]\n", target );
    prt = twoSum3( nums3, numsSize, target, &returnSize );
    printNums( prt, returnSize );

    return;
}

void tst_removeElement( void ){
    int nums[] = {3,2,2,3};
    int numsSize = 4;
    int val = 3;
    int retLen = 0;

    printNums( nums, numsSize );
    retLen = removeElement( nums, numsSize, val );
    printNums( nums, retLen );

    int nums1[] = {0,1,2,2,3,0,4,2};
    numsSize = 8;
    val = 2;
    printNums( nums1, numsSize );
    retLen = removeElement( nums1, numsSize, val );
    printNums( nums1, retLen );

    return;
}

void tst_findMaxConsecutiveOnes( void ){
    int nums[] = {1,1,0,1,1,1};
    int numsSize = 6;
    int iRet = 0;

    iRet = findMaxConsecutiveOnes( nums, numsSize );
    printf( "iRet[%d]\n", iRet );

    iRet = findMaxConsecutiveOnes1( nums, numsSize );
    printf( "iRet[%d]\n", iRet );
    
    return;
}
