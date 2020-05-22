#include "alg_string.h"

int myAtoi( char * str ){
    int num = 0, i = 0, k = 0;
    int signFlag = 0;
    for( i = 0; i < strlen( str ); i++ ){
        if( ' ' == str[i] && 0 == signFlag ){
            continue;
        }

        if( '-' == str[i] && 0 == signFlag ){
            signFlag = -1;
            continue;
        }
        if( '+' == str[i] && 0 == signFlag ){
            signFlag = 1;
            continue;
        }

        //第一个非空字符 不是数字或正、负号  0
        if( ( str[i] < '0' || str[i] > '9' ) && 0 == signFlag ){
            break;
        }

        if( str[i] < '0' || str[i] > '9' ){
            break;
        }

        if( 0 == signFlag ){
            signFlag = 1;
        }

        k = str[i] - '0';

        if( 1 == signFlag ){
            if( num > 214748364 ){
                num = 2147483647;
                break;
            }else if( 214748364 == num ){
                if( k >= 7 ){
                    num = 2147483647;
                    break;
                }
            }
        } else {
            if( num > 214748364 ){
                //num = 2147483648;
                //break;
                return -2147483648;
            }else if( 214748364 == num ){
                if( k >= 8 ){
                    //num = 2147483648;
                    //break;
                    return -2147483648;
                }
            }
        }

        num = num * 10 + k;
    }

    num *= signFlag;

    return num;
}

