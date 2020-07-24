#include "lutil_tst.h"

void tst_binarySearch( void ){

    int nums[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
    int l = 0;
    int r = sizeof( nums ) / sizeof( int );

    printf( "r[%d]\n", r);

    binarySearch( nums, l, r, 7 );

    return;
}
