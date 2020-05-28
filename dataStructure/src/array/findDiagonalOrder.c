#include "ds_array.h"

/**
 ** Note: The returned array must be malloced, assume caller calls free().
 **/
int findDiagonalOrder(int** matrix, int matrixSize, int* matrixColSize, int* returnSize){
    // 对角线
    int i = 0, j = 0; // (i,j) 坐标
    int n1 = 0, n2 = 0; 
    int signFlag = 1; //正反序标识

    int* reArray = (int*)malloc( sizeof( int ) * matrixSize * matrixColSize[0] + 1 );

    for( n1 = 0; n1 < matrixSize + matrixColSize[0]; n1++ ) { //多少条对角线


    }

    

}
