
#include "ds.h"

/* Stack */
//最小栈
/**
 * Your MinStack struct will be instantiated and called as such:
 * MinStack* obj = minStackCreate();
 * minStackPush(obj, x);
 
 * minStackPop(obj);
 
 * int param_3 = minStackTop(obj);
 
 * int param_4 = minStackGetMin(obj);
 
 * minStackFree(obj);
*/
typedef struct {
    int maxStackLen = 5;
    int currStackLen = 0;
    int Min = 0;
    int* arrMinStack = NULL;
} MinStack;

MinStack * minStackCreate(); 

bool isMinStackFull( MinStack * obj );
int callocMinStack( MinStack * obj );

void minStackPush( MinStack * obj, int x );

void minStackPop( MinStack * obj );

int minStackTop( MinStack * obj );

int minStackGetMin( MinStack* obj );

extern bool isValid(char * s);
