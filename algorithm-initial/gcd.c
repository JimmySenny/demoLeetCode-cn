#include <stdio.h>


//辗转相除法 
int gcd(int a,int b){ 
    if(a%b==0)
        return b;
    else
        return gcd(b,a%b);
}


#if 0

//穷举法
int divisor (int a, int b) //自定义函数求两数的最大公约数
{
    int  temp;//定义整型变量
    temp=(a>b)?b:a;//采种条件运算表达式求出两个数中的最小值
    while(temp>0)

    {
        if(a%temp==0&&b%temp==0)//只要找到一个数能同时被a,b所整除，则中止循环
            break;
        temp--;//如不满足if条件则变量自减，直到能被a,b所整除 
    } 
    return (temp);//返回满足条件的数到主调函数处 
} 

//更相减损法
int gcd2(int m,int n)
{
    int i=0,temp,x;
    while(m%2==0&&n%2==0)//判断m和n能被多少个2整除
    {
        m/=2;
        n/=2;
        i+=1;
    } 
    if(m<n)//m保存大的值
    {
        temp=m;
        m=n;
        n=temp;
    } 
    while(x)
    {
        x=m-n;
        m=(n>x)?n:x;
        n=(n<x)?n:x;
        if(n==(m-n))
            break;
    }
    if(i==0)
        return n;
    else
        return (int) pow(2,i)*n;
} 

//Stein算法
int Stein( unsigned int x, unsigned int y )
    /* return the greatest common divisor of x and y */
{
    int factor = 0;
    int temp;
    if ( x < y )
    {
        temp = x;
        x = y;
        y = temp;
    }
    if ( 0 == y )
    {
        return 0;
    }
    while ( x != y )
    {
        if ( x & 0x1 )
        {/* when x is odd */
            if ( y & 0x1 )
            {/* when x and y are both odd */
                y = ( x - y ) >> 1;
                x -= y;
            }
            else
            {/* when x is odd and y is even */
                y >>= 1;
            }
        }
        else
        {/* when x is even */
            if ( y & 0x1 )
            {/* when x is even and y is odd */
                x >>= 1;
                if ( x < y )
                {
                    temp = x;
                    x = y;
                    y = temp;
                }
            }
            else
            {/* when x and y are both even */
                x >>= 1;
                y >>= 1;
                ++factor;
            }
        }
    }
    return ( x << factor );
}


int main()
{
    int i;     
    int a[30];
    for(i=0;i<30;i++)
    {
        a[i]=rand()%100 + 1;
        printf("%d ",a[i]);
    }
    printf("\n");
    int b[30];
    for(i=0;i<30;i++)
    {
        b[i]=rand()%100 + 1;
        printf("%d ",b[i]);
    }
    printf("\n");
    clock_t start,finish;
    double dur;
    start= clock();
    for(i=0;i<30;i++)
    {
        //printf("辗转相除法所得最大公约数为：%d\n",gcd(a[i],b[i]));
        //printf("穷举法所得最大公约数为：%d\n",divisor(a[i],b[i]));
        printf("更相减损法所得最大公约数为：%d\n",gcd2(a[i],b[i]));
        //printf("Stein算法所得最大公约数为：%d\n",Stein(a[i],b[i]));
    }
    finish=clock();
    dur=(double)(finish-start)/CLOCKS_PER_SEC;
    printf("运行所用的时间为：%lf s\n",dur); 
    return 0;
}
#endif
