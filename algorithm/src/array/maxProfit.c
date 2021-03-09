#include "alg_array.h"

int maxProfit( int* prices, int pricesSize ){
    int i, j, profit = 0;
    printf( "pricesSize[%d]\n", pricesSize );
    if( prices == NULL || pricesSize < 2 ){
        return 0;
    }
    profit = 0;
    for( i = 0, j = 1; j < pricesSize; j++ ){
        if( prices[j] <= prices[i] ){
            i = j;
        }else{ /* prices[j] > prices[i] */
            if( pricesSize - 1 ==  j || prices[j] > prices[j + 1] ){
                profit += prices[j] - prices[i];
                i = j;
            }
        }
    }

    return profit;
}

/*
 * 贪心
 */
int maxProfit1( int* prices, int pricesSize ){
    int i, profit = 0;

    if( prices == NULL || pricesSize < 2 ){
        return profit;
    }

    for( i = 1; i < pricesSize; i++ ){
        if( prices[i] > prices[i-1] ){
            profit += prices[i] - prices[i-1];
        }
    }

    return profit;
}
