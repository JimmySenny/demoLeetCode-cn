#include "ds_array.h"
void tst_pivotIndex( void ){
    return;
}

void tst_dominantIndex( void ){
    return;
}

void tst_plusOne( void ){
    int digits[4] = { 1, 9, 9, 9 };
//    int digits[3] = { 9, 9, 9 };
    int* redigits = NULL;
    int returnSize = 0;

    redigits = plusOne( digits, sizeof(digits)/sizeof(int), &returnSize );

    for( int i = 0; i < returnSize; i++ ){
        printf( " [%d] ", redigits[i] );
    }
    printf( "\n" );
//    free(redigits);

    return;
}

void tst_searchInsert( void ){
    int nums[] = { 1, 3, 5, 6 };
    int target = 7;

    printf( "indx[%d]\n", searchInsert( nums, 4, target ) );

    printf( "indx[%d]\n", searchInsert1( nums, 4, target ) );

    return;
}

void tst_merge( void ){
    int matrix[][2] = { {  1,  3 },\
                        {  2,  6 },\
                        {  8, 10 },\
                        { 15, 18 } };
    int *pmatrix[3];
    int matrixSize = 4, matrixColSize = 2;

    pmatrix[0] = matrix[0];
    pmatrix[1] = matrix[1];
    pmatrix[2] = matrix[2];
    pmatrix[3] = matrix[3];

    printMatrix( pmatrix, 4, 2 );

    return;
}

void tst_setZeroes( void ){
    /*
    int matrix[][3] = { { 1, 1, 1 }, \
                        { 1, 0, 1 }, \
                        { 1, 1, 1 } };
    int *pmatrix[3];
    int matrixSize = 3, matrixColSize = 3;
    pmatrix[0] = matrix[0];
    pmatrix[1] = matrix[1];
    pmatrix[2] = matrix[2];
    */
    int matrix[][4] = { { 0, 1, 2, 0 }, \
                        { 3, 4, 5, 2 }, \
                        { 1, 3, 1, 5 } };
    int *pmatrix[3];
    int matrixSize = 3, matrixColSize = 4;
    pmatrix[0] = matrix[0];
    pmatrix[1] = matrix[1];
    pmatrix[2] = matrix[2];


    setZeroes( pmatrix, matrixSize, &matrixColSize );
    printMatrix( pmatrix, matrixSize, matrixColSize );

    return;
}

void tst_findDiagonalOrder( void ){
    int returnSize = -1;
    int matrix[][3] = { { 1, 2, 3 }, \
                        { 4, 5, 6 }, \
                        { 7, 8, 9 } };
    int *pmatrix[3];
    int matrixSize = 3, matrixColSize = 3;
    pmatrix[0] = matrix[0];
    pmatrix[1] = matrix[1];
    pmatrix[2] = matrix[2];

    findDiagonalOrder( pmatrix, matrixSize, &matrixColSize, returnSize );

    return;
}
