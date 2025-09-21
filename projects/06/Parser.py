import os
import re
from Type import Type

class Parser:
    def __init__(self, infile: str):
        self.__file = open(infile, 'r', encoding='UTF-8')
        self.__reset()
    
    def __del__(self):
        if hasattr(self, '__infile'):
            self.__file.close()
    
    def has_more_lines(self) -> bool:
        while True:
            init_pos = self.__file.tell() # 読み取り位置を戻す場所
            line = self.__file.readline()

            if len(line) == 0: # EOFに到達した場合
                return False
            
            # 末尾の改行と前後のスペースを除去して
            line = line.rstrip('\n')
            line = line.strip()
            
            if len(line) == 0: # スペース以外何も書かれていない行だった場合
                continue
            
            if len(line) >= 2 and line[:2] == '//': # コメントのみの行だった場合
                continue

            self.__file.seek(init_pos, os.SEEK_SET)
            return True

    def advance(self) -> None:
        self.__reset()
        line = self.__file.readline()
        print(line)
        line = line.strip('\n')
        line = line.strip()

        # 命令の形式
        # - A命令: @xxx
        # - C命令: [dest=]comp[;jump]

        if line[0] == '@': # A命令の場合
            self.__type = Type.A_INSTRUCTION
            for c in line[1:]:
                if not c.isdigit():
                    break
                self.__symbol += c
            return
        else: # C命令の場合
            self.__type = Type.C_INSTRUCTION
            pos = 0

            if self.__has_dest(line=line):
                end = line.find('=')
                self.__dest = line[pos:end]
                pos = end+1
            
            for ci, ch in enumerate(line[pos:]):
                if ch == ';':
                    self.__jump = re.split(r'[/ \t]', line[ci+1:], maxsplit=1)[0]
                    break
                
                if ch in [' ', '\t', '/']:
                    break

                self.__comp += ch

    def instruction_type(self) -> Type:
        return self.__type

    def symbol(self) -> str:
        return self.__symbol

    def dest(self) -> str:
        return self.__dest

    def comp(self) -> str:
        return self.__comp

    def jump(self) -> str:
        return self.__jump

    def __reset(self) -> None:
        self.__type = -1
        self.__symbol = ''
        self.__dest = 'null'
        self.__comp = ''
        self.__jump = 'null'
    
    def __has_dest(self, line, start=0) -> bool:
        COMP_TERMINATORS = [' ', '\t', ';', '/'] # compの終わりを示す字
        s = line[start:]
        
        for ci, ch in enumerate(s):
            if ch == '=':
                return True

            if ch in COMP_TERMINATORS: # compが終了
                return False
        
        return False
        