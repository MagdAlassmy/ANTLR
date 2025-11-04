# Generated from C:/Users/alass/PycharmProjects/PythonProject11/SimpleLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SimpleLangParser import SimpleLangParser
else:
    from SimpleLangParser import SimpleLangParser

# This class defines a complete generic visitor for a parse tree produced by SimpleLangParser.

class SimpleLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SimpleLangParser#program.
    def visitProgram(self, ctx:SimpleLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#statement.
    def visitStatement(self, ctx:SimpleLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:SimpleLangParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#whileStatement.
    def visitWhileStatement(self, ctx:SimpleLangParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#ifStatement.
    def visitIfStatement(self, ctx:SimpleLangParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#expression.
    def visitExpression(self, ctx:SimpleLangParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#comparisonExpr.
    def visitComparisonExpr(self, ctx:SimpleLangParser.ComparisonExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#additiveExpr.
    def visitAdditiveExpr(self, ctx:SimpleLangParser.AdditiveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#multiplicativeExpr.
    def visitMultiplicativeExpr(self, ctx:SimpleLangParser.MultiplicativeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#primary.
    def visitPrimary(self, ctx:SimpleLangParser.PrimaryContext):
        return self.visitChildren(ctx)



del SimpleLangParser