#include "ds_comm.h"

void printNums( int * nums, int numsSize ){
    printf( "[" );
    for( int i = 0; i < numsSize; i++ ){
        printf( "%d ", nums[i] );
    }
    printf( "]\n" );
    return;
}

void printChars( char * s, int sSize ){
    printf( "[" );
    for( int i = 0; i < sSize; i++ ){
        printf( "%d ", s[i] );
    }
    printf( "]\n" );
    return;
}
void printMatrix( int ** matrix, int row, int col ){
    int i = 0, j = 0;

    for( i = 0; i < row; i++ ){
        printf( "[" );
        for( j = 0; j < col; j++ ){
            printf( " %d ", matrix[i][j] );
        }
        printf( "]\n" );
    }

    return;
}

int compi( const void *a, const void *b ){
    const int* p = a;
    const int* q = b;

    return *p - *q;
}
