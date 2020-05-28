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
