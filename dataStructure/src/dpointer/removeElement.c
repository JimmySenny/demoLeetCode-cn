#include "ds_dpointer.h"

int removeElement( int * nums, int numsSize, int val ){
    int retLen= 0;
    int fast = 0, slow = 0;

    for( fast = 0, slow = 0; fast < numsSize; fast++ ){
        if( val != nums[fast] ){
            nums[slow++] = nums[fast];
            retLen = slow;
        }
    }

    return retLen;
}
