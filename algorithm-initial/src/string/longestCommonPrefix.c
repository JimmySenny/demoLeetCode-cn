#include "alg_string.h"


/*
 * 暴力
 */
char * longestCommonPrefix(char ** strs, int strsSize){
    int i = 0, j = 0, tmp = 0, sFlag = 0;
    int colsize = 0;

    printf( "tot[%ld]\n", sizeof( strs )/sizeof( char ) );
    printf( "row[%ld]\n", sizeof( strs[0] )/sizeof( char ) );
    printf( "col[%ld]\n", ( sizeof( strs )/sizeof( char ) ) / ( sizeof( strs[0] )/sizeof( char ) ) );

    if( 0 == strsSize ){
        return strs[0];
    }

    if( 1 == strsSize ){
        return strs[0];
    }

    colsize = strs[1] - strs[0];
    printf( "colsize[%d]\n", colsize );

    if( colsize < 1 ){
        return "";
    }

    printf( "sl[%ld]\n", strlen( strs[0]) );

    for( i = 0; i < strlen( strs[0] ); i++ ){
        printf( "i[%d]\n", i );
        tmp = strs[0][i];
        for( j = 1; j < strsSize; j++ ){
            if( tmp != strs[j][i] ){
                sFlag = true;
                break;
            }
        }
        if( sFlag ){
            break;
        }
    }

    //修改原二维数据的0行返回
    strs[0][i] = '\0';

    return strs[0];
}
