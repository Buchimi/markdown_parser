from Token import Token
from typing import List

class ASTNode:

    def __init__(self, token: Token, children : List[Token]) -> None:
        self.token = token
        self.children = children
        pass

    def __str__(self) -> str:
        return f"[{self.token} [{(i for i in self.children)}]]"
        pass
    