#include "alg_string.h"

/*
 * 暴力
 */
void reverseString(char* s, int sSize){
    int i, j, tmp;

    for( i = 0; i < sSize / 2; i++ ){
        j = sSize - i - 1;
        if( s[i] == s[j] ||
               i == j ){
            continue;
        }else{
            tmp = s[i];
            s[i] = s[j];
            s[j] = tmp;
        }
    }

    return;
}
