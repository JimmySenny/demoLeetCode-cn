
/* hashEntry 定义 */
typedef struct hashEntry{
    int    key;
    char * value;
    struct hashEntry* next;
}struHashEntry;

/* hashTable 定义 */
typedef struct hashTable{
    struct hashEntry ** head;
    int hash_width;
}struHashTable;

extern int initHashTable( struct hashTable* table, int width );
extern int freeHashTable( struHashTable table );
extern int addHash( struHashTable table, int key );
extern struHashEntry* findHash( struHashTable table, int key );
