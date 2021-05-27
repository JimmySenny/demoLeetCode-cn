#include "alg_array.h"

extern void quickSort(int* nums, int numsSize, int l, int r );

// removeDuplicates
void tst_removeDuplicates( void ){
    //int nums[]={1, 1, 2};
    int nums[10]={0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
    int len = sizeof(nums)/sizeof(nums[0]);

    len = removeDuplicates( nums, len );
    printNums( nums, len );

    return;
}

// maxProfit
void tst_maxProfit( void ){
    int prices[] = {7, 1, 5, 3, 6, 4};
    //int prices[] = {1, 2, 3, 4, 5};
    //int prices[] = {7, 6, 4, 3, 1};
    
    printf( "maxProfit[%d]\n", maxProfit( prices, sizeof(prices)/sizeof(prices[0]) ) );
    printf( "maxProfit1[%d]\n", maxProfit1( prices, sizeof(prices)/sizeof(prices[0]) ) );

    return;
}

// rotate
void tst_rotate( int argc, char * argv[] ){
    int nums[] = {1, 2, 3, 4, 5, 6};
    //int nums[] = {-1,-100,3,99};
    if( argc != 2 ){
        printf( "USAGE arg k" );
        return;
    }
    int k = atoi(argv[1]);
    int size = sizeof(nums)/sizeof(nums[0]);

    //rotate( nums, size, k );
    rotate2( nums, size, k );
    printNums( nums, size );

    return;
}


// containsDuplicate
void tst_containsDuplicate( void ){
//    int nums[] = {1,2,3,1};
    int nums[] = {1,2,3,4,5};

    int length = sizeof(nums)/sizeof(nums[0]);

    printNums( nums, length );

    printf( "containsDuplicate[%d]\n", containsDuplicate(nums, length));
    printf( "containsDuplicate[%d]\n", containsDuplicate1(nums, length));

    return;
}

// singleNumber
void tst_singleNumber( void ){
//    int nums[] = {2,2,1};
    int nums[] = {4,1,2,1,2};
    int length = sizeof(nums)/sizeof(nums[0]);

    printf( "singleNumber[%d]\n", singleNumber3(nums, length));

    printNums( nums, length );

    return;
}

// intersect1
void tst_intersect( void ){
//    int nums1[] = {1,2,2,1};
//    int nums2[] = {2,2};
//    int nums1[] = {4,9,5};
//    int nums2[] = {9,4,9,8,4};
    int nums1[] = {-2147483648,1,2,3};
    int nums2[] = {1,-2147483648,-2147483648};

    int length1 = sizeof(nums1)/sizeof(nums1[0]);
    int length2 = sizeof(nums2)/sizeof(nums2[0]);

    int len = 0;
    int * nums = NULL;

    nums = intersect1(nums1, length1, nums2, length2, &len );

    printNums( nums, len );

    return;
}

// moveZeroes
void tst_moveZeroes( void ){
    int nums[] = {0, 1, 0, 3, 12 };
//    int nums[] = {1, 0, 1};
    int length = sizeof(nums)/sizeof(nums[0]);

    moveZeroes1(nums, length);

    printNums( nums, length );

    return;
}

// twoSum
void tst_twoSum( void ){
    int nums[] = {2, 7, 11, 15};
    int length = sizeof(nums)/sizeof(nums[0]);

    int len = 0;

    printf("tst_twoSum()");
    twoSum( nums, length, 9, &len ); 

    printNums( nums, len );

    return;
}

// isValidSudoku
void tst_isValidSudoku( void ){
    char board[][9] = { { '5','3','.','.','7','.','.','.','.' }, \
                        { '6','.','.','1','9','5','.','.','.' }, \
                        { '.','9','8','.','.','.','.','6','.' }, \
                        { '8','.','.','.','6','.','.','.','3' }, \
                        { '4','7','.','8','.','3','.','.','1' }, \
                        { '7','.','.','.','2','.','.','.','6' }, \
                        { '.','6','.','.','.','.','2','8','.' }, \
                        { '.','.','.','4','1','9','.','.','5' }, \
                        { '.','.','.','.','8','.','.','7','9' } };

    char * pboard[9];
    pboard[0] = board[0];
    pboard[1] = board[1];
    pboard[2] = board[2];
    pboard[3] = board[3];
    pboard[4] = board[4];
    pboard[5] = board[5];
    pboard[6] = board[6];
    pboard[7] = board[7];
    pboard[8] = board[8];

    int size = 9;

    printf( "[%d]\n", isValidSudoku(pboard, size, &size ) );

    return;
}

void tst_rotatei( void ){
    /*
    int matrix[][3] = { { 1, 2, 3 }, \
                        { 4, 5, 6 }, \
                        { 7, 8, 9 } };

    int *pmatrix[3];
    pmatrix[0] = matrix[0];
    pmatrix[1] = matrix[1];
    pmatrix[2] = matrix[2];
    int matrixSize = 3, matrixColSize = 3;
    
    int matrix[][5] = { { 1, 2, 3, 4, 5 }, \
                        { 6, 1, 2, 3, 6 }, \
                        { 5, 8, 9, 4, 7 }, \
                        { 4, 7, 6, 5, 8 }, \
                        { 3, 2, 1, 0, 9 } };

    int *pmatrix[5];
    pmatrix[0] = matrix[0];
    pmatrix[1] = matrix[1];
    pmatrix[2] = matrix[2];
    pmatrix[3] = matrix[3];
    pmatrix[4] = matrix[4];
    int matrixSize = 5, matrixColSize = 5;
    */
    int matrix[][6] = { { 1, 2, 3, 4, 5, 6 }, \
                        { 0, 1, 2, 3, 4, 7 }, \
                        { 9, 2, 1, 2, 5, 8 }, \
                        { 8, 1, 4, 3, 6, 9 }, \
                        { 7, 0, 9, 8, 7, 0 }, \
                        { 6, 5, 4, 3, 2, 1 } };

    int *pmatrix[6];
    pmatrix[0] = matrix[0];
    pmatrix[1] = matrix[1];
    pmatrix[2] = matrix[2];
    pmatrix[3] = matrix[3];
    pmatrix[4] = matrix[4];
    pmatrix[5] = matrix[5];
    int matrixSize = 6, matrixColSize = 6;

    printf( "[%d-%d]\n", sizeof(pmatrix[0]), sizeof( *pmatrix[0] ) );


    printMatrix( pmatrix, matrixSize, matrixColSize );

    rotatei( pmatrix, matrixSize, &matrixColSize );
    
    printMatrix( pmatrix, matrixSize, matrixColSize );

    return;
}

