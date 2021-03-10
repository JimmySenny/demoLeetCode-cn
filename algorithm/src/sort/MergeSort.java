import java.util.Arrays;

public class MergeSort{
    public static void main(String[] args){
        int[] arr = {5,1,7,6,9,4,3,8,2};
        System.out.println("Before:"+Arrays.toString(arr));
        System.out.println("After:"+Arrays.toString(mergeSort(arr)));
    }

    /**
     * 常规解法
     */
    public static int[] mergeSort(int[] arr){
        if(null==arr || arr.length < 2){
            return arr;
        }

        // 在排序前，先建好一个长度等于原数组长度的临时数组，避免递归中频繁开辟空间
        int[] arrTmp = new int[arr.length];

        mergeSort(arr,0,arr.length-1,arrTmp);

        return arr;
    }

    public static void mergeSort(int[] arr,int left, int right, int[] arrTmp){
        System.out.println("sort:"+left+","+right);

        if(left < right){
            int mid = (left + right)/2;
            //左右边分别归并排序
            mergeSort(arr,left,mid,arrTmp);
            mergeSort(arr,mid+1,right,arrTmp);
            //将两个有序子数组合并操作
            merge(arr,left,mid,right,arrTmp);
        }
    }

    public static void merge(int[] arr, int left, int mid, int right, int[] arrTmp){
        int i = left; //左序列指针
        int j = mid + 1; //右序列指针
        int k = 0; //临时数组指针

        System.out.println("merge:"+left+","+mid+","+right);

        while(i<=mid && j <= right){
            if(arr[i] <= arr[j]){
                arrTmp[k++] = arr[i++];
            }else{
                arrTmp[k++] = arr[j++];
            }
        }

        while(i <= mid){
            arrTmp[k++] = arr[i++];
        }

        while(j <= right){
            arrTmp[k++] = arr[j++];
        }

        System.out.println("merge arrTmp:"+Arrays.toString(arrTmp));
        k = 0;
        //将temp中的元素全部拷贝到原数组中
        while(left <= right){
            arr[left++] = arrTmp[k++];
        }
        System.out.println("merge arr:"+Arrays.toString(arr));
        return;
    }
    /**
     * 
    public static int[] mergeSort(int[] arr){
        if(null==arr || arr.length < 2){
            return arr;
        }

        int mid = arr.length / 2;

        int[] left = Arrays.copyOfRange(arr,0,mid);
        int[] right = Arrays.copyOfRange(arr,mid,arr.length);
        return merge(mergeSort(left),mergeSort(right));
    }

    public static int[] merge(int[] left, int[] right){
        int[] result = new int[left.length + right.length];
        int i = 0;

        while(left.length > 0 && right.length > 0){
            if(left[0] <= right[0]){
                result[i++] = left[0];
                left = Arrays.copyOfRange(left,1,left.length);
            } else {
                result[i++] = right[0];
                right = Arrays.copyOfRange(right,1,right.length);
            }
        }

        while(left.length > 0){
            result[i++] = left[0];
            left = Arrays.copyOfRange(left,1,left.length);
        }

        while(right.length > 0){
            result[i++] = right[0];
            right = Arrays.copyOfRange(right,1,right.length);
        }

        return result;
    }
     */
}
