#include "ds_string.h"

/*
 * 暴力
 */
char * reverseWords(char * s){
    int len = strlen( s );
    int start = -1, end = -1;
    int k = 0;
    int width = 0;
    char * word = NULL;
    char * result = NULL;
    char * p = NULL;

    result = ( char * )malloc( len + 1);
    memset( result, 0x00, len + 1 );

    for( int i = 0; i < len; i++ ){

        if( 0 == i && s[i] != ' ' ){  // 首为开始
            start = i;
        }else
        if( 0 == i && s[i] == ' ' ){  // 首不为开始
            continue;
        }else
        if( s[i-1] == ' ' && s[i] != ' ' ){ // 中间开始
            start = i;
        }

        if( len - 1 == i && s[i] != ' '  ){ //尾为结束
            end = i;
        }else
        if( len - 1 == i && s[i] == ' '  ){ //尾不为结束
            break;
        }else
        if( s[i] != ' ' && s[i+1] == ' ' ){ // 中间结束
            end = i;
        }

        if( start <= end && end == i ){
            width = end - start + 1;
            word = (char *)malloc( width + 1 );
            memset( word, 0x00, width + 1 );
            strncpy( word, s + start, width );

            printf( "s[%d,%d][%s]\n", start, end, word );
            reverseChars( word );
            printf( "rs[%s]\n", word );

            if( k ){
                strcat( result, " " );
            }
            strcat( result, word );
            k++;
        }
    }

    printf( "result[%s]\n", result );
    reverseChars( result );
    printf( "reresult[%s]\n", result );

    return p;
}
