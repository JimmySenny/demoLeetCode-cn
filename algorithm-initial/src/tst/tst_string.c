#include "alg_string.h"


void tst_reverseString( void ){
    char s[10]={"hello"};

    int len = strlen( s );

    printf( "len[%d]\n", len );
    reverseString( s, len );
    printChars( s, len );

    return;
}

void tst_reverse( void ){
//    int x = 123;
//    int x = -123;
//    int x = -2147483648;
//    int x = 2147483647;
    int x = 1534236469;

    printf( "y[%d]\n", reverse( x ) );

    return;
}

void tst_firstUniqChar( void ){
//    char s[] = "leetcode";
//    char s[] = "loveleetcode";
//    char s[] = "llllll";
    char s[] = "abcdabcdabcd";

    printf( "return[%d]\n", firstUniqChar( s ) );
    return;
}

void tst_isAnagram( void ){
    char s[] = "anagram";
    char t[] = "nagaram";

//    printf( "isAnagram[%d]\n", isAnagram( s, t ) );
    printf( "isAnagram1[%d]\n", isAnagram1( s, t ) );

    return;
}

void tst_isPalindrome( void ){
//    char s[] = "A man, a plan, a canal: Panama";
//    char s[] = "race a car";
//    char s[] = ".,";
    char s[] = "0P";

    printf( "isPalindrome[%d]\n", isPalindrome( s ) );

    return;
}

void tst_myAtoi( void ){
//    char s[] = "   -42";
//    char s[] = "www.   -42";
//    char s[] = "-43.21";
//    char s[] = "2147483649";
//    char s[] = "-2147483649";
//    char s[] = "  0000000000012345678"; //12345678
//    char s[] = "   +0 123"; //0
    char s[] = "-000000000000001"; //-1

    printf( "myAtoi[%d]\n", myAtoi( s ) );

    return;
}

void tst_strStr( void ){
    char haystack[] = "hello";
    char needle[] = "ll";

    printf( "strStr[%d]\n", strStr( haystack, needle ) );

    return;
}
