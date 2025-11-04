from antlr4 import InputStream, CommonTokenStream
from SimpleLangLexer import SimpleLangLexer
from SimpleLangParser import SimpleLangParser
from pretty_printer_visitor import PrettyPrinterVisitor

#Beispielcode (korrekt formatiert, ohne überflüssige Leerzeilen)
code = """
a := 0
if 10 < 1 do
    a := 42
else do
    a := 7
end
"""

#Lexer und Parser aufbauen
lexer = SimpleLangLexer(InputStream(code))
tokens = CommonTokenStream(lexer)
parser = SimpleLangParser(tokens)
tree = parser.program()

#Pretty Printer ausführen
printer = PrettyPrinterVisitor()
formatted = printer.visit(tree)

# Ausgabe
print("--- Formatiertes Programm ---")
print(formatted)
