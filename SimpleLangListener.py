# Generated from C:/Users/alass/PycharmProjects/PythonProject11/SimpleLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SimpleLangParser import SimpleLangParser
else:
    from SimpleLangParser import SimpleLangParser

# This class defines a complete listener for a parse tree produced by SimpleLangParser.
class SimpleLangListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleLangParser#program.
    def enterProgram(self, ctx:SimpleLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#program.
    def exitProgram(self, ctx:SimpleLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#statement.
    def enterStatement(self, ctx:SimpleLangParser.StatementContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#statement.
    def exitStatement(self, ctx:SimpleLangParser.StatementContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:SimpleLangParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:SimpleLangParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#whileStatement.
    def enterWhileStatement(self, ctx:SimpleLangParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#whileStatement.
    def exitWhileStatement(self, ctx:SimpleLangParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#ifStatement.
    def enterIfStatement(self, ctx:SimpleLangParser.IfStatementContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#ifStatement.
    def exitIfStatement(self, ctx:SimpleLangParser.IfStatementContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#expression.
    def enterExpression(self, ctx:SimpleLangParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#expression.
    def exitExpression(self, ctx:SimpleLangParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#comparisonExpr.
    def enterComparisonExpr(self, ctx:SimpleLangParser.ComparisonExprContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#comparisonExpr.
    def exitComparisonExpr(self, ctx:SimpleLangParser.ComparisonExprContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#additiveExpr.
    def enterAdditiveExpr(self, ctx:SimpleLangParser.AdditiveExprContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#additiveExpr.
    def exitAdditiveExpr(self, ctx:SimpleLangParser.AdditiveExprContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#multiplicativeExpr.
    def enterMultiplicativeExpr(self, ctx:SimpleLangParser.MultiplicativeExprContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#multiplicativeExpr.
    def exitMultiplicativeExpr(self, ctx:SimpleLangParser.MultiplicativeExprContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#primary.
    def enterPrimary(self, ctx:SimpleLangParser.PrimaryContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#primary.
    def exitPrimary(self, ctx:SimpleLangParser.PrimaryContext):
        pass



del SimpleLangParser