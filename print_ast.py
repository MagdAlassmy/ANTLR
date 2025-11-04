from antlr4 import *
from SimpleLangLexer import SimpleLangLexer
from SimpleLangParser import SimpleLangParser
from ast_builder import ASTBuilder

code = """a := 0
if 10 < 1 do
    a := 42
else do
    a := 7
end
"""

input_stream = InputStream(code)
lexer = SimpleLangLexer(input_stream)
tokens = CommonTokenStream(lexer)
parser = SimpleLangParser(tokens)
tree = parser.program()

builder = ASTBuilder()
ast_root = builder.visit(tree)

def print_ast(node, indent=0):
    space = "    " * indent
    if node is None:
        return

    from ast_builder import (
        ProgramNode, AssignNode, WhileNode, IfNode,
        BinaryOpNode, LiteralNode, VarNode
    )

    if isinstance(node, ProgramNode):
        print(space + "Program")
        for st in node.statements:
            print_ast(st, indent + 1)

    elif isinstance(node, AssignNode):
        print(space + f"Assign({node.name})")
        print_ast(node.expr, indent + 1)

    elif isinstance(node, WhileNode):
        print(space + "While")
        print(space + "  Condition:")
        print_ast(node.condition, indent + 2)
        print(space + "  Body:")
        for st in node.body:
            print_ast(st, indent + 2)

    elif isinstance(node, IfNode):
        print(space + "If")
        print(space + "  Condition:")
        print_ast(node.condition, indent + 2)
        print(space + "  Then:")
        for st in node.then_body:
            print_ast(st, indent + 2)
        if node.else_body:
            print(space + "  Else:")
            for st in node.else_body:
                print_ast(st, indent + 2)

    elif isinstance(node, BinaryOpNode):
        print(space + f"BinaryOp({node.op})")
        print_ast(node.left, indent + 1)
        print_ast(node.right, indent + 1)

    elif isinstance(node, LiteralNode):
        print(space + f"Literal({node.value})")

    elif isinstance(node, VarNode):
        print(space + f"Var({node.name})")

print("--- AST ---")
print_ast(ast_root)
