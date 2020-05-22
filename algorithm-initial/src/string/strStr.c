#include "alg_string.h"

/*
 * 暴力
 */
int strStr(char * haystack, char * needle){
    int idx = -1;
    int i = 0, j = 0, k = 0;

    if( 0 == strlen( haystack ) ||  0 == strlen( needle ) ){
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
