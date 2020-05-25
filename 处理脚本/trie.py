# 字典树
class TrieNode(object):
    def __init__(self):
        # 是否构成一个完成的单词
        self.is_word = False
        self.children = [None] * 26


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, s):
        """Add a string to this trie."""
        p = self.root
        n = len(s)
        for i in range(n):
            if p.children[ord(s[i]) - ord('a')] is None:
                new_node = TrieNode()
                if i == n - 1:
                    new_node.is_word = True
                p.children[ord(s[i]) - ord('a')] = new_node
                p = new_node
            else:
                p = p.children[ord(s[i]) - ord('a')]
                if i == n - 1:
                    p.is_word = True
                    return

    def search(self, s):
        """Judge whether s is in this trie."""

        p = self.root
        for c in s:
            p = p.children[ord(c) - ord('a')]
            if p is None:
                return False
        if p.is_word:
            return True
        else:
            return False


allPinyin = ["a", "ai", "an", "ang", "ao", "ba", "bao", "bai", "ban", "bang", "bei", "ben", "beng", "bi", "bian",
             "biao", "bie", "bin", "bing", "bo", "bu", "ca", "cai", "can", "cang", "cao", "ce", "cen", "ceng",
             "cha", "chai", "chan", "chang", "chao", "che", "chen", "cheng", "chong", "chou", "chi", "chu", "chua",
             "chuai", "chuan", "chuang", "chui", "chun", "chuo", "ci", "cong", "cou", "cu", "cuan", "cui", "cun",
             "cuo", "da", "dai", "dan", "dang", "dao", "de", "dei", "den", "deng", "di", "dian", "diao", "die",
             "ding", "diu", "dong", "dou", "du", "duan", "dui", "dun", "duo", "e", "ei", "en", "eng", "er", "fa",
             "fan", "fang", "fei", "fen", "feng", "fo", "fou", "fu", "ga", "gai", "gan", "gang", "gao", "ge", "gei",
             "gen", "geng", "gong", "gou", "gu", "gua", "guai", "guan", "guang", "gui", "gun", "guo", "ha", "hai",
             "han", "hang", "hao", "he", "hei", "hen", "heng", "hong", "hou", "hu", "hua", "huai", "huan", "huang",
             "hui", "hun", "huo", "ji", "jia", "jian", "jiang", "jiao", "jie", "jin", "jing", "jiong", "jiu", "ju",
             "juan", "jue", "jun", "ka", "kai", "kan", "kang", "kao", "ke", "ken", "keng", "kong", "kou", "ku",
             "kua", "kuai", "kuan", "kuang", "kui", "kun", "kuo", "la", "lai", "lan", "lang", "lao", "le", "lei",
             "leng", "li", "lia", "lian", "liang", "liao", "lie", "lin", "ling", "liu", "long", "lou", "lu", "lv",
             "luan", "lve", "lun", "luo", "ma", "mai", "man", "mang", "mao", "me", "mei", "men", "meng", "mi",
             "mian", "miao", "mie", "min", "ming", "miu", "mo", "mou", "mu", "na", "nai", "nan", "nang", "nao",
             "ne", "nei", "nen", "neng", "ni", "nian", "niang", "niao", "nie", "nin", "ning", "niu", "nong", "nou",
             "nu", "nv", "nuan", "nve", "nuaio", "o", "ou", "pa", "pai", "pan", "pang", "pao", "pei", "pen", "peng",
             "pi", "pian", "piao", "pie", "pin", "ping", "po", "pou", "pu", "qi", "qia", "qian", "qiang", "qiao",
             "qie", "qin", "qing", "qiong", "qiu", "qu", "quan", "que", "qun", "ran", "rang", "rao", "re", "ren",
             "reng", "ri", "rong", "rou", "ru", "ruan", "rui", "run", "ruo", "sa", "sai", "san", "sang", "sao",
             "se", "sen", "seng", "sha", "shai", "shan", "shang", "shao", "she", "shei", "shen", "sheng", "shou",
             "shi", "shu", "shua", "shuai", "shuan", "shuang", "shui", "shun", "shuo", "si", "song", "sou", "su",
             "suan", "sui", "sun", "suo", "ta", "tai", "tan", "tang", "tao", "te", "teng", "ti", "tian", "tiao",
             "tie", "ting", "tong", "tou", "tu", "tuan", "tui", "tun", "tuo", "wa", "wai", "wan", "wang", "wei",
             "wen", "weng", "wo", "wu", "xi", "xia", "xian", "xiang", "xiao", "xie", "xin", "xing", "xiong", "xiu",
             "xu", "xuan", "xue", "xun", "ya", "yan", "yang", "yao", "ye", "yi", "yin", "ying", "yong", "you", "yu",
             "yuan", "yue", "yun", "za", "zai", "zan", "zang", "zao", "ze", "zei", "zen", "zeng", "zha", "zhai",
             "zhan", "zhang", "zhao", "zhe", "zhei", "zhen", "zheng", "zhong", "zhou", "zhi", "zhu", "zhua",
             "zhuai", "zhuan", "zhuang", "zhui", "zhun", "zhuo", "zi", "zong", "zou", "zu", "zuan", "zui", "zun",
             "zuo"]
pinyinTree = Trie()
for i in allPinyin:
    pinyinTree.add(i)

