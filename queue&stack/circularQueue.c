#include <stdio.h>
#include <stdlib.h>

#define true 0
#define false 1

typedef int bool;

typedef struct{
//int* head  = NULL;
//int* tail  = NULL;
//int* queue = NULL;
//int  size        = 0;
//int  currentSize = 0;
    int* head;
    int* tail;
    int* queue;
    int size;
    int currentSize;
}MyCircularQueue;

/** Initialize your data structure here. Set the size of the queue to be k. */
MyCircularQueue* myCircularQueueCreate(int k) {
	MyCircularQueue* mcq;
    
    mcq = (MyCircularQueue*)malloc( sizeof(MyCircularQueue) );

    printf("[%p]\n", mcq );
	
    mcq->queue = (int*)malloc( sizeof(int) * k + 1 );
    mcq->head = mcq->queue;
    mcq->tail = mcq->queue + k - 1;
    mcq->size = k;
    mcq->currentSize = 0;

    printf("[%p]\n", mcq );

    return mcq;
}

/** Insert an element into the circular queue. Return true if the operation is successful. */
bool myCircularQueueEnQueue(MyCircularQueue* obj, int value) {
    if( obj->currentSize >= obj->size ){
        return false;
    }

    obj->currentSize++;
    obj->tail++;

    if( obj->tail - obj->queue == obj->size ){
        obj->tail = obj->queue;
    }

    *(obj->tail) = value;

    return true;
}

/** Delete an element from the circular queue. Return true if the operation is successful. */
bool myCircularQueueDeQueue(MyCircularQueue* obj) {
    if( obj->currentSize <= 0 ){
        obj->head = obj->queue;
        obj->tail = obj->queue + obj->size - 1;
        return false;
    }

    obj->currentSize--;
    *(obj->head) = -1;

    obj->head++;
    if( obj->head - obj->queue == obj->size  ){
        obj->head = obj->queue;
    }

    return true;
}

/** Get the front item from the queue. */
int myCircularQueueFront(MyCircularQueue* obj) {
    if( obj->currentSize > 0 ){
        return *(obj->head);
    }

    return -1;
}

/** Get the last item from the queue. */
int myCircularQueueRear(MyCircularQueue* obj) {
    if( obj->currentSize > 0 ){
        return *(obj->tail);
    }
  
    return -1;
}

/** Checks whether the circular queue is empty or not. */
bool myCircularQueueIsEmpty(MyCircularQueue* obj) {
    if( obj->currentSize == 0 ){
        return true;
    }
  
    return false;
}

/** Checks whether the circular queue is full or not. */
bool myCircularQueueIsFull(MyCircularQueue* obj) {
    if( obj->currentSize == obj->size ){
        return true;
    }
  
    return false;
}

void myCircularQueueFree(MyCircularQueue* obj) {
    if( obj->queue != NULL ){
        free( obj->queue );
        obj->head = NULL;
        obj->tail = NULL;
        obj->queue= NULL;
    }

    if( obj != NULL ){
        free(obj);
        obj = NULL;
    }
}

void MyCircularQueueItera(MyCircularQueue* obj) {
    int* ptr = NULL;
    ptr = obj->queue;
    for(int i=0; i<obj->size; i++){
        printf( "[%d]\t", *ptr++);
    }
}

/**
 * Your MyCircularQueue struct will be instantiated and called as such:
 * MyCircularQueue* obj = myCircularQueueCreate(k);
 * bool param_1 = myCircularQueueEnQueue(obj, value);
 * bool param_2 = myCircularQueueDeQueue(obj);
 * int param_3 = myCircularQueueFront(obj);
 * int param_4 = myCircularQueueRear(obj);
 * bool param_5 = myCircularQueueIsEmpty(obj);
 * bool param_6 = myCircularQueueIsFull(obj);
 * myCircularQueueFree(obj);
**/


int main( int argc, char * argv[]){
    MyCircularQueue * mcq;

    mcq = myCircularQueueCreate( 3 );

    printf( "head[%p]\n", mcq->head );
    printf( "isempty[%d]\n", myCircularQueueIsEmpty (mcq) );

    printf( "insert[%d]\n", myCircularQueueEnQueue (mcq, 1) );
    printf( "insert[%d]\n", myCircularQueueEnQueue (mcq, 2) );
    printf( "insert[%d]\n", myCircularQueueEnQueue (mcq, 3) );
    printf( "insert[%d]\n", myCircularQueueEnQueue (mcq, 4) );

    MyCircularQueueItera (mcq);
    printf( "head[%p]\n", mcq->head );
    printf( "tail[%p]\n", mcq->tail);
    printf( "front[%d]\n", myCircularQueueFront (mcq) );
    printf( "tail[%d]\n", myCircularQueueRear (mcq) );

    printf( "isfull[%d]\n", myCircularQueueIsFull (mcq) );

    printf( "del[%d]\n", myCircularQueueDeQueue (mcq) );
    printf( "del[%d]\n", myCircularQueueDeQueue (mcq) );
    printf( "del[%d]\n", myCircularQueueDeQueue (mcq) );
    printf( "insert[%d]\n", myCircularQueueEnQueue (mcq, 5) );
    printf( "insert[%d]\n", myCircularQueueEnQueue (mcq, 6) );

    MyCircularQueueItera (mcq);

    printf( "head[%p]\n", mcq->head );
    printf( "tail[%p]\n", mcq->tail);

    printf( "currentSize[%d]\n", mcq->currentSize );
    printf( "front[%d]\n", myCircularQueueFront (mcq) );
    printf( "tail[%d]\n", myCircularQueueRear (mcq) );

    printf( "del[%d]\n", myCircularQueueDeQueue (mcq) );
    printf( "del[%d]\n", myCircularQueueDeQueue (mcq) );
    printf( "insert[%d]\n", myCircularQueueEnQueue (mcq, 7) );

    MyCircularQueueItera (mcq);

    printf( "head[%p]\n", mcq->head );
    printf( "tail[%p]\n", mcq->tail);
    printf( "currentSize[%d]\n", mcq->currentSize );
    printf( "currentSize[%d]\n", mcq->currentSize );

    printf( "front[%d]\n", myCircularQueueFront (mcq) );
    printf( "tail[%d]\n", myCircularQueueRear (mcq) );

    printf( "del[%d]\n", myCircularQueueDeQueue (mcq) );

    MyCircularQueueItera (mcq);

    myCircularQueueFree (mcq);

    return 0;
}
