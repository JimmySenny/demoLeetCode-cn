
import java.util.Arrays;

public class QuickSort{
    public static void main(String[] args){
        int [] arr = {5,1,7,6,9,4,3,8,2};
        System.out.println("Before:"+Arrays.toString(arr));
        quickSort(arr);
        System.out.println("After:"+Arrays.toString(arr));
    }

    /**
     * @param arr
     */
    public static void quickSort(int [] arr){
        if (null==arr || arr.length < 2){
            return;
        }

        quickSort(arr, 0, arr.length - 1);
    }

    /**
     * 简化模板
     * @param arr
     * @param left 左指针
     * @param right 右指针
    public static void quickSort(int[] arr, int left, int right){
        if(left < right){
            int i = left, j = right, x = arr[left];
            while(i < j){
                // 从右向左找第一个小于x的数
                while(i < j && arr[j] >= x){
                    j--;
                }
                if(i < j){
                    arr[i++] = arr[j];
                }
                // 从左向右找第一个大于等于x的数
                while(i < j && arr[i] < x){
                    i++;
                }
                if(i < j){
                    arr[j--] = arr[i];
                }
            }
            arr[i] = x;
            quickSort(arr, left, i-1);
            quickSort(arr, i+1, right);
        }
    }
     */

    public static void quickSort(int[] arr, int left, int right){
        if(left < right){
            // 获取枢纽值，并将其放在当前待处理序列末尾
            getPivot(arr, left, right);
            // 枢纽值被放在序列末尾
            int pivot = right - 1;
            // 左右指针
            int i = left, j = right - 1;

            while(true){
                while(arr[++i] < arr[pivot]){
                }
                while(j > left && arr[--j] > arr[pivot]){
                }

                if(i < j){
                    swap(arr, i, j);
                }else{
                    break;
                }
            }

            if(i < right){
                swap(arr, i, right - 1);
            }

            quickSort(arr, left, i -1);
            quickSort(arr, i + 1, right);
        }
    }

    public static void getPivot(int[] arr, int left, int right){
        int mid = (left + right)/2;
        if(arr[left] > arr[mid]){
            swap(arr, left, mid);
        }

        if(arr[left] > arr[right]){
            swap(arr, left, right);
        }

        if(arr[right] < arr[mid]){
            swap(arr, right, mid);
        }
        swap(arr, right - 1, mid);
    }

    /**
     * 递归法 易于理解 基准值固定为左边元素，通过快慢指针找到枢纽值实际位置
     * @param arr
     * @param left 左指针
     * @param right 右指针
     */
    /*
    public static void quickSort(int []arr, int left, int right){
        if(left < right){
            // 获取枢纽值
            int indexPivot = dealPivot(arr, left, right);
            // 递归处理
            quickSort(arr, left, indexPivot - 1);
            quickSort(arr, indexPivot + 1, right);
        }
    }

    public static int dealPivot(int[] arr, int left, int right){
        // 选定一个基准值，基准值可以随机取任何一个值，这里选择最左边的元素作为基准值
        // index永远指向基准值位置的下一个位置，或者说，index左边的都是比基准值小的元素
        int index = left + 1;
        // 开始遍历序列，基准值选择了最左边的元素，所以从第二个开始往后，挨个和基准值比较
        for(int i = index; i <= right; i++){
            // i是从前往后的一个快指针 index是慢指针
            if(arr[i] < arr[left]){
                // 如果比基准值小，说明它应该在基准值的左边，
                // 交换i和index位置的元素位置，保证index左边都是比它小的元素
                swap(arr, i, index);
                index++;
            }
        }
        //最后，把index左边的元素和基准值交换，
        //因为index左边的元素本来就是比基准值小的，所以换完对排序没影响
        swap(arr, left, index - 1);

        // 最后基准值的位置就是index-1，下一次迭代，就是迭代基准值左边和右边的。
        return index - 1;
    }
     */

    private static void swap (int[] arr, int i, int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}
