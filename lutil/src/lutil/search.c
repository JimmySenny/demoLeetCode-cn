#include "lutil.h"

/*
 * example
 */
int _binarySearch( int * nums, int left, int right, int target ){
    int result = -1;

    int mid;
    while( left < right ){
        mid = left + ( right - left ) >> 2;

        if( nums[mid] < target ){
            left = mid + 1;
        }else \
        if( nums[mid] > target ){
            right = mid - 1;
        }else{
            result = mid;
            break;
        }
    }
    return result;
}

int binarySearch( int * nums, int left, int right, int target ){
    int mid = 0;

    printNums( nums, right );

    while( left < right ){
        mid = ( left + right ) >> 1; // left + rigth / 2

        printf( "l,r,m[%d,%d,%d,%d]\n", left, right, mid, nums[mid] );

        if( nums[mid] < target ){
            left = mid + 1;
        }else{
            right = mid;
        }
    }

    return ( nums[left] == target )?left:-1;

}
