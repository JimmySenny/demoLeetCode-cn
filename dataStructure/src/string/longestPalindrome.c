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


/*
 * 中心扩散发 滑动窗口
 */
char * longestPalindrome2( char * s ){
    int length = strlen( s );
    int left = 0, right = 0, len = 0; //滑动窗口左、右、长度
    int maxStart = 0;
    int maxLen = 0;

    char buf[1000+1];
    char * p = NULL;

    for( int i = 0; i < length; i++ ){ // 顺次测试每个中心 找出最长的滑动窗口
        len = 1;
        left = i - 1;
        right = i + 1;

        // 需考虑 奇回文和偶回文
        while( left >= 0 && s[left] == s[i] ){
            len++;
            left--;
        }

        while( right < length && s[right] == s[i] ){
            len++;
            right++;
        }

        // 以中心(奇或偶)向两边扩散
        while( left >= 0 && right < length  && s[left] == s[right] ){
            len += 2;
            left--;
            right++;
        }

        if( len > maxLen ){
            memset( buf, 0x00, sizeof( buf ) );
            maxLen = len;
            maxStart = left + 1;
            strncpy( buf, s + maxStart, maxLen );

            printf( "len[%d]buf[%s]\n", len, buf );
        }
    }

    p = buf;

    return p;
}

