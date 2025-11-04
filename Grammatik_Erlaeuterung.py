"""
Erläuterungen zur Grammatik

program:
    Definiert ein Programm als eine oder mehrere Anweisungen (statement+) gefolgt von EOF.

statement:
    Beschreibt die möglichen Arten von Anweisungen. Jede Anweisung wird durch NEWLINE beendet,
    damit der Parser erkennen kann, wo eine Zeile endet.

whileStatement / ifStatement:
    Entsprechen der im Aufgabentext definierten Syntax:
    - Schlüsselwort (while / if)
    - Bedingung (expression)
    - do
    - Block aus Anweisungen
    - end
    Beim if ist ein else-Teil optional.
    Die Blöcke werden als (NEWLINE statement)* modelliert, damit mehrere Anweisungen im Block möglich sind.

Expressions:
    Die Operatoren haben unterschiedliche Prioritäten. In einer erweiterten Version würde man
    separate Regeln für Vergleich, Addition/Subtraktion und Multiplikation/Division einführen,
    um Punkt-vor-Strich sicherzustellen.

Lexer:
    - Schlüsselwörter werden als einzelne Tokens definiert.
    - Längere Operatoren wie '==' oder '>=' werden vor kürzeren wie '=' oder '>' definiert,
      damit der Lexer den längstmöglichen Token erkennt.
    - NEWLINE wird nicht geskippt, weil Zeilenenden Teil der Syntax sind.
    - Kommentare und Whitespace werden mit '-> skip' ignoriert.
"""
