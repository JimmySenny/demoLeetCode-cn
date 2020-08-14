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

    printMatrix( pmatrix, matrixSize, matrixColSize );

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
    int matrixSize = 3, matrixColSize = 3;
    int * p = NULL;
    /*
    int matrix[][3] = { { 1, 2, 3 }, \
                        { 4, 5, 6 }, \
                        { 7, 8, 9 } };
    int *pmatrix[3];
    pmatrix[0] = matrix[0];
    pmatrix[1] = matrix[1];
    pmatrix[2] = matrix[2];

    printMatrix( pmatrix, matrixSize, matrixColSize );

    findDiagonalOrder( pmatrix, matrixSize, &matrixColSize, &returnSize );

    int matrix1[][1] = { { 1 } };
    int *pmatrix1[1];

    pmatrix1[0] = matrix1[0];

    matrixSize = 1;
    matrixColSize = 1;

    printMatrix( pmatrix1, matrixSize, matrixColSize );
    p = findDiagonalOrder( pmatrix1, matrixSize, &matrixColSize, &returnSize );
    printf( "re[%d]returnSize[%d]\n", p[0], returnSize );
    printNums( p, returnSize );
    */
    
    int matrix2[][5] = { { 1, 2, 3, 4, 5 }, \
                         { 6, 7, 8, 9, 10 }, \
                         { 11, 12, 13, 14, 15 }, \
                         { 16, 17, 18, 19, 20 }, \
                         { 21, 22, 23, 24, 25 } };
    int *pmatrix2[5];
    matrixSize = 5;
    matrixColSize = 5;
    pmatrix2[0] = matrix2[0];
    pmatrix2[1] = matrix2[1];
    pmatrix2[2] = matrix2[2];
    pmatrix2[3] = matrix2[3];
    pmatrix2[4] = matrix2[4];

    printMatrix( pmatrix2, matrixSize, matrixColSize );
    p = findDiagonalOrder( pmatrix2, matrixSize, &matrixColSize, &returnSize );
    printNums( p, returnSize );

    int matrix3[][2] = { { 1, 2 }, \
                         { 8, 4 }, \
                         {0, -1}
                       };
    int *pmatrix3[3];
    pmatrix3[0] = matrix3[0];
    pmatrix3[1] = matrix3[1];
    pmatrix3[2] = matrix3[2];

    matrixSize = 3;
    matrixColSize = 2;

    printMatrix( pmatrix3, matrixSize, matrixColSize );
    p = findDiagonalOrder( pmatrix3, matrixSize, &matrixColSize, &returnSize );
    printNums( p, returnSize );


    return;
}


void tst_generate( void ){
    int numRows = 5;
    int returnSize = 0;
    int returnColumSizes = 0;
    int ** ppMatrix = NULL;

    /*
    ppMatrix = generate( numRows, &returnSize, &&returnColumSizes );
    printMatrix( ppMatrix, returnSize, returnColumSizes );
    */

    return;
}

void tst_getRow( void ){

    return;
}

void tst_reverseWords( void ){

    return;
}

void tst_findMin( void ){

    return;
}
