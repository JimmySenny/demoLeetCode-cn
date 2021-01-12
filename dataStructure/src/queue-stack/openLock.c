#include "ds_queue.h"

/*
 * 标准的BFS模板题目
 * 每个节点有四位数，每个数有两种转换方式，即每个节点子节点有8个。\
 * 从根节点("0000")出发遍历子节点，如果节点值和目标值相等，返回当前深度即可。\
 * 不等的话，检查是否访问过该节点或者该节点存在于死节点数组中，因为已经访问的节点或者死节点是不用再访问它的子节点的。\
 * 如果没有访问过，需要添加到队列中，以待访其子节点。\
 * 同时，将其添加到死节点数组中，防止后续重复访问。\
 * 因为队列元素动态变化，所以每层遍历需要先获取当层需要遍历的节点数。\
 * 此外，使用c语言，需要手动实现队列的入队、出队等操作。此外，再和死节点数组比较时，采用hash，这样在于死节点数组比较时速度会更快。\
 */

#define LOCK_SIZE 4
#define LOCK_MAXNUM 10000

typedef struct Node{
    char node[LOCK_SIZE+1];
}NODE;

typedef struct LockQueue{
    int front;
    int rear;
    int size;
    NODE elem[LOCK_MAXNUM];
}LOCK_QUEUE;

LOCK_QUEUE* lockQueueCreate(){
    LOCK_QUEUE * q = ( LOCK_QUEUE * )malloc( sizeof(LOCK_QUEUE));
    q->front = 0;
    q->rear = 0;
    q->size = 0;

    return q;
}

void lockQueueFree( LOCK_QUEUE * q ){
    if( NULL != q ){
        free(q);
        q = NULL;
    }

    return;
}

bool isLockQueueEmpty( LOCK_QUEUE * q){
    if( q->rear == q->front ){
        return true;
    }

    return false;
}

bool isLockQueueFull( LOCK_QUEUE * q){
    if( ( q->rear + 1 )%LOCK_MAXNUM == q->front ){
        return true;
    }

    return false;
}

int sizeofLockQueue( LOCK_QUEUE * q){
    return q->size;
}

bool enLockQueue(LOCK_QUEUE * q, NODE * n){
    if( isLockQueueFull(q) ){
        return false;
    }

    q->elem[q->rear] = *n;
    q->rear = (q->rear + 1)%LOCK_MAXNUM;
    q->size++;

    return true;
}

bool deLockQueue(LOCK_QUEUE * q, NODE * n){
    if( isLockQueueEmpty(q)){
        return false;
    }

    *n = q->elem[q->front];
    q->front = (q->front + 1)%LOCK_MAXNUM;
    q->size--;

    return true;
}

NODE * frontLockQueue( LOCK_QUEUE * q ){
    return &(q->elem[q->front]);
}

NODE * rearLockQueue( LOCK_QUEUE * q ){
    return &(q->elem[q->rear]);
}

bool isTarget( const char * this,const char * target ){
    return !strcmp( this, target );
}

int isDeadrears( int * dead, char * t){
    int i, v;

    for( i = 0, v = 0; i < 4; i++ ){
        v = v * 10 + ( t[i] - '0' );
    }

    if( 1 == dead[v] ){
        return true;
    }

    return false;
}

void reareadrears( int * dead, char * t){
    int i, v;
    for( i = 0, v = 0; i < 4; i++ ){
        v = v * 10 + ( t[i] - '0' );
    }

    dead[v] = 1;

    return;
}


int openLock(char ** deadrears, int deadrearsSize, char * target){
    int steps = -1;
    char start[] = "0000";
    char n[] = "00000";
    char c[] = "00000";
    LOCK_QUEUE * q;

    q = (LOCK_QUEUE *)malloc( sizeof( LOCK_QUEUE ) );
    if( NULL == q ){
        return steps;
    }
//    q->length = 0;
    q->front = 0;
    q->rear = 0;


    return steps;
}
