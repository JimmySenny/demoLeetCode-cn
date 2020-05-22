#include "alg_string.h"

/*
 * 暴力 
 */
bool isAnagram(char * s, char * t){

    printf( "s[%s]\n", s );
    printf( "t[%s]\n", t );

    qsort( s, strlen( s ), sizeof( char ), compc );
    qsort( t, strlen( t ), sizeof( char ), compc );

    printf( "s[%s]\n", s );
    printf( "t[%s]\n", t );

    if( !strcmp( s, t ) ){
        return true;
    }

    return false;
}

/*
 * 
 */
bool isAnagram1(char * s, char * t){
    int i = 0, idx = 0;
    int num[26+1] = { 0 };

    if( NULL == s && NULL == t )
        return true;
    if( NULL == s || NULL == t )
        return false;

    int slen = strlen( s );
    int tlen = strlen( t );

    if( slen != tlen )
        return false;

    for( i = 0; i < slen ; i++ ) {
        idx = s[i] - 'a';
        printf( "si[%c] idx[%d]\n", s[i], idx );
        num[idx]++;
    }

    for( i = 0; i < tlen; i++ ){
        idx = t[i] - 'a';
        printf( "ti[%c] idx[%d]\n", t[i], idx );
        num[idx]--;
    }

    printNums( num, 26 );

    for( i = 0; i < 26; i++ ){
        if( 0 != num[i] ){
            return false;
        }
    }

    return true;
}
