from antlr4 import InputStream, CommonTokenStream
from SimpleLangLexer import SimpleLangLexer
from SimpleLangParser import SimpleLangParser
from SimpleLangVisitor import SimpleLangVisitor


class PrettyPrinterVisitor(SimpleLangVisitor):
    def __init__(self):
        self.indent = 0
        self.INDENT = "    "
        self.lines = []

    def _emit(self, text: str):
        self.lines.append(self.INDENT * self.indent + text)

    def visitProgram(self, ctx: SimpleLangParser.ProgramContext):
        for st in ctx.statement():
            self.visit(st)
        return "\n".join(self.lines)

    def visitStatement(self, ctx: SimpleLangParser.StatementContext):
        if ctx.assignmentStatement():
            line = self.visit(ctx.assignmentStatement())
            self._emit(line)
        elif ctx.whileStatement():
            self.visit(ctx.whileStatement())
        elif ctx.ifStatement():
            self.visit(ctx.ifStatement())
        else:
            self._emit("")
        return None

    def visitAssignmentStatement(self, ctx: SimpleLangParser.AssignmentStatementContext):
        name = ctx.ID().getText()
        expr = self.visit(ctx.expression())
        return f"{name} := {expr}"

    def visitWhileStatement(self, ctx: SimpleLangParser.WhileStatementContext):
        cond = self.visit(ctx.expression())
        self._emit(f"while {cond} do")
        self.indent += 1
        for st in ctx.statement():
            self.visit(st)
        self.indent -= 1
        self._emit("end")
        return None

    def visitIfStatement(self, ctx: SimpleLangParser.IfStatementContext):
        cond = self.visit(ctx.expression())
        self._emit(f"if {cond} do")
        self.indent += 1

        all_stmts = ctx.statement()
        if ctx.ELSE():
            else_token = ctx.ELSE().getSymbol()
            then_stmts = []
            else_stmts = []
            for st in all_stmts:
                if st.start.tokenIndex < else_token.tokenIndex:
                    then_stmts.append(st)
                else:
                    else_stmts.append(st)

            for st in then_stmts:
                self.visit(st)
            self.indent -= 1
            self._emit("else do")
            self.indent += 1
            for st in else_stmts:
                self.visit(st)
            self.indent -= 1
            self._emit("end")
        else:
            for st in all_stmts:
                self.visit(st)
            self.indent -= 1
            self._emit("end")

        return None

    def visitExpression(self, ctx: SimpleLangParser.ExpressionContext):
        text = ctx.getText()
        for op in ["==", "!=", ">=", "<=", "<", ">", "+", "-", "*", "/"]:
            text = text.replace(op, f" {op} ")
        text = " ".join(text.split())
        return text
