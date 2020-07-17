#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>

extern void printNums( int * nums, int numsSize );
extern void printChars( char * s, int sSize );
extern void printMatrix( int ** matrix, int row, int col );

extern int compi( const void *a, const void *b );
extern int compc( const void *a, const void *b );

extern void reverseNums( int * nums, int numSize );
extern void reverseChars( char * str );
extern void reverseCharsbyIdx( char * str, int start, int end );
