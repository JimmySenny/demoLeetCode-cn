#include "alg_string.h"


void tst_reverseString( void ){
    char s[10]={"hello"};

    int len = strlen( s );

    printf( "len[%d]\n", len );
    reverseString( s, len );
    printChars( s, len );

    return;
}

/*
 * 暴力
 */
void tst_reverse( void ){
//    int x = 123;
//    int x = -123;
//    int x = -2147483648;
//    int x = 2147483647;
    int x = 1534236469;

    printf( "y[%d]\n", reverse( x ) );

    return;
}

void tst_firstUniqChar( void ){
//    char s[] = "leetcode";
//    char s[] = "loveleetcode";
//    char s[] = "llllll";
    char s[] = "abcdabcdabcd";

    printf( "return[%d]\n", firstUniqChar( s ) );
    return;
}

void tst_isAnagram( void ){

    return;
}
