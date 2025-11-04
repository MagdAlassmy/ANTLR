from SimpleLangVisitor import SimpleLangVisitor
from SimpleLangParser import SimpleLangParser

class ProgramNode:
    def __init__(self, statements):
        self.statements = statements

class AssignNode:
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr

class WhileNode:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class IfNode:
    def __init__(self, condition, then_body, else_body=None):
        self.condition = condition
        self.then_body = then_body
        self.else_body = else_body

class BinaryOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class LiteralNode:
    def __init__(self, value):
        self.value = value

class VarNode:
    def __init__(self, name):
        self.name = name

class ASTBuilder(SimpleLangVisitor):
    def visitProgram(self, ctx: SimpleLangParser.ProgramContext):
        stmts = []
        for st in ctx.statement():
            node = self.visit(st)
            if node is not None:
                stmts.append(node)
        return ProgramNode(stmts)

    def visitStatement(self, ctx: SimpleLangParser.StatementContext):
        if ctx.assignmentStatement():
            return self.visit(ctx.assignmentStatement())
        if ctx.whileStatement():
            return self.visit(ctx.whileStatement())
        if ctx.ifStatement():
            return self.visit(ctx.ifStatement())
        return None

    def visitAssignmentStatement(self, ctx: SimpleLangParser.AssignmentStatementContext):
        name = ctx.ID().getText()
        expr = self.visit(ctx.expression())
        return AssignNode(name, expr)

    def visitWhileStatement(self, ctx: SimpleLangParser.WhileStatementContext):
        cond = self.visit(ctx.expression())
        body = [self.visit(st) for st in ctx.statement()]
        return WhileNode(cond, body)

    def visitIfStatement(self, ctx: SimpleLangParser.IfStatementContext):
        cond = self.visit(ctx.expression())
        if ctx.ELSE():
            else_token = ctx.ELSE().getSymbol()
            then_body = []
            else_body = []
            for st in ctx.statement():
                if st.start.tokenIndex < else_token.tokenIndex:
                    then_body.append(self.visit(st))
                else:
                    else_body.append(self.visit(st))
            return IfNode(cond, then_body, else_body)
        else:
            then_body = [self.visit(st) for st in ctx.statement()]
            return IfNode(cond, then_body)

    def visitExpression(self, ctx: SimpleLangParser.ExpressionContext):
        return self.visit(ctx.comparisonExpr())

    def visitComparisonExpr(self, ctx: SimpleLangParser.ComparisonExprContext):
        parts = ctx.additiveExpr()
        if len(parts) == 1:
            return self.visit(parts[0])
        left = self.visit(parts[0])
        for i in range(1, len(parts)):
            op = ctx.getChild(2 * i - 1).getText()
            right = self.visit(parts[i])
            left = BinaryOpNode(left, op, right)
        return left

    def visitAdditiveExpr(self, ctx: SimpleLangParser.AdditiveExprContext):
        parts = ctx.multiplicativeExpr()
        if len(parts) == 1:
            return self.visit(parts[0])
        left = self.visit(parts[0])
        for i in range(1, len(parts)):
            op = ctx.getChild(2 * i - 1).getText()
            right = self.visit(parts[i])
            left = BinaryOpNode(left, op, right)
        return left

    def visitMultiplicativeExpr(self, ctx: SimpleLangParser.MultiplicativeExprContext):
        parts = ctx.primary()
        if len(parts) == 1:
            return self.visit(parts[0])
        left = self.visit(parts[0])
        for i in range(1, len(parts)):
            op = ctx.getChild(2 * i - 1).getText()
            right = self.visit(parts[i])
            left = BinaryOpNode(left, op, right)
        return left

    def visitPrimary(self, ctx: SimpleLangParser.PrimaryContext):
        if ctx.ID():
            return VarNode(ctx.ID().getText())
        if ctx.INTEGER_LITERAL():
            return LiteralNode(int(ctx.INTEGER_LITERAL().getText()))
        if ctx.STRING_LITERAL():
            return LiteralNode(ctx.STRING_LITERAL().getText())
        if ctx.expression():
            return self.visit(ctx.expression())
        return None
