
import os
import re
import sys
from Code import Code
from Parser import Parser
from Type import Type

class HackAssembler:
    def __init__(self, infile):
        if not os.path.isfile(infile):
            print('ファイルが存在しません: ' + infile, file=sys.stderr)
            sys.exit(1)
        
        ASM_EXTENTION = '.asm'
        HACK_EXTENTION = '.hack'

        self.__parser = Parser(infile=infile)

        outfile = re.sub(ASM_EXTENTION+'$', '', infile) + HACK_EXTENTION
        self.__outfile = open(outfile, 'w', encoding='UTF-8')
    
    def __del__(self):
        if hasattr(self, '__outfile'):
            self.__outfile.close()
    
    def run(self) -> None:
        binary = ''
        while self.__parser.has_more_lines():
            self.__parser.advance()
            match self.__parser.instruction_type():
                case Type.A_INSTRUCTION:
                    binary += '0'
                    binary += format(int(self.__parser.symbol()), "015b")
                case Type.C_INSTRUCTION:
                    binary += '111'
                    comp = Code.comp(self.__parser.comp())
                    dest = Code.dest(self.__parser.dest())
                    jump = Code.jump(self.__parser.jump())
                    binary += comp + dest + jump
            self.__outfile.write(binary)
            binary = '\n'

if __name__ == '__main__':
    infile = sys.argv[1]
    assembler = HackAssembler(infile=infile)
    assembler.run()