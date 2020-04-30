#include <stdio.h>

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
    char grid[][3] = { {1,0,0}, {0,1,0}, {0,0,1} };
    char* p[3];
//    p[0] = &grid[0][0];
    p[0] = grid[0];
    p[1] = grid[1];
    p[2] = grid[2];

//    printf( "row[%d]\n", strlen(p) );
    printf( "col[%d]\n", *p[0] );

    int tmp = 3;
    printf( "[%d]\n", numIsland( p, 3, &tmp) );

    for( int i = 0; i < 3; i++ ){
        for( int j = 0; j < 3; j++ ){
            printf( "grid[%d]", grid[i][j]);
        }
        printf("\n");
    }
    printf("\n");

    return 0;
}
