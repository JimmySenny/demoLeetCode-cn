
import java.util.Arrays;

public class HeapSort{
    public static void main(String[] args){
        //int [] arr = {5,1,7,6,9,4,3,8,2};
        int [] arr = {3,2,3,1,2,4,5,5,6};
        System.out.println("Before:"+Arrays.toString(arr));
        maxHeapSort(arr);
        System.out.println("After:"+Arrays.toString(arr));
    }

    /**
     * 构建和调整使用同一份逻辑的堆排序
     * @param arr
     */
    public static void maxHeapSort(int [] arr){
        if (null==arr || 0==arr.length){
            return;
        }

        // 构建大顶堆
        buildMaxHeap(arr);
        System.out.println("buildMaxHeap:"+Arrays.toString(arr));

        // 调整堆结构 交换堆顶元素与末尾元素
        for(int j = arr.length-1;j>0;j--){
            swap(arr, 0, j); // 将堆顶元素与末尾元素进行交换
            adjustHeap(arr,0,j);
        }
    }

    /**
     * 构建大顶堆
     * @param arr
     */
    public static void buildMaxHeap(int []arr){
        // 从最后一个非叶节点开始向前遍历
        // (int)Math.floor(arr.length / 2) - 1)
        for(int i = arr.length/2 - 1; i>=0;i--){
            adjustHeap(arr,i,arr.length);
        }
    }

    /**
     * 调整大顶堆（仅是调整过程，建立在大顶堆已构建的基础上）
     * @param arr
     * @param i
     * @param length
     */
    public static void adjustHeap(int []arr,int i,int len){
        /**
         * recursion 递归解决
         */
        // 根据堆性质，找出它左右子节点的索引
        int indexLeft = 2*i + 1;
        int indexRight = indexLeft + 1;
        // 默认当前节点（父节点）是最大值。
        int indexMax = i; 
        if(indexLeft<len && arr[indexLeft] > arr[indexMax]){
            indexMax = indexLeft;
        }
        if(indexRight<len && arr[indexRight] > arr[indexMax]){
            indexMax = indexRight;
        }

        if(indexMax != i){
            swap(arr,i,indexMax);
            // 因为互换之后，子节点的值变了，
            // 如果该子节点也有自己的子节点，仍需要再次调整。
            adjustHeap(arr,indexMax,len);
        }
        /**
         * 
        // 先取出当前元素i的值
        int temp = 0;
        // j指i节点子节点的子节点
        int j = 2*i+1;
        // 从i结点的左子结点开始，也就是2i+1处开始
        while(j<len){
            //如果左子结点小于右子结点，j指向右子结点
            if(j+1<len && arr[j+1]>arr[j]){
                j++;
            }

            if(arr[i]>=arr[j]){
                break;
            }

            swap(arr,i,j);

            i = j;
            j = 2*i+1;
        }
         */
        /**
         *
        int temp = arr[i];//先取出当前元素i
        //从i结点的左子结点开始，也就是2i+1处开始]
        for(int k=i*2+1;k<len;k=k*2+1){
            //如果左子结点小于右子结点，k指向右子结点
            if(k+1<len && arr[k]<arr[k+1]){
                k++;
            }
            //如果子节点大于父节点，将子节点值赋给父节点（不用进行交换）
            if(arr[k] >temp){
                arr[i] = arr[k];
                i = k;
            }else{
                break;
            }
        }
        arr[i] = temp;//将temp值放到最终的位置
         */
    }

    /**
     * 交换元素
     * @param arr
     * @param a
     * @param b
     */
    public static void swap(int []arr,int a ,int b){
        int temp=arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }
}
