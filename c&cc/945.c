#include <stdio.h>

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

int minIncrementForUnique(int* A, int ASize){
    int minMove = 0;
    mysort(A,ASize);

    for (int i = 0; i < ASize - 1; i++ ){
        while (A[i] == A[i+1]) {
            A[i+1]++;
            minMove++;
            mysort(A,ASize);
        }
    }

    return minMove;

}

int main( int argc, char[] argv ){
    int a[5] = {1,2,3,4,5};
    int b = minIncrementForUnique(a, 5);
    printf("[%d]", b);
}
