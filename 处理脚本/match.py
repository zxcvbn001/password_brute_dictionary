# -*- coding: utf-8 -*-

from .trie import pinyinTree


# 拼音
def pinyinMatch(S):
    S = S.lower()
    for ch in S:
        if ord(ch) not in range(97, 123):
            return False
    # print("目标1 " + S)
    # 如果直接搜索成功，则返回成功
    if pinyinTree.search(S):
        # print("命中 " + S)
        return True
    else:
        # 不成功则递归匹配前缀
        for i in range(1, len(S)):
            temp = S[0:len(S) - i]
            # print("目标2 " + temp)
            if pinyinTree.search(temp):
                # 前缀匹配成功则删除前缀继续匹配后面的
                # print("命中 " + temp)
                return pinyinMatch(S[len(S) - i:])
            else:
                # 如果到最后一个字符还搜索失败就直接返回false
                if i == len(S) - 1:
                    return False


# 键盘模式
# 同一行（例如，qwertyuio）、之字形（例如，qazsedcf）
def keyboardMatch(S):
    S = S.lower()
    keyDict = {
        '`': '1!',
        '~': '1!',
        '1': '2q@w~`',
        '!': '2q@w~`',
        '2': '1q3w#e',
        '@': '1q3w#e',
        '3': '2w4e$r',
        '#': '2w4e$r',
        '4': '3e5r%t',
        '$': '3e5r%t',
        '5': '4ry6t^',
        '%': '4ry6t^',
        '6': '5t7y&u',
        '^': '5t7y&u',
        '7': '6yi8u*',
        '&': '6yi8u*',
        '8': '7uoi(',
        '*': '7uoi(',
        '9': '8ip0o)',
        '(': '8ip0o)',
        '0': '9op[-{',
        ')': '9op[-{',
        '-': '0p[{}]+=',
        '+': '-{[]}',
        '=': '-{[]}',
        'q': '12was!@',
        'w': '123qaeds!@#',
        'e': '234wsrfd@#$',
        'r': '345edtgf#$%',
        't': '456rfyhg$%^',
        'y': '567tgujh%^&',
        'u': '678yhikj^&*',
        'i': '789ujolk&*(',
        'o': '890ikpl*();',
        'p': '90ol;()-[{',
        '[': '0)p-=+]};:',
        '{': '0)p-=+]};:',
        ']': '-=+{[',
        '}': '-=+{[',
        'a': 'qwsxz',
        's': 'qweadzcx',
        'd': 'wersfvxc',
        'f': 'ertdgcbv',
        'g': 'rftyhvnb',
        'h': 'tyugjbmn',
        'j': 'yuihknm,<',
        'k': 'uiojlm,.<>',
        'l': 'iopk;:,./<>?',
        ';': 'op[{l.>/?',
        ':': 'op[{l.>/?',
        'z': 'asx',
        'x': 'zasdc',
        'c': 'xsdfv',
        'v': 'cdfgb',
        'b': 'vfghn',
        'n': 'bghjm',
        'm': 'nhjk,<',
        ',': 'mjkl.>',
        '<': 'mjkl.>',
        '.': ',kl;:/?',
        '>': ',kl;:/?',
        '/': '.l;:>',
        '?': '.l;:>',
    }
    # 排除这些口令
    # T = ['1234', '12345', '123456', '1234567', '12345678', '123456789']
    # if S in T:
    #     return False
    if len(S) < 4:
        return False
    for i in range(0, len(S) - 1):
        # print(i)
        if S[i] not in keyDict.keys():
            return False
        if S[i + 1] in keyDict[S[i]]:
            continue
        else:
            return False
    return True


def digitMatch(S):
    for ch in S:
        if ord(ch) not in range(48, 58):
            return False
    return True

def letterMatch(S):
    for ch in S:
        if ord(ch) not in range(97, 123):
            return False
    return True

# Digit+letter
def digitAndLetterMatch(S):
    for ch in S:
        if ord(ch) not in range(48, 58) and ord(ch) not in range(97, 123):
            return False
    if digitMatch(S) or letterMatch(S):
        return False
    return True
    '''
    digit_pattern = re.compile(r'^\d+')
    if digit_pattern.findall(S):
        letter_pattern = re.compile(r'[a-z]+$')
        if letter_pattern.findall(S):
            return True
    return False
    '''

