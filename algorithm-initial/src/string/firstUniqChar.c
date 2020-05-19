#include "alg_string.h"

/*
 * 暴力
 */
int firstUniqChar(char * s){
    int i, j, k, idx = -1;
    int len = strlen( s );
    int uniqFlag = true;

    if( len < 1 ){
        return -1;
    }

    if( 1 == len ){
        return 0;
    }

    for( i = 0; i < len; i++ ){
        uniqFlag = true;
        for( j = i+1; j < len; j++ ){
            if( s[i] == s[j] ){
                uniqFlag = false;
                break;
            }
        }
        
        if( uniqFlag ){
            for( k = 0; k < i; k++ ){
                if( s[k] == s[i] ){
                    uniqFlag = false;
                    break;
                }
            }
            if( uniqFlag ){
                idx = i;
                break;
            }
        }
    }

    return idx;
}
