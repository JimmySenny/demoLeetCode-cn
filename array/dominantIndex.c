#include <stdio.h>


int dominantIndex( int * nums, int numsSize ){
    int i, j, flag = 0;

    for( i=0; i < numsSize; i++ ){
        flag = 1;
        for( j=0; j < numsSize; j++ ){
            if( i == j ){
                continue;
            }
            if( nums[i] < 2*nums[j] ){
                flag = 0;
                break;
            }
        }
        if( flag == 1 ){
            return i;
        }
    }
    return -1;
}

int main( int argc, char * argv[] ){
    return 0;
}
