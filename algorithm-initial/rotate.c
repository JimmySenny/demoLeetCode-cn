#include <stdio.h>

void printNums( int * nums, int numsSize ){
    printf( "[" );
    for( int i = 0; i < numsSize; i++ ){
	printf( "%d ", nums[i] );
    }
    printf( "]\n" );
    return;
}

/*
 * 无算法实现
 */
void rotate( int* nums, int numsSize, int k ){
    int i,j, temp = 0;

    if( NULL == nums || 2 > numsSize ||  0 == k ){
	return;
    }

    for( i = 0; i < k; i++ ){
	temp = nums[numsSize - 1];
	for( j = numsSize - 1; j > 0; j-- ){
            nums[j] = nums[j-1];
	}
	nums[0] = temp;
    }

    return;
}

/*
 * 逆序后再分段逆序
 */
void reverse( int* nums, int start, int end ){
    int i, j, temp = 0;

    for( i = start; i < (end - start)/2; i++ ){
        temp = nums[i];
	j = end - i - 1;
	nums[i] = nums[j];
	nums[j] = temp;
    }
}
void rotate1( int* nums, int numsSize, int k ){

    if( NULL == nums || 2 > numsSize ||  0 == k ){
	return;
    }

    reverse( nums, 0, numsSize );
    printNums( nums, numsSize );

    reverse( nums, 0, k );
    printNums( nums, numsSize );

    reverse( nums, k+1, numsSize );
    printNums( nums, numsSize );

    return;
}

void rotate2( int* nums, int numsSize, int k ){
    int i, j, m, temp1, temp2 = 0;

    for( i = 0,j = 0; i < gcd(k, numsSize); i++ ){
	m = (j + k)%numsSize;
	temp1 = nums[i];
	while( m != i){
            temp2 = nums[m];
	    nums[m] = temp1;
	    m = (m + k)%numsSize; 
	    temp1 = temp2;
	}

        printNums( nums, numsSize );
    }

    return;
}

int main( int argc, char * argv[]){
    int nums[] = {1, 2, 3, 4, 5, 6, 7};
//    int nums[] = {-1,-100,3,99};

    if( argc != 2 ){
        printf( "USAGE arg k" );
	exit(-1);
    }
    int k = atoi(argv[1]);
    printf( "k[%d]\n", k );

    printNums( nums, sizeof(nums)/sizeof(nums[0]) );

    rotate2( nums, sizeof(nums)/sizeof(nums[0]), k );

//    printNums( nums, sizeof(nums)/sizeof(nums[0]) );

    return 0;
}
