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
