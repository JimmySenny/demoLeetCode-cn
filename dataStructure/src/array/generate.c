#include "ds_array.h"

/*
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced,
 * assume caller calls free().
 */
int** generate( int numRows, int * returnSize, int ** returnColumSizes ){
    //returnSize表示返回杨辉三角的行数 = 输入numRows
    *returnSize = numRows;
    //returnColumnSizes是指向一个数组的指针，数组元素为对应行的元素个数
    *returnColumSizes = (int*)malloc( sizeof( int ) * numRows );
    //n行则有n*n二维数组
    //returnMatrix指向的是由指针构成的数组，每个指针都指向对应的三角的一行数；也是二维数组
    int ** returnMatrix = (int**)malloc( sizeof(int*) * numRows );
    int i = 0;

    /*
    for( 0; i < *returnSize; i++ ){
        (*returnColumSizes)[i] = i + 1;
        returnMatrix[i] = (int*)malloc( sizeof( int ) * (*returnSize)[i] );
        returnMatrix[i][0] = 1;
        returnMatrix[i][i] = 1;
    }

    for( i = 2; i < numRows - 1; i++ ){
        for( int j = 1; j < i; j++ ){
            returnMatrix[i][j] = returnMatrix[i-1][j-1] + returnMatrix[i-1][j];
        }
    }
    */

    return returnMatrix;
}
