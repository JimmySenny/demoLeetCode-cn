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
    char grid[3][3] = { {'1','0','0'},{'0','1','0'},{'0','0','1'}};

    printf( "[%d]\n", numIsland( grid, 3, grid[1] ) );

    return 0;
}
