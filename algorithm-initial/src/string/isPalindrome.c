#include "alg_string.h"


/*
 * 暴力
 */
bool isPalindrome(char * s){
    int slen = strlen( s );
    int i = 0, j = slen - 1;
    bool iRet = true;

    while( i <= slen -1 && j >= 0 ){
        printf( "sij[%c][%c]\n", s[i], s[j] );
        if( ( 'A' <= s[i] && s[i] <= 'Z' ) ||
            ( 'a' <= s[i] && s[i] <= 'z' ) ||
            ( '0' <= s[i] && s[i] <= '9' ) ){
            ;
        }else {
            i++;
            continue;
        }

        if( ( 'A' <= s[j] && s[j] <= 'Z' ) ||
            ( 'a' <= s[j] && s[j] <= 'z' ) ||
            ( '0' <= s[j] && s[j] <= '9' ) ){
            ;
        }else {
            j--;
            continue;
        }


        if( tolower(s[i]) == tolower(s[j]) ){
            i++;
            j--;
        }else {
            iRet = false;
            break;
        }
    }

    return iRet;
}
