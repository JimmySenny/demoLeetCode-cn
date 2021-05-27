## 搭建测试框架参考



https://blog.csdn.net/m0_37302219/article/details/106938621



## 想实现的效果

main函数中如果换题测试只需要改一个地方
也就是我只需要把No1488这个地方换掉即可

        TextInterface problem = new No1488();
        problem.test();
比较方便放多个测试用例
比如这样。其实单独用一个txt文件来存放，进行文件读取应该更方便。这个后续如果有精力会继续完成，本文只是对于这个框架的设计提供一个思路   

@Override
    public List<String[]> getOriginalCase() {
        List<String[]> list = new ArrayList<>();
        addToList(list, "[1,2,0,3,0,3,0,0,3,3,3,0]", "");
        addToList(list, "[1,2,0,0,2,1]", "[-1,-1,2,1,-1,-1]");
        addToList(list, "[1,2,3,4]", "[-1,-1,-1,-1]");
        addToList(list, "[1,2,0,1,2]", "[]");
        addToList(list, "[69,0,0,0,69]", "[-1,69,1,1,-1]");
        addToList(list, "[10,20,20]", "");
        addToList(list, "[0,1,1]", "");
        addToList(list, "[1,0,2,0,2,1]", "[-1,1,-1,2,-1,-1]");
        addToList(list, "[1,0,2,3,0,1,2]", "[-1,1,-1,-1,2,-1,-1]");
        addToList(list, "[2,3,0,0,3,1,0,1,0,2,2]", "[]");
        return list;
    }

## 设计接口

那么想实现这个效果，自然会想到接口。那么开始思考接口需要怎么设计

因为每题的输入与输出是不同的，要看情况，因此需要定义两个泛型

TextInterface<I, O>

接口的主入口

//统一调用这个进行测试
test()

然后test需要：

调用测试用例
需要调用算法
需要比较输入与测试用例的差异
那么需要

    //用于比较输入与测试用例的差异
    boolean isEqual(O output, O expectedRes)
    //和测试主程序进行一次组合即可
    O testTask(I input);
    
    List<TextCaseHelper> getTestCase()

其中TextCaseHelper为

public class TextCaseHelper<I, O> {
    public I input;
    public String inputString;
    public O output;
    public String outputString;
}

因为LeetCode的测试用例都是字符串类型的，比如数组，它会给你[1,2,3]这样的形式。那么我们可以把“字符串类型”的测试用例与实际上我们最后生成的测试用例进行一个分离

因此我们还需要：

List<String[]> getOriginalCase();

//用于上面的方法进行调用添加
void addToList(List<String[]> list, String input, String output)

//实现转换
I changeInput(String input)
O changeOutput(String output)

那么完整的全貌大概如下：

因为java8已经支持了接口默认实现方法，所以如果测试类没有特殊的需求，我们几个方法都是可以用默认实现的，必须由调用类实现的只有两个方法

public interface TextInterface<I, O> {

    //调用这个进行测试
    default void test() {
        List<TextCaseHelper> list = getTestCase();
        for (TextCaseHelper<I, O> th : list) {
            I input = th.input;
            O output = testTask(input);
            O expectedRes = th.output;
            boolean isEqual = isEqual(output, expectedRes);
            if (!isEqual) {
                System.out.println("TestCase " + th.inputString + " 错误");
                System.out.println("正确的输出 " + th.outputString);
                continue;
            }
        }
    }
    
    //用于比较输入与测试用例的差异
    default boolean isEqual(O output, O expectedRes) {
        return output.equals(expectedRes);
    }
    
    //和测试主程序进行一次组合即可
    O testTask(I input);
    
    default List<TextCaseHelper> getTestCase() {
        List<TextCaseHelper> list = new ArrayList<>();
        List<String[]> originalCase = getOriginalCase();
        for (String[] strArr : originalCase) {
            TextCaseHelper<I, O> textCaseHelper = new TextCaseHelper<>();
            String inputString = strArr[0];
            String outputString = strArr[1];
            textCaseHelper.input = changeInput(inputString);
            textCaseHelper.inputString = inputString;
            textCaseHelper.outputString = outputString;
            textCaseHelper.output = changeOutput(outputString);
            list.add(textCaseHelper);
        }
        return list;
    }
    
    //原始样例数据
    List<String[]> getOriginalCase();


    default void addToList(List<String[]> list, String input, String output) {
        String[] temp = new String[2];
        temp[0] = input;
        temp[1] = output;
        list.add(temp);
    }
    
    //实现转换
    default I changeInput(String input) {
    
    }
    
    default O changeOutput(String output) {
    
    }
    调用类：
public class No1488 implements TextInterface<int[], int[]> {


    @Override
    public int[] testTask(int[] input) {
        return avoidFlood(input);
    }
    
    @Override
    public List<String[]> getOriginalCase() {
        List<String[]> list = new ArrayList<>();
        addToList(list, "[1,2,0,3,0,3,0,0,3,3,3,0]", "");
        addToList(list, "[1,2,0,0,2,1]", "[-1,-1,2,1,-1,-1]");
        addToList(list, "[1,2,3,4]", "[-1,-1,-1,-1]");
        addToList(list, "[1,2,0,1,2]", "[]");
        addToList(list, "[69,0,0,0,69]", "[-1,69,1,1,-1]");
        addToList(list, "[10,20,20]", "");
        addToList(list, "[0,1,1]", "");
        addToList(list, "[1,0,2,0,2,1]", "[-1,1,-1,2,-1,-1]");
        addToList(list, "[1,0,2,3,0,1,2]", "[-1,1,-1,-1,2,-1,-1]");
        addToList(list, "[2,3,0,0,3,1,0,1,0,2,2]", "[]");
        return list;
    }
    public int[] avoidFlood(int[] rains) {
    
    }
}


## 需要用到的转换

对于转换，我们首先希望它能很方便地扩展，同时我们只是出参不同，入参都是字符串。比如同样给你[1,2,3]
有可能是树，也有可能是数组，也可能是List

那么很自然地会想到工厂模式

同时我们希望它的这个生成过程能“自动化”，那么就需要用到反射了

首先是工厂类

public interface TestHelperFactory<T> {
    T produce(String s);
}
1
2
3
那么比如字符串转一维数组，我们就可以写成

public class IntArr_One_Factory implements TestHelperFactory<int[]> {

    @Override
    public int[] produce(String s) {
        String temp1 = s.replace("[", "");
        String temp2 = temp1.replace("]", "");
        if(temp2.length()==0){
            return new int[0];
        }
        String[] s2 = temp2.split(",");
        int n = s2.length;
        int[] res = new int[n];
        for (int i = 0; i < n; ++i) {
            res[i] = Integer.parseInt(s2[i]);
        }
        return res;
    }
}

然后我们建一个工厂选择器

public class FactorySelector {

    private ClassHelper classHelper;
    private Class<?> intArr_One_Class;//一维数组的class
    
    public FactorySelector() {
        classHelper = new ClassHelper();
        intArr_One_Class = classHelper.getIntArr_One_TypeName();
    }
    
    public TestHelperFactory getFactory(Class<?> className) {
        if (className.equals(intArr_One_Class)) {
            return new IntArr_One_Factory();
        }
        return null;
    }

}

其中

    public static Class<?> getIntArr_One_TypeName() {
        int[] arrOne = new int[0];
        return arrOne.getClass();
    }

用于返回一个数组的默认类型。那么上面的代码就可以实现：当我们的泛型是一维数组时，返回一个一维数组工厂

诸如此类，我们还可以定义各类Tree生成工厂等。这些代码可以参考我另一篇文章
LeetCode-测试用例生成方法与辅助函数等

完整的接口代码
那么基于这些，我们可以得到设计接口测试框架的完整代码了：

public interface LeetCodeTextInterface<I, O> {

    //调用这个进行测试
    default void test() {
        List<TextCaseHelper> list = getTestCase();
        for (TextCaseHelper<I, O> th : list) {
            I input = th.input;
            O output = testTask(input);
            O expectedRes = th.output;
            boolean isEqual = isEqual(output, expectedRes);
            if (!isEqual) {
                System.out.println("TestCase " + th.inputString + " 错误");
                System.out.println("正确的输出 " + th.outputString);
                continue;
            }
        }
    }
    
    //用于比较输入与测试用例的差异
    default boolean isEqual(O output, O expectedRes) {
        try {
            Class<?> oClass = output.getClass();
            String oClassTypeName = oClass.getTypeName();
    
            String intArr_One_TypeName = ClassHelper.getIntArr_One_ClassTypeName();
            if (oClassTypeName.equals(intArr_One_TypeName)) {
                return Arrays.equals((int[]) output, (int[]) expectedRes);
            }


        } catch (Exception exception) {
    
        }
        return output.equals(expectedRes);
    }
    
    //和测试主程序进行一次组合即可
    O testTask(I input);


    default List<TextCaseHelper> getTestCase() {
        List<TextCaseHelper> list = new ArrayList<>();
        List<String[]> originalCase = getOriginalCase();
        for (String[] strArr : originalCase) {
            TextCaseHelper<I, O> textCaseHelper = new TextCaseHelper<>();
            String inputString = strArr[0];
            String outputString = strArr[1];
            textCaseHelper.input = changeInput(inputString);
            textCaseHelper.inputString = inputString;
            textCaseHelper.outputString = outputString;
            textCaseHelper.output = changeOutput(outputString);
            list.add(textCaseHelper);
        }
        return list;
    }
    
    //原始样例数据
    List<String[]> getOriginalCase();


    default void addToList(List<String[]> list, String input, String output) {
        String[] temp = new String[2];
        temp[0] = input;
        temp[1] = output;
        list.add(temp);
    }
    
    //实现转换
    default I changeInput(String input) {
        String name = ClassHelper.getInterfaceTName(this, 0, 0);
        FactorySelector fs = new FactorySelector();
        TestHelperFactory<I> factory = fs.getFactory(name);
        return (I) factory.produce(input);
    }
    
    default O changeOutput(String output) {
        String name = ClassHelper.getInterfaceTName(this, 0, 1);
        FactorySelector fs = new FactorySelector();
        TestHelperFactory<O> factory = fs.getFactory(name);
        return (O) factory.produce(output);
    }
}
————————————————
版权声明：本文为CSDN博主「什么你竟然不会敲代码」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/m0_37302219/article/details/106938621