#include "ds_string.h"

/*
 * 暴力
 * 1 拆分每个word
 * 2 翻转每个单词 并连接
 * 3 翻转整个字符串
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

    return result;
}

/*
 * 暴力 空间占用O(1)
 * 1 翻转每个word 并且去除首尾空格，单词间距处理为1个空格 
 * 2 整体翻转
 */
char * reverseWords2(char * s){
    int len = strlen( s );
    int start = -1, end = -1;
    int idx= 0;

    printf( "input[%s]\n", s );

    printf( "s[%s]\n", s );

    for( start = 0; start < len; start++ ){
        if( s[start] != ' ' ){ // 每个单词的开始
            if( idx != 0 ){ // 除首个单词外 其他均前补空格 确保每个单词中间一个g空格
                s[idx++] = ' ';
            }

            end = start;
            while( end < len && s[end] != ' ' ){ // 遍历每个单词至末尾
                s[idx++] = s[end++];
            }

            printf( "s[%d,%d,%d,%s]\n", start, end, idx, s );
            int j = idx - ( end - start + 1);
            reverseCharsbyIdx( s, idx - ( end - start ), idx - 1 );
            start = end;
        }
    }
    s[idx] = '\0'; // 多余的 截断处理 !!!
    printf( "s[%s]\n", s );

    reverseChars( s );

    printf( "returns[%s]\n", s );

    return s;
}
