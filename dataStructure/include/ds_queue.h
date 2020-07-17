#include "ds.h"

// 循环队列实现
typedef struct MyCircularQueue{
//int* head  = NULL;
//int* tail  = NULL;
//int* queue = NULL;
//int  size        = 0;
//int  currentSize = 0;
    int* queue;
    int* head;
    int* tail;
    int front;
    int last;
    int size;
    int currentSize;
}MyCircularQueue;

/** Initialize your data structure here. Set the size of the queue to be k. */
extern MyCircularQueue* myCircularQueueCreate(int k);
/** Insert an element into the circular queue. Return true if the operation is successful. */
extern bool myCircularQueueEnQueue(MyCircularQueue* obj, int value) ;
/** Delete an element from the circular queue. Return true if the operation is successful. */
extern bool myCircularQueueDeQueue(MyCircularQueue* obj);
/** Get the front item from the queue. */
extern int myCircularQueueFront(MyCircularQueue* obj);
/** Get the last item from the queue. */
extern int myCircularQueueRear(MyCircularQueue* obj);
/** Checks whether the circular queue is empty or not. */
extern bool myCircularQueueIsEmpty(MyCircularQueue* obj);
/** Checks whether the circular queue is full or not. */
extern bool myCircularQueueIsFull(MyCircularQueue* obj);
extern void myCircularQueueFree(MyCircularQueue* obj);
extern void MyCircularQueueItera(MyCircularQueue* obj);

extern void dfs( char** grid, int row, int col, int gridSize, int* gridColSize );

extern int numIslands(char** grid, int gridSize, int* gridColSize);
//extern int openLock(char ** deadends, int deadendsSize, char * target);
