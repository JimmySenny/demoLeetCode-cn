#include <stdio.h>

void bfs( char** grid, int row, int col, int gridSize, int* gridColSize ){
    grid[row][col] = '0';

    /* 上方 */
    if( 0 < row && '1' == grid[row - 1][col] ){
        bfs(grid, row-1, col, gridSize, gridColSize);
    }
    /* 下方 */
    if( gridSize < row + 1 && '1' == grid[row + 1][col] ){
        bfs(grid, row+1, col, gridSize, gridColSize);
    }
    /* 左方 */
    if( 0 < col && '1' == grid[row][col-1] ){
        bfs(grid, row, col-1, gridSize, gridColSize);
    }
    /* 右方 */
    if( gridColSize[row] > col+ 1 && '1' == grid[row][col+1] ){
        bfs(grid, row, col+1, gridSize, gridColSize);
    }


}
int numIsland( char** grid, int gridSize, int* gridColSize ){
    int num = 0;

    for( int i = 0; i < gridSize; i++ ){
        for( int j = 0; j < gridColSize[i]; j++ ){
            printf('[%s]\n', grid[i][j] );
            if( '1' == grid[i][j] ){
                num++;
                bfs(grid, i, j, gridSize, gridColSize);
            }
        }
    }

    return num;
}
