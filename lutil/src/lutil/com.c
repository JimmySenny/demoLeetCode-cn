#include "lutil.h"

int compi( const void *a, const void *b ){
    const int* p = a;
    const int* q = b;

    return *p - *q;
}

int compc( const void *a, const void *b ){
    const char * p = a;
    const char * q = b;

    return *p - *q;
}
