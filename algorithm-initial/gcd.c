//շת����� 

 int gcd(int a,int b)

 { 
     if(a%b==0)
     return b;
         else;
         return gcd(b,a%b);
 }


//��ٷ�

 int divisor (int a, int b) //�Զ��庯�������������Լ��

 {
      int  temp;//�������ͱ���
     temp=(a>b)?b:a;//��������������ʽ����������е���Сֵ
     while(temp>0)

      {
              if(a%temp==0&&b%temp==0)//ֻҪ�ҵ�һ������ͬʱ��a,b������������ֹѭ��
              break;
              temp--;//�粻����if����������Լ���ֱ���ܱ�a,b������ 
      } 
     return (temp);//���������������������������� 
  } 

//�������
 int gcd2(int m,int n)
 {
     int i=0,temp,x;
     while(m%2==0&&n%2==0)//�ж�m��n�ܱ����ٸ�2����
    {
         m/=2;
         n/=2;
         i+=1;
    } 
     if(m<n)//m������ֵ
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

  //Stein�㷨
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
        //printf("շת������������Լ��Ϊ��%d\n",gcd(a[i],b[i]));
        //printf("��ٷ��������Լ��Ϊ��%d\n",divisor(a[i],b[i]));
          printf("��������������Լ��Ϊ��%d\n",gcd2(a[i],b[i]));
        //printf("Stein�㷨�������Լ��Ϊ��%d\n",Stein(a[i],b[i]));
    }
 finish=clock();
 dur=(double)(finish-start)/CLOCKS_PER_SEC;
 printf("�������õ�ʱ��Ϊ��%lf s\n",dur); 
    return 0;
 }
