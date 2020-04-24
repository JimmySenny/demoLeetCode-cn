#include <stdio.h>
#include <stdbool.h>

extern int containsDuplicate(int* nums, int numsSize);

int main(int argc, char* argv[]){
//    int nums[] = {1,2,3,4,1};
    int nums[] = {1,2,3,4,5};

    printf( "containsDuplicate[%d]\n", containsDuplicate(nums, sizeof(nums)/sizeof(nums[0])));

    return 0;
}
