#include "ds_queue.h"

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
void tst_circularQueueEnQueue( void ){
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

    return;
}

void tst_numIslands( void ){
    /*
    char grid[][] ={ { '1','1','1','1','0'}, \
                     { '1','1','0','1','0'}, \
                     { '1','1','0','0','0'}, \
                     { '0','0','0','0','0'} };
                    */
//    char grid[3][3] = { {'1','0','0'},{'0','1','0'},{'0','0','1'} };
//    char grid[3][3] = { '1','0','0','0','1','0','0','0','1' };
//    char grid[3][3] = { {"100"},{"010"},{"001"} };
//    char grid[][3] = { "100","010","001" };
    char grid[][3] = { {'1','0','0'}, \
                       {'0','1','0'}, \
                       {'0','0','1'}, \
                       {'0','0','0'} };
    char* p[3];
//    p[0] = &grid[0][0];
    p[0] = grid[0];
    p[1] = grid[1];
    p[2] = grid[2];
    p[3] = grid[3];

    char grid2[][5] = { {'1','1','1','1','0'}, \
                        {'1','1','0','1','0'}, \
                        {'1','1','0','0','0'}, \
                        {'0','0','0','0','0'} };
    char* p2[4];
    // 指针必须赋值完全
    p2[0] = grid2[0];
    p2[1] = grid2[1];
    p2[2] = grid2[2];
    p2[3] = grid2[3];

    printf( "[%d-%d]\n", strlen(p),strlen(p[0]) ); //6, 4  6 TODO???
    printf( "[%d-%d]\n", strlen(p2),strlen(p2[0]) ); //6, 4  6 TODO???

    int tmp = 5;
    printf( "[%d]\n", numIsland( p2, 4, &tmp) );

    printMatrix( p2, 4, 5 );

    return;
}
