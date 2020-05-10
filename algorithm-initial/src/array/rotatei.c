#include "alg_array.h"

/*
 * 暴力
 */
void rotatei(int** matrix, int matrixSize, int* matrixColSize){
    int i = 0, j = 0, k = 0;
    int len = 0, length = 0, tmp = 0;
    // n*n matrix 需要旋转的圈数为 matrixSize / 2
    // 第 i 圈 i行，matrixSize -1 -i 行, i 列  matrixSize - 1 -i 列
    // 第 i 圈 每边的节点数 len =  (matrixSize - i * 2 )
    // 共( matrixSize - i * 2 ) * 4 - 4 个节点需要顺时针旋转
    for( i = 0; i < matrixSize / 2; i++ ){
        len = matrixSize - 2*i;
        length = matrixSize - 1 - i;
        printf( "i[%d]len[%d]length[%d]\n", i,len,length );
        for( j = i, k = 0; k < len - 1; j++, k++ ){
            //(i,j) -> (j,matrixSize-1-i) -> 
            //( matrixSize-1-i-j,i) -> (matixSize-1-j,matrixSize-1-i-j) ->
            // 每次旋转4个点
            printf( " %d ", matrix[i][j] );
            printf( " %d ", matrix[j][length] );
            printf( " %d ", matrix[length][length-k] );
            printf( " %d \n", matrix[length-k][i] );

            tmp                      = matrix[i][j];
            matrix[i][j]             = matrix[length-k][i];
            matrix[length-k][i]      = matrix[length][length-k];
            matrix[length][length-k] = matrix[j][length];
            matrix[j][length]        = tmp;

            printf( " %d ", matrix[i][j] );
            printf( " %d ", matrix[j][length] );
            printf( " %d ", matrix[length][length-k] );
            printf( " %d \n", matrix[length-k][i] );
            //matrix[i][j] = tmp;
        }
    }


    return;
}
