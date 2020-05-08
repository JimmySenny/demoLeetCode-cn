#include "../include/alg_comm.h"

void printNums( int * nums, int numsSize ){
    printf( "[" );
    for( int i = 0; i < numsSize; i++ ){
        printf( "%d ", nums[i] );
    }
    printf( "]\n" );
    return;
}

int compi( const void *a, const void *b ){
    const int* p = a;
    const int* q = b;

    return *p - *q;
}
