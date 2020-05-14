#include "alg_string.h"


void tst_reverseString( void ){
    char s[10]={"hello"};

    int len = strlen( s );

    printf( "len[%d]\n", len );
    reverseString( s, len );
    printChars( s, len );

    return;
}
