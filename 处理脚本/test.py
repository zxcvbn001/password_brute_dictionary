from 处理脚本.match import *

if __name__ == '__main__':
    print(digitMatch('0123456789'))
    print(digitMatch('0123456789#'))
    print(letterMatch('asSxcxzczxc'))
    print(letterMatch('!@#$%'))
    print(digitAndLetterMatch('asd1230'))