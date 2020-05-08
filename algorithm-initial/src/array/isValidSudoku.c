#include "alg_array.h"

/*
 * 数字 1-9 在每一行只能出现一次。
 * 数字 1-9 在每一列只能出现一次。
 * 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次
 */

/*
 * 暴力
 */

bool isValidSudokuRow( char ** board, int size, char * row, int i, int j ){
    int n = 0;
    printf( "row[%c]\n", board[i][j] );
    if( '.' == board[i][j] ){
        return true;
    }

//    n = atoi( board[i][j] );
    n = board[i][j] - '1';

    printf( "row[%d]\n", n );

    if( '0' == row[n] ){
        return false;
    }else{
        row[n] = '0';
    }

    return true;
}

bool isValidSudokuCol( char ** board, int size, char * col, int i, int j ){
    int n = 0;
    printf( "col[%c]\n", board[i][j] );
    if( '.' == board[i][j] ){
        return true;
    }
    n = board[i][j] - '1';

    printf( "col[%d]\n", n );

    if( '0' == col[n] ){
        return false;
    }else{
        col[n] = '0';
    }

    return true;
}

/*
 * 0-0 0-1 0-2 0-3 0-4 0-5 0-6 0-7 0-8
 * 1-0 1-1 1-2 1-3 1-4 1-5 1-6 1-7 1-8
 * 2-0 2-1 2-2 2-3 2-4 2-5 2-6 2-7 2-8
 * 3-0 3-1 3-2 3-3 3-4 3-5 3-6 3-7 3-8
 * 4-0 4-1 4-2 4-3 4-4 4-5 4-6 4-7 4-8
 * 5-0 5-1 5-2 5-3 5-4 5-5 5-6 5-7 5-8
 * 6-0 6-1 6-2 6-3 6-4 6-5 6-6 6-7 6-8
 * 7-0 7-1 7-2 7-3 7-4 7-5 7-6 7-7 7-8
 * 8-0 8-1 8-2 8-3 8-4 8-5 8-6 8-7 8-8
 */
bool isValidSudokuSmall( char ** board, int size, char small[][9+1], int i, int j ){
    /* 
     * m 第m个小九宫格 为 i/3 * 3 + j/3
     * n 数字
     */
    int m = 0, n = 0;
    printf( "col[%c]\n", board[i][j] );
    if( '.' == board[i][j] ){
        return true;
    }
    n = board[i][j] - '1';

    m = i/3 * 3 + j/3;
    printf( "i,j,m,n[%d,%d,%d,%d]\n", i,j,m,n );

    if( '0' == small[m][n] ){
        return false;
    }else{
        small[m][n] = '0';
    }

    return true;
}

bool isValidSudoku( char** board, int boardSize, int* boardColSize ){
    int i = 0, j = 0;
    char row[9+1];
    char col[9+1];

    char small[9][9+1] = {  {'1','2','3','4','5','6','7','8','9'}, \
                            {'1','2','3','4','5','6','7','8','9'}, \
                            {'1','2','3','4','5','6','7','8','9'}, \
                            {'1','2','3','4','5','6','7','8','9'}, \
                            {'1','2','3','4','5','6','7','8','9'}, \
                            {'1','2','3','4','5','6','7','8','9'}, \
                            {'1','2','3','4','5','6','7','8','9'}, \
                            {'1','2','3','4','5','6','7','8','9'}, \
                            {'1','2','3','4','5','6','7','8','9'} };


    /* 
     * 必须为方阵
     */
    for( i = 0 ; i < boardSize; i++ ){ 
//        printf( "[%d%d]\n", i, j );
        strcpy( row, "123456789" );
        strcpy( col, "123456789" );
        for( j = 0 ; j < boardColSize[0]; j ++ ){
            if( false == isValidSudokuRow( board, *boardColSize, row, i, j ) ){
                return false;
            }

            if( false == isValidSudokuCol( board, boardSize, col, j, i ) ){
                return false;
            }

            if( false == isValidSudokuSmall( board, boardSize, small, i, j ) ){
                return false;
            }
        }
    }

    return true;
}
