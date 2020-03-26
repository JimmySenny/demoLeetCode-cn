#include <stdio.h>

#include <stdio.h>
#include <stdlib.h>

int compi(const void *a, const void *b) {
	const int *p = a;
	const int *q = b;
    
	return *p - *q;
}

void mysort(int * A, int ASize){
    int i = 0;
    int j = 0;
    int tmp = 0;
    for( i; i<ASize; i++){
        j = i+1;
        for(j;j<ASize; j++){
            if(A[i] > A[j] ){
                tmp = A[i];
                A[i] = A[j];
                A[j] = tmp;
            }
        }
    }
    
}

void mysort2(int * A, int ASize, int start, int end){
    int i = start;
    int j = 0;
    int tmp = 0;
    if( end >= ASize){
        return ;
    }
    
    for( i; i<ASize; i++){
        j = i+1;
        for(j;j<ASize; j++){
            if(A[i] > A[j] ){
                tmp = A[i];
                A[i] = A[j];
                A[j] = tmp;
            }
        }
    }
}

int minIncrementForUnique(int* A, int ASize){
    int minMove = 0;
    
    if(ASize < 2){
        return minMove;
    }
    
    //mysort(A,ASize);
    qsort(A,ASize,sizeof(A[0]),compi);
    

    for (int i = 0; i < ASize - 2; i++ ){
        while (A[i] == A[i+1]) {
            A[i+1]++;
            minMove++;
            mysort2(A,ASize,i, i+2);
        }
    }
    
    if( A[ASize-2] == A[ASize-1]){
        minMove++;
    }

    return minMove;
}

int main( int argc, char[] argv ){
    int a[5] = {1,2,3,4,5};
    int b = minIncrementForUnique(a, 5);
    printf("[%d]", b);
}

