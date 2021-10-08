# password_brute_dictionary
## 前言

爆破，简单而粗暴，而成功的关键，我觉得在于字典。
随着安全意识的提升，常规的密码字典top100、top500啥的已经开始渐渐吃力起来，于是小弟决定做点工作更新一下密码爆破字典。
当然，收集信息然后按照一定的规则来生成字典，也是比较好的方式，但是不在本文讨论范围，这里只研究比较通用的密码爆破字典。
不想看过程的话直接跳到最后就能白嫖字典了。

## 数据来源

我下载了嘟嘟牛、7K7K、人人网、CSDN、178 游戏网等五个平台的泄露数据，只保留密码这一列，最后经过整理后的总行数为 42,208,168。详细情况如下表：
[![img](https://i.loli.net/2020/05/25/wtlurMF5RTN6IJZ.png)](https://i.loli.net/2020/05/25/wtlurMF5RTN6IJZ.png)
（数据量肯定是比不上大佬们的sgk的）

## 统计分析

b话一大堆，终于开始进入正题了。
我的思路是提取这些泄露数据中的各种类型的密码，然后按出现频率排序，比如键盘组合top100等等，就能得到各种类型的密码字典。下面细说：

### 键盘组合

键盘组合的密码，还是蛮常见的，我统计过这些网站泄露密码的top10：
[![img](https://i.loli.net/2020/05/25/gyomT6xHN5dbVWK.png)](https://i.loli.net/2020/05/25/gyomT6xHN5dbVWK.png)
可以看到我标红的那些，就是很明显的键盘组合的密码。
键盘组合的匹配方法：
（1） 根据键盘相邻的顺序，生成一组dict或者map，例如`<a,z>，<a,s>`；
（2） 再遍历字符串中的每个字符，判断它与它后面的一个字符是否在这组dict或者map中；
（3） 所有字符均满足此条件则返回True，否则False。
这样我们就能将泄露数据中键盘组合的密码给提取出来。

### 拼音

国人使用拼音也挺多的，比如“woaini”这些，搞一搞还是很有必要的。
提取拼音，稍微复杂一点点，得用到字典树，这里不罗嗦了，代码会放在github里面。

### 数字与字母混合

单一字符组成，现在很多网站都不允许这样设置密码了，所以我准备提取下非单一字符组成的密码，数字与字母混合算是一种比较经典的。最后提取出来发现占了全部密码数据的40%左右。

## 其他



```
1. 拼音 pinyinMatch
通过字典树进行匹配
2. 键盘组合 keyboardMatch
根据键盘序列来进行匹配
3. 纯数字 digitMatch
根据ascii码来匹配
4. 纯小写 letterMatch
根据ascii码来匹配
5. 数字和字母混合 digitAndLetterMatch
根据ascii码来匹配
```



### 排序

提取出来之后得按频率排序，这里我用的是Linux中的sort指令，例如把test.txt中的内容按重复次数降序输出

```
>sort test.txt | uniq -c | sort –rn
```

处理结果是这样，前面是次数，后面是密码：
[![img](https://i.loli.net/2020/05/25/4lNCJQT6mZMKLjs.png)](https://i.loli.net/2020/05/25/4lNCJQT6mZMKLjs.png)

## 结果

最后直接放结果吧：
https://github.com/huyuanzhi2/password_brute_dictionary
[![img](https://i.loli.net/2020/05/25/lZBjv23UqnC4QTX.png)](https://i.loli.net/2020/05/25/lZBjv23UqnC4QTX.png)
键盘组合与拼音类型的字典，都是top100、top500、全部三个文件：
[![img](https://i.loli.net/2020/05/25/9jyXWue6GlmZdPI.png)](https://i.loli.net/2020/05/25/9jyXWue6GlmZdPI.png)
字母数字混合的字典，由于太大，因此没放全部的，只到了top1000。
处理脚本目录中是用到的相关算法。

最后祝各位爆破必成功！

## todo
```
根据密码策略生成字典
自定义正则提取字典
```


# Stargazers over time

[![Stargazers over time](https://starchart.cc/huyuanzhi2/password_brute_dictionary.svg)](https://starchart.cc/huyuanzhi2/password_brute_dictionary)


文章地址 https://xz.aliyun.com/t/7823
