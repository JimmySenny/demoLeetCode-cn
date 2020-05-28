#include "alg_string.h"

/*
 * 暴力
 */
int strStr(char * haystack, char * needle){
    int idx = -1;
    int i = 0, j = 0, k = 0;

    if( NULL == haystack || NULL == needle ){
        return 0;
    }

    if( 0 == strlen( needle ) ){
        return 0;
    }

    for( i = 0; i < strlen( haystack ); i++ ){
        k = i;
        for( j = 0, k = i; j < strlen( needle ); j++, k++ ){
            if( haystack[k] != needle[j] ){
                idx = -1;
                break;
            }
            idx = i;
        }
        if( idx == i )
            break;
    }

    return  idx;
}

/*
 * 滑动窗口
 */
int strStr1( char * haystack, char * needle ){
    int idx = -1;
    int len = strlen( haystack );
    int sublen = strlen( needle );
    int i = 0;

    if( 0 == sublen ){
        return 0;
    }

    for( i = 0; i <= len - sublen; i++ ){
        if( haystack[i] == needle[0] ) { // 首位相等才比较串
            if( 0 == strncmp( haystack + i, needle, sublen ) ){
                idx = i;
                break;
            }
        }
    }

    return idx;
}
