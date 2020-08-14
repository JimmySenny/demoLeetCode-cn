#include "lutil.h"

void reverseNums( int * nums, int numsSize ){
    int i = 0, j = 0, tmp = 0;

    for( i = 0; i < numsSize/2; i++ ){
        tmp = nums[i];
        nums[i] = nums[numsSize - i - 1];
        nums[numsSize - i - 1] = tmp;
//        printf( "i[%d]j[%d]\n", i, j );
    }

    return;
}

void reverseChars( char * str ){
    char tmp;
    int len = strlen( str );
    for( int i = 0; i < len / 2; i++ ){
        tmp = str[i];
        str[i] = str[len - i - 1];
        str[len-i-1] = tmp;
    }
    
    return;
}

void reverseCharsbyIdx( char * str, int start, int end ){
    char tmp;
    int len = end - start + 1;
    int idx = start;

    for( int i = 0; i < len / 2; i++ ){
        tmp = str[idx];
        str[idx] = str[start + len - 1 - i];
        str[start + len - 1 - i] = tmp;
        idx++;
    }

    return;
}
