
import os
import re
import sys
from Code import Code
from Parser import Parser
from SymbolTable import SymbolTable
from Type import Type

class HackAssembler:
    def __init__(self, infile):
        if not os.path.isfile(infile):
            print('ファイルが存在しません: ' + infile, file=sys.stderr)
            sys.exit(1)
        
        ASM_EXTENTION = '.asm'
        HACK_EXTENTION = '.hack'
        self.__infile = infile
        self.__val_address = 16 # 変数に割り当てるアドレス

        self.__symbols = SymbolTable()
        # 定義済みシンボル
        self.__symbols.add_entry(symbol='R0', address=0)
        self.__symbols.add_entry(symbol='R1', address=1)
        self.__symbols.add_entry(symbol='R2', address=2)
        self.__symbols.add_entry(symbol='R3', address=3)
        self.__symbols.add_entry(symbol='R4', address=4)
        self.__symbols.add_entry(symbol='R5', address=5)
        self.__symbols.add_entry(symbol='R6', address=6)
        self.__symbols.add_entry(symbol='R7', address=7)
        self.__symbols.add_entry(symbol='R8', address=8)
        self.__symbols.add_entry(symbol='R9', address=9)
        self.__symbols.add_entry(symbol='R10', address=10)
        self.__symbols.add_entry(symbol='R11', address=11)
        self.__symbols.add_entry(symbol='R12', address=12)
        self.__symbols.add_entry(symbol='R13', address=13)
        self.__symbols.add_entry(symbol='R14', address=14)
        self.__symbols.add_entry(symbol='R15', address=15)
        self.__symbols.add_entry(symbol='SP', address=0)
        self.__symbols.add_entry(symbol='LCL', address=1)
        self.__symbols.add_entry(symbol='ARG', address=2)
        self.__symbols.add_entry(symbol='THIS', address=3)
        self.__symbols.add_entry(symbol='THAT', address=4)
        self.__symbols.add_entry(symbol='SCREEN', address=16384)
        self.__symbols.add_entry(symbol='KBD', address=24576)

        self.__parser = Parser(infile=infile)

        outfile = re.sub(ASM_EXTENTION+'$', '', infile) + HACK_EXTENTION
        self.__outfile = open(outfile, 'w', encoding='UTF-8')
    
    def __del__(self):
        if hasattr(self, '__outfile'):
            self.__outfile.close()
    
    def run(self) -> None:
        self.__collect_symbols()
        self.__generate_code()
    
    def __collect_symbols(self) -> None:
        with open(self.__infile, 'r', encoding='UTF-8') as f:
            address = 0
            for line in f:
                line = line.rstrip('\n')
                line = line.strip()

                if len(line) == 0 or line[0] == '/': # コード以外の記述
                    continue
                elif len(line) > 0 and line[0] == '(': # ラベル
                    symbol = line[1:].split(')', maxsplit=1)[0]
                    self.__symbols.add_entry(symbol=symbol, address=address)
                    continue
                else:
                    address += 1

    def __generate_code(self) -> None:
        binary = ''
        while self.__parser.has_more_lines():
            self.__parser.advance()
            match self.__parser.instruction_type():
                case Type.L_INSTRUCTION:
                    continue
                case Type.A_INSTRUCTION:
                    binary += '0'
                    symbol = self.__parser.symbol()
                    address = 0
                    if symbol.isdigit():
                        address = int(symbol)
                    else:
                        if self.__symbols.contains(symbol=symbol):
                            address = self.__symbols.get_address(symbol=symbol)
                        else: # シンボルが変数の場合
                            address = self.__consume_address()
                            self.__symbols.add_entry(symbol=symbol, address=address)
                    binary += format(address, "015b")
                case Type.C_INSTRUCTION:
                    binary += '111'
                    comp = Code.comp(self.__parser.comp())
                    dest = Code.dest(self.__parser.dest())
                    jump = Code.jump(self.__parser.jump())
                    binary += comp + dest + jump
            self.__outfile.write(binary)
            binary = '\n'
    
    def __consume_address(self) -> int:
        address = self.__val_address
        self.__val_address += 1
        return address

if __name__ == '__main__':
    infile = sys.argv[1]
    assembler = HackAssembler(infile=infile)
    assembler.run()