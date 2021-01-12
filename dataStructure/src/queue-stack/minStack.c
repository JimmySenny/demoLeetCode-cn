#include "ds_stack.h"

/**
 * Your MinStack struct will be instantiated and called as such:
 * MinStack* obj = minStackCreate();
 * minStackPush(obj, x);
 
 * minStackPop(obj);
 
 * int param_3 = minStackTop(obj);
 
 * int param_4 = minStackGetMin(obj);
 
 * minStackFree(obj);
*/

/*
MinStack* minStackCreate() {
    MinStack  minstack;
    
    minstack.maxStackLen = 5;
    minstack.currStackLen = 0;
    minstack.Min = 0; 
    
    minstack.arrMinStack = (int*)malloc( sizeof(int) * minstack.maxStackLen );

    return &minstack;
}

bool isMinStackFull( MinStack * obj ){
    if( obj->currStackLen == obj->maxStackLen ){
        return true;
    }

    return false;
}

int callocMinStack( MinStack * obj ){

}

void minStackPush(MinStack* obj, int x) {
    if( isMinStackFull( obj ) ){
        callocMinStack( obj );
    }
    if( obj->Min > x ){
        obj->Min = x;
    }

    obj->arrMinStack[obj->currStackLen++] = x;
}

void minStackPop(MinStack* obj) {
    obj->currStackLen--;
    if( obj->Min == obj->arrMinStack[obj->currStackLen]) {
        
    }
}

int minStackTop(MinStack* obj) {
    return obj->arrMinStack[obj->currStackLen];
}

int minStackGetMin(MinStack* obj) {
    return obj->Min;
}

void minStackFree(MinStack* obj) {
    if( obj->arrMinStack != NULL ){
    }
}

*/
