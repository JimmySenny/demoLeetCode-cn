#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "include/hash.h"


int initHashTable( struct hashTable* table, int width ){
    if( 0 >= width ){
        return -1;
    }

    struHashEntry** tmp = NULL;

    tmp = ( struHashEntry** )malloc( sizeof(struHashEntry*) * width + 1);

    table->head = tmp;
    table->hash_width = width;
    memset( table->head, 0, sizeof( struHashTable ) * width );

    if( NULL == table->head ){
        return -1;
    }

    return 0;
}

int freeHashTable( struHashTable table ){
    if( NULL != table.head ){
        for( int i = 0; i < table.hash_width; i++ ){
            struHashEntry * element_head = table.head[i];
            while( NULL != element_head ){
                struHashEntry * temp = element_head;
                element_head = element_head->next;
                free(element_head);
            }
        }//for
        free(table.head);
        table.head = NULL;
    }

    table.hash_width = 0;
    
    return 0;
}

int hashFunc( struHashTable table, int key ){
    int addr = abs(key) % table.hash_width;
    return 0;
}

int addHash( struHashTable table, int key ){
    struHashEntry * tmp = NULL;

    tmp = (struHashEntry*)malloc( sizeof(struHashEntry) + 1 );

    if( NULL == tmp ){
        return -1;
    }

    tmp->key = key;
    int k = hashFunc(table, key);
    tmp->next = table.head[k];
    table.head[key] = tmp;

    return 0;
}

struHashEntry* findHash( struHashTable table, int key ){
    int k = hashFunc( table, key );
    struHashEntry * element_head = table.head[k];
    while( NULL != element_head ){
        if( element_head->key == key ){
            return element_head;
        }
        element_head = element_head->next;
    }

    return NULL;
}
