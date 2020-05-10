# shell



[TOC]



## [192. 统计词频](https://leetcode-cn.com/problems/word-frequency/)

### tags: awk tr xargs 

写一个 bash 脚本以统计一个文本文件 words.txt 中每个单词出现的频率。

为了简单起见，你可以假设：

words.txt只包括小写字母和 ' ' 。
每个单词只由小写字母组成。
单词间由一个或多个空格字符分隔。
示例:

假设 words.txt 内容如下：

the day is sunny the the
the sunny is is
你的脚本应当输出（以词频降序排列）：

the 4
is 3
sunny 2
day 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-frequency
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



## [193. 有效电话号码](https://leetcode-cn.com/problems/valid-phone-numbers/)

### tags: 正则表达式

给定一个包含电话号码列表（一行一个电话号码）的文本文件 file.txt，写一个 bash 脚本输出所有有效的电话号码。

你可以假设一个有效的电话号码必须满足以下两种格式： (xxx) xxx-xxxx 或 xxx-xxx-xxxx。（x 表示一个数字）

你也可以假设每行前后没有多余的空格字符。

示例:

假设 file.txt 内容如下：

987-123-4567
123 456 7890
(123) 456-7890
你的脚本应当输出下列有效的电话号码：

987-123-4567
(123) 456-7890



## [194. 转置文件](https://leetcode-cn.com/problems/transpose-file/)

### tags: awk cut 

给定一个文件 file.txt，转置它的内容。

你可以假设每行列数相同，并且每个字段由 '  ' 分隔.

示例:

假设 file.txt 文件内容如下：

name age
alice 21
ryan 30
应当输出：

name alice ryan
age 21 30

## [195. 第十行](https://leetcode-cn.com/problems/tenth-line/)

### tags: head tail sed

给定一个文本文件 file.txt，请只打印这个文件中的第十行。

示例:

假设 file.txt 有如下内容：

Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10
你的脚本应当显示第十行：

Line 10
说明:
1. 如果文件少于十行，你应当输出什么？
2. 至少有三种不同的解法，请尝试尽可能多的方法来解题。


