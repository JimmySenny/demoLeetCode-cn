#include "ds_array.h"

/**
 ** Note: The returned array must be malloced, assume caller calls free().
 **/
int findDiagonalOrder(int** matrix, int matrixSize, int* matrixColSize, int* returnSize){
    // 对角线
    int i = 0, j = 0; // (i,j) 坐标
    int signFlag = 1; //正反序标识
    int k = 1, l = 0, m = 0, n = 0; //计数器

    int* reArray = (int*)malloc( sizeof( int ) * matrixSize * matrixColSize[0] + 1 );
    int* tmpArray = (int*)malloc( sizeof( int ) * ( matrixSize + matrixColSize[0] ) + 1 );

    memset( reArray, 0x00, sizeof( reArray ) );
    m = 0;
    for( k = 0; k < matrixSize + matrixColSize[0] - 1; k++ ) { //多少条对角线
        signFlag = k % 2;
        l = 0;
        memset( tmpArray, 0x00, sizeof( tmpArray ) );
        if( k < matrixColSize[0] ){
            printf( " order1: " );
            i = 0;
            j = k;
            /*
               for( i = 0, j = k; 
               i < matrixSize && j >= 0 && j < matrixColSize[0]; 
               i++, j-- ){
               printf( " [%d,%d][%d] ", i, j, matrix[i][j] );
               tmpArray[l++] = matrix[i][j];

               }
               */
        }else {
            printf( " order2: " );
            i = k - matrixColSize[0] + 1;
            j = matrixColSize[0] - 1;
            /*
               for( i = k - matrixColSize[0] + 1, j = matrixColSize[0] - 1; 
               i < matrixSize && j >= 0 && j < matrixColSize[0];
               i++, j-- ){
               printf( " [%d,%d][%d] ", i, j, matrix[i][j] );
               tmpArray[l++] = matrix[i][j];
               }
               */
        }
        while( i < matrixSize && j >= 0 && j < matrixColSize[0] ){
            printf( " (%d,%d)[%d] ", i, j, matrix[i][j] );
            tmpArray[l++] = matrix[i][j];
            i++;
            j--;
        }
        printf( "\n" );
        printf( "l[%d]signFlag[%d]i[%d]\n", l, signFlag, i );
        printNums( tmpArray, l );
        if( 0 == signFlag ){ //偶数对角线逆序
            reverseNums( tmpArray, l );
        }
        printNums( tmpArray, l );

        for( n = 0; n < l; m++, n++ ){
            reArray[m] = tmpArray[n];
        }
    }
    printNums( reArray, matrixSize * matrixColSize[0] );

    return 0;
}
