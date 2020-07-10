#include "ds_string.h"

void tst_longestPalindrome( void ){
    char a[] = "abcde";
    char b[] = "xxabay";
    char c[] = "xxabbay";
    char d[] = "aaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaa";

    longestPalindrome( a );
    longestPalindrome( b );
    longestPalindrome( c );

    printf( "\n" );

    printf( "%s:\n", a );
    longestPalindrome2( a );
    printf( "%s:\n", b );
    longestPalindrome2( b );
    printf( "%s:\n", c );
    longestPalindrome2( c );

    longestPalindrome2( d );

    return;
}

void tst_reverseWords( void ){
    char a[] = "the sky is blue";
    char b[] = "  hello world!  ";
    char c[] = "a good   example";


    /*
    reverseWords( a );
    reverseWords( b );
    reverseWords( c );
    */

    reverseWords2( a );
    reverseWords2( b );
    reverseWords2( c );

    return;
}

void tst_arrayPairSum( void ){
    int numsSize = 1;
    char nums[] = "abc";

    arrayPairSum( nums, numsSize );

    return;
}
