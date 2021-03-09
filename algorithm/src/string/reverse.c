#include "alg_string.h"

int reverse( int x ){
    int  n = 0;
    long y = 0;


    printf( "x[%d]\n", x );
    do{
        n = x % 10;
        if( ( y >  214748364 || (  214748364 == y && n >  7 ) ) ||
            ( y < -214748364 || ( -214748364 == y && n < -8) ) ){
            y = 0;
            break;
        }
        y = y * 10 + n;
        printf( "n[%d]y[%ld]\n", n, y );
        x /= 10;
        printf( "while[%d]\n", x );
    }while( x );

    /*
    if( -2147483648 > y || 2147483647 < y ){
        y = 0;
    }
    */

    return y;
}
