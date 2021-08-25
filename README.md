# password_brute_dictionary
口令爆破字典，有键盘组合字典、拼音字典、字母与数字混合这三种类型

随着安全意识的提升，常规的密码字典top100、top500啥的已经开始渐渐吃力起来，于是小弟决定做点工作更新一下口令爆破字典。

处理脚本中的match.py是从口令数据集中提取这三种类型口令的算法。

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
