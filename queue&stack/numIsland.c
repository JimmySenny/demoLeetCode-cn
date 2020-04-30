#include <stdio.h>

int direction[4][2] = { {-1, 0 },    /* 上 */
                        { 1, 0 },    /* 下 */
                        { 0,-1 },    /* 左 */
                        { 0, 1 } };  /* 右 */

void dfs( char** grid, int row, int col, int gridSize, int* gridColSize ){

    printf ( "dfs_grid[%d]\n", grid[row][col] );
    if( 1 != grid[row][col] ){
        return;
    }

    grid[row][col] = 2;

    /* 上方 */
    if( 0 < row && 1 == grid[row - 1][col] ){
        dfs(grid, row-1, col, gridSize, gridColSize);
    }
    /* 下方 */
    if( gridSize < row + 1 && 1 == grid[row + 1][col] ){
        dfs(grid, row+1, col, gridSize, gridColSize);
    }
    /* 左方 */
    if( 0 < col && 1 == grid[row][col-1] ){
        dfs(grid, row, col-1, gridSize, gridColSize);
    }
    /* 右方 */
    if( gridColSize[0] > col+ 1 && 1 == grid[row][col+1] ){
        dfs(grid, row, col+1, gridSize, gridColSize);
    }

    return;
}
int numIsland( char **grid, int gridSize, int* gridColSize ){
    int num = 0;

    printf ( "grid_i_j[%d]\n", grid[0][0] );
    for( int i = 0; i < gridSize; i++ ){
        for( int j = 0; j < gridColSize[0]; j++ ){
            printf ( "j[%d]\n", j );
            if( 1 == grid[i][j] ){
                num++;
                dfs(grid, i, j, gridSize, gridColSize);
            }
        }
    }

    printf ( "num[%d]\n", num );
    return num;
}
