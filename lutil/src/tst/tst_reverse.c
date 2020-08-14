#include "lutil_tst.h"

void tst_reverseNums( void ){
    int nums1[] = {1};
    int nums2[] = {1, 2};
    int nums3[] = {1, 2, 3};
    int nums4[] = {1, 2, 3, 4};
    int nums5[] = {1, 2, 3, 4, 5};
    int nums6[] = {1, 2, 3, 4, 5, 6};
    int nums7[] = {1, 2, 3, 4, 5, 6, 7};

    reverseNums( nums1, 1 );
    printNums( nums1, 1 );

    reverseNums( nums2, 2 );
    printNums( nums2, 2 );

    reverseNums( nums3, 3 );
    printNums( nums3, 3 );

    reverseNums( nums4, 4 );
    printNums( nums4, 4 );


    reverseNums( nums5, 5 );
    printNums( nums5, 5 );

    reverseNums( nums6, 6 );
    printNums( nums6, 6 );

    reverseNums( nums7, 7 );
    printNums( nums7, 7 );

    return;
}
