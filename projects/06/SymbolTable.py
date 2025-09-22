class SymbolTable:
    def __init__(self):
        self.__symbols = {}

    def add_entry(self, symbol: str, address: int) -> None:
        self.__symbols[symbol] = address

    def contains(self, symbol: str) -> bool:
        try:
            self.__symbols[symbol]
            return True
        except KeyError:
            return False

    def get_address(self, symbol: str) -> int:
        return self.__symbols[symbol]