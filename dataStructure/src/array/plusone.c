#include <stdio.h>

/**
 ** Note: The returned array must be malloced, assume caller calls free().
 **/
int* plusOne(int* digits, int digitsSize, int* returnSize){
    int i = 0;

    if( digits == NULL ){
        *returnSize = 0;
        return NULL;
    }

    for(i = digitsSize - 1; i >= 0; i-- ){
        if( digits[i] == 9 ){
            digits[i] = 0 ;
        }else {
            digits[i] += 1;
            *returnSize = digitsSize;
            return digits; //no malloc in func main free coredump
        }
    }
    int * redigits = (int*)malloc( sizeof(int) * ( digitsSize + 1) + 1);
    memset( redigits, 0x00, sizeof(int)*(digitsSize + 1) + 1);
    redigits[0] = 1;
    *returnSize = digitsSize + 1;
    for( i = 1; i < *returnSize; i++ ){
        redigits[i] = digits[i - 1];
    }
    return redigits;
}

int* plusOne1(int* digits, int digitsSize, int* returnSize){
    if( digits == NULL ){
        *returnSize = 0;
        return NULL;
    }

    int i = digitsSize - 1;
    int carryFlag = 0;
    int * redigits = (int*) malloc(sizeof(int) * digitsSize + 1);
    memset( redigits, 0x00, sizeof(int)*digitsSize + 1);

    for(i = digitsSize - 1; i >= 0; i-- ){

        if( i == digitsSize -1 ||
            carryFlag == 1 ){
            if( digits[i] + 1 > 9){
                carryFlag = 1;
                redigits[i] = 0 ;
            }else {
                carryFlag = 0;
                redigits[i] = digits[i] + 1;
            }
        }else {
            redigits[i] = digits[i];
        }
    }
    if( carryFlag == 1 ){
        int * redigits1 = (int*)malloc( sizeof(int) * ( digitsSize + 1) + 1);
        memset( redigits1, 0x00, sizeof(int)*(digitsSize + 1) + 1);
        redigits1[0] = 1;
        memcpy( redigits1 + 1, redigits, sizeof(int) * digitsSize + 1);
        free(redigits);
        *returnSize = digitsSize + 1;
        return redigits1;
    }else{
        *returnSize = digitsSize;
        return redigits;
    }
    return NULL;
}
