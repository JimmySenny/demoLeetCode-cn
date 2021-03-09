import java.util.Arrays;

public class ShellSort{
    public static void main(String[] args){
        int [] arr = {5,1,7,6,9,4,3,8,2};
        System.out.println("Before:"+Arrays.toString(arr));
        shellSort(arr);
        System.out.println("After:"+Arrays.toString(arr));
    }

    /**
     * 选择增量序列进行插入排序
     * @param arr
     */
    public static void shellSort(int [] arr){
        if (null==arr || 0==arr.length){
            return;
        }
        int len = arr.length;
        int tmp;

        //找出增量序列最大值
        int incer = selectIncer(len);
        System.out.println("Incer:"+incer);

        while(incer>0){
            /**
             * 排序
            for(int i=incer;i<len;i++){
                int j = i - incer;
                tmp = arr[i];
                while(j>=0 && arr[j]>tmp){
                    arr[j+incer] = arr[j];
                    j -= incer;
                }
                arr[j+incer] = tmp;
            }
             */
            /**
             * 标准插入排序
             */
            // 增量为k则有k此插入排序
            for(int k = 0; k < incer; k++){
                // 插入第一层
                for(int i=k; i<len-incer; i += incer){
                    // 插入第二层
                    for(int j = i+incer; j>k; j -= incer){
                        if(arr[j]<arr[j-incer]){
                            tmp = arr[j-incer];
                            arr[j-incer] = arr[j];
                            arr[j] = tmp;
                        }else{
                            break;
                        }
                    }
                }
            }

            // 下一个增量值
            incer = (int)Math.floor((incer-1)/2);
        }
    }

    /**
     * 找出增量序列最大值
     * @param len
     */
    public static int selectIncer(int len){
        // Hibbard增量 h(i+1) = 2h(i) + 1
        // 找出增量序列最大的增量值，也就是将序列分为incer组
        int incer = 1;
        while(2*incer+1 <= (len-1)/2){
            incer = 2*incer + 1;
        }
        return incer;
    }
}
