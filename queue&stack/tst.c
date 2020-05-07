#include <stdio.h>
#include <string.h>

extern int numIsland( char** grid, int gridSize, int* gridColSize );

int main( int argc, char* argv[] ){
    /*
    char grid[][] ={ \
                     { '1','1','1','1','0'}, \
                     { '1','1','0','1','0'}, \
                     { '1','1','0','0','0'}, \
                     { '0','0','0','0','0'}  \
                    };
                    */
//    char grid[3][3] = { {'1','0','0'},{'0','1','0'},{'0','0','1'} };
//    char grid[3][3] = { '1','0','0','0','1','0','0','0','1' };
//    char grid[3][3] = { {"100"},{"010"},{"001"} };
//    char grid[][3] = { "100","010","001" };
    char grid[][3] = { {'1','0','0'}, {'0','1','0'}, {'0','0','1'},{'0','0','0'} };
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

    for( int i = 0; i < 4; i++ ){
        for( int j = 0; j < 5; j++ ){
            printf( "[%d]", grid2[i][j]);
        }
        printf("\n");
    }
    printf("\n");

    return 0;
}
