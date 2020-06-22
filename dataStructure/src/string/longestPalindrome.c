#include "ds_string.h"

/*
 * 暴力
 */
bool isPalindrome( const char * s ){
    int len = strlen( s );

    for ( int i = 0; i < len / 2; i++ ){
        if( s[i] != s[len - i - 1]){
            return false;
        }
    }

    return true;
}
char * longestPalindrome(char * s){
    int i = 0, j = 0;
    int len = strlen( s );
    char buf[1000+1];
    int maxlen = 0;

    for(i = 0; i < len; i++ ){
        memset( buf, 0x00, sizeof( buf ) );
        for( j = i + 1; j <= len; j++ ){
            strncpy( buf, s + i, j - i );
            //printf( "buf[%s]\n", buf );

            if( isPalindrome( buf ) && ( j - i ) > maxlen ){
                maxlen = j - i;
                printf( "(i-j:%d-%d)[%s]\n", i, j, buf );
            }
        }
    }

    return buf;
}


