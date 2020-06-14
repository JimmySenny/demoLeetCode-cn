#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int tst( char ** pm, int size ){
    return strlen( pm[0] );
}

int main( void ){
    char m[][1] = { "", "" };
    char *pm[2];
    pm[0] = m[0];
    pm[1] = m[1];

    printf( "[%d]\n", strlen( "" ) );

    printf( "tst[%s]\n", tst( pm, 2 ) );

    return 0;
}
