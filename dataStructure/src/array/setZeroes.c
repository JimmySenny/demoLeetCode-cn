#include "ds_array.h"

/*
 * 暴力
 */
void setZeroes(int** matrix, int matrixSize, int* matrixColSize){
    int i = 0, j = 0;

    int * m = (int *)malloc( sizeof( int ) * matrixSize + 1 );
    int * n = (int *)malloc( sizeof( int ) * matrixColSize[0] + 1 );

    //memset( m, 0x00, sizeof( int ) * matrixSize + 1 );
    //memset( n, 0x00, sizeof( int ) * matrixColSize[0] + 1 );

    for( i = 0; i < matrixSize; i++ ){
        for( j = 0; j < matrixColSize[0]; j++ ){
            if( 0 == matrix[i][j] ){
                printf( "i,j(%d,%d)\n", i, j );
                m[i] = 1;
                n[j] = 1;
            }
        }
    }

//    printMatrix( matrix, matrixSize, matrixColSize[0] );
    printNums( m, matrixSize );
    printNums( n, matrixColSize[0] );

    for( i = 0; i < matrixSize; i++ ){
        for( j = 0; j < matrixColSize[0]; j++ ){
            if( 1 == m[i] ){
                matrix[i][j] = 0;
            }

            if( 1 == n[j] ){
                for( int k = 0; k < matrixSize; k++ ){
                    matrix[k][j] = 0;
                }
            }
        }
    }

//    printMatrix( matrix, matrixSize, matrixColSize[0] );

    return;
}
