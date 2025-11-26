# Generated from ToyLangParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,44,300,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,1,0,3,0,64,8,0,1,0,3,0,67,
        8,0,1,0,3,0,70,8,0,1,1,1,1,1,1,1,1,4,1,76,8,1,11,1,12,1,77,1,2,1,
        2,4,2,82,8,2,11,2,12,2,83,1,3,1,3,4,3,88,8,3,11,3,12,3,89,1,4,3,
        4,93,8,4,1,4,1,4,3,4,97,8,4,1,4,1,4,1,4,1,5,1,5,1,5,5,5,105,8,5,
        10,5,12,5,108,9,5,1,5,3,5,111,8,5,1,5,1,5,1,5,3,5,116,8,5,1,6,1,
        6,1,6,3,6,121,8,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,5,8,130,8,8,10,8,12,
        8,133,9,8,3,8,135,8,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,143,8,8,10,8,12,
        8,146,9,8,3,8,148,8,8,1,9,1,9,1,9,1,9,3,9,154,8,9,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,5,10,165,8,10,10,10,12,10,168,9,10,
        1,10,1,10,1,10,3,10,173,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,
        1,14,1,14,4,14,197,8,14,11,14,12,14,198,1,14,1,14,3,14,203,8,14,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,214,8,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,5,15,228,
        8,15,10,15,12,15,231,9,15,1,16,1,16,3,16,235,8,16,1,17,1,17,3,17,
        239,8,17,1,18,1,18,1,18,1,18,5,18,245,8,18,10,18,12,18,248,9,18,
        1,18,1,18,1,18,1,18,3,18,254,8,18,1,19,1,19,1,19,5,19,259,8,19,10,
        19,12,19,262,9,19,1,19,1,19,1,20,1,20,1,20,1,20,5,20,270,8,20,10,
        20,12,20,273,9,20,1,21,1,21,1,22,1,22,1,23,1,23,3,23,281,8,23,1,
        24,1,24,1,25,1,25,1,26,1,26,1,27,1,27,1,28,1,28,1,29,1,29,1,29,1,
        30,1,30,1,30,1,30,1,30,0,1,30,31,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,0,6,1,1,
        42,42,1,0,13,14,1,0,20,23,1,0,6,7,1,0,24,29,1,0,17,19,308,0,63,1,
        0,0,0,2,75,1,0,0,0,4,81,1,0,0,0,6,87,1,0,0,0,8,92,1,0,0,0,10,115,
        1,0,0,0,12,120,1,0,0,0,14,122,1,0,0,0,16,134,1,0,0,0,18,153,1,0,
        0,0,20,155,1,0,0,0,22,174,1,0,0,0,24,181,1,0,0,0,26,186,1,0,0,0,
        28,202,1,0,0,0,30,213,1,0,0,0,32,234,1,0,0,0,34,238,1,0,0,0,36,253,
        1,0,0,0,38,255,1,0,0,0,40,265,1,0,0,0,42,274,1,0,0,0,44,276,1,0,
        0,0,46,280,1,0,0,0,48,282,1,0,0,0,50,284,1,0,0,0,52,286,1,0,0,0,
        54,288,1,0,0,0,56,290,1,0,0,0,58,292,1,0,0,0,60,295,1,0,0,0,62,64,
        3,2,1,0,63,62,1,0,0,0,63,64,1,0,0,0,64,66,1,0,0,0,65,67,3,4,2,0,
        66,65,1,0,0,0,66,67,1,0,0,0,67,69,1,0,0,0,68,70,3,6,3,0,69,68,1,
        0,0,0,69,70,1,0,0,0,70,1,1,0,0,0,71,72,3,14,7,0,72,73,5,42,0,0,73,
        76,1,0,0,0,74,76,5,42,0,0,75,71,1,0,0,0,75,74,1,0,0,0,76,77,1,0,
        0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,3,1,0,0,0,79,82,3,8,4,0,80,82,
        5,42,0,0,81,79,1,0,0,0,81,80,1,0,0,0,82,83,1,0,0,0,83,81,1,0,0,0,
        83,84,1,0,0,0,84,5,1,0,0,0,85,88,3,10,5,0,86,88,5,42,0,0,87,85,1,
        0,0,0,87,86,1,0,0,0,88,89,1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,90,
        7,1,0,0,0,91,93,3,38,19,0,92,91,1,0,0,0,92,93,1,0,0,0,93,94,1,0,
        0,0,94,96,5,43,0,0,95,97,3,40,20,0,96,95,1,0,0,0,96,97,1,0,0,0,97,
        98,1,0,0,0,98,99,5,32,0,0,99,100,3,28,14,0,100,9,1,0,0,0,101,106,
        3,12,6,0,102,103,5,33,0,0,103,105,3,12,6,0,104,102,1,0,0,0,105,108,
        1,0,0,0,106,104,1,0,0,0,106,107,1,0,0,0,107,110,1,0,0,0,108,106,
        1,0,0,0,109,111,5,33,0,0,110,109,1,0,0,0,110,111,1,0,0,0,111,112,
        1,0,0,0,112,113,7,0,0,0,113,116,1,0,0,0,114,116,3,18,9,0,115,101,
        1,0,0,0,115,114,1,0,0,0,116,11,1,0,0,0,117,121,3,14,7,0,118,121,
        3,16,8,0,119,121,5,15,0,0,120,117,1,0,0,0,120,118,1,0,0,0,120,119,
        1,0,0,0,121,13,1,0,0,0,122,123,5,43,0,0,123,124,5,31,0,0,124,125,
        3,30,15,0,125,15,1,0,0,0,126,131,3,30,15,0,127,128,5,34,0,0,128,
        130,3,30,15,0,129,127,1,0,0,0,130,133,1,0,0,0,131,129,1,0,0,0,131,
        132,1,0,0,0,132,135,1,0,0,0,133,131,1,0,0,0,134,126,1,0,0,0,134,
        135,1,0,0,0,135,136,1,0,0,0,136,137,5,30,0,0,137,147,5,43,0,0,138,
        139,5,30,0,0,139,144,5,43,0,0,140,141,5,34,0,0,141,143,5,43,0,0,
        142,140,1,0,0,0,143,146,1,0,0,0,144,142,1,0,0,0,144,145,1,0,0,0,
        145,148,1,0,0,0,146,144,1,0,0,0,147,138,1,0,0,0,147,148,1,0,0,0,
        148,17,1,0,0,0,149,154,3,20,10,0,150,154,3,22,11,0,151,154,3,24,
        12,0,152,154,3,26,13,0,153,149,1,0,0,0,153,150,1,0,0,0,153,151,1,
        0,0,0,153,152,1,0,0,0,154,19,1,0,0,0,155,156,5,10,0,0,156,157,3,
        30,15,0,157,158,5,32,0,0,158,166,3,28,14,0,159,160,5,11,0,0,160,
        161,3,30,15,0,161,162,5,32,0,0,162,163,3,28,14,0,163,165,1,0,0,0,
        164,159,1,0,0,0,165,168,1,0,0,0,166,164,1,0,0,0,166,167,1,0,0,0,
        167,172,1,0,0,0,168,166,1,0,0,0,169,170,5,12,0,0,170,171,5,32,0,
        0,171,173,3,28,14,0,172,169,1,0,0,0,172,173,1,0,0,0,173,21,1,0,0,
        0,174,175,5,5,0,0,175,176,5,43,0,0,176,177,5,6,0,0,177,178,3,30,
        15,0,178,179,5,32,0,0,179,180,3,28,14,0,180,23,1,0,0,0,181,182,5,
        8,0,0,182,183,3,30,15,0,183,184,5,32,0,0,184,185,3,28,14,0,185,25,
        1,0,0,0,186,187,5,4,0,0,187,188,5,32,0,0,188,189,3,28,14,0,189,190,
        5,9,0,0,190,191,3,30,15,0,191,27,1,0,0,0,192,203,3,12,6,0,193,194,
        5,42,0,0,194,196,5,1,0,0,195,197,3,10,5,0,196,195,1,0,0,0,197,198,
        1,0,0,0,198,196,1,0,0,0,198,199,1,0,0,0,199,200,1,0,0,0,200,201,
        5,2,0,0,201,203,1,0,0,0,202,192,1,0,0,0,202,193,1,0,0,0,203,29,1,
        0,0,0,204,205,6,15,-1,0,205,206,3,54,27,0,206,207,3,30,15,3,207,
        214,1,0,0,0,208,209,5,35,0,0,209,210,3,30,15,0,210,211,5,36,0,0,
        211,214,1,0,0,0,212,214,3,32,16,0,213,204,1,0,0,0,213,208,1,0,0,
        0,213,212,1,0,0,0,214,229,1,0,0,0,215,216,10,6,0,0,216,217,3,44,
        22,0,217,218,3,30,15,7,218,228,1,0,0,0,219,220,10,5,0,0,220,221,
        3,46,23,0,221,222,3,30,15,6,222,228,1,0,0,0,223,224,10,4,0,0,224,
        225,3,52,26,0,225,226,3,30,15,5,226,228,1,0,0,0,227,215,1,0,0,0,
        227,219,1,0,0,0,227,223,1,0,0,0,228,231,1,0,0,0,229,227,1,0,0,0,
        229,230,1,0,0,0,230,31,1,0,0,0,231,229,1,0,0,0,232,235,3,34,17,0,
        233,235,5,43,0,0,234,232,1,0,0,0,234,233,1,0,0,0,235,33,1,0,0,0,
        236,239,3,36,18,0,237,239,3,42,21,0,238,236,1,0,0,0,238,237,1,0,
        0,0,239,35,1,0,0,0,240,241,5,37,0,0,241,246,3,32,16,0,242,243,5,
        34,0,0,243,245,3,32,16,0,244,242,1,0,0,0,245,248,1,0,0,0,246,244,
        1,0,0,0,246,247,1,0,0,0,247,249,1,0,0,0,248,246,1,0,0,0,249,250,
        5,38,0,0,250,254,1,0,0,0,251,254,3,58,29,0,252,254,3,60,30,0,253,
        240,1,0,0,0,253,251,1,0,0,0,253,252,1,0,0,0,254,37,1,0,0,0,255,260,
        5,43,0,0,256,257,5,34,0,0,257,259,5,43,0,0,258,256,1,0,0,0,259,262,
        1,0,0,0,260,258,1,0,0,0,260,261,1,0,0,0,261,263,1,0,0,0,262,260,
        1,0,0,0,263,264,5,30,0,0,264,39,1,0,0,0,265,266,5,30,0,0,266,271,
        5,43,0,0,267,268,5,34,0,0,268,270,5,43,0,0,269,267,1,0,0,0,270,273,
        1,0,0,0,271,269,1,0,0,0,271,272,1,0,0,0,272,41,1,0,0,0,273,271,1,
        0,0,0,274,275,7,1,0,0,275,43,1,0,0,0,276,277,7,2,0,0,277,45,1,0,
        0,0,278,281,3,48,24,0,279,281,3,50,25,0,280,278,1,0,0,0,280,279,
        1,0,0,0,281,47,1,0,0,0,282,283,7,3,0,0,283,49,1,0,0,0,284,285,7,
        4,0,0,285,51,1,0,0,0,286,287,7,5,0,0,287,53,1,0,0,0,288,289,5,16,
        0,0,289,55,1,0,0,0,290,291,5,30,0,0,291,57,1,0,0,0,292,293,5,37,
        0,0,293,294,5,38,0,0,294,59,1,0,0,0,295,296,5,37,0,0,296,297,5,41,
        0,0,297,298,5,38,0,0,298,61,1,0,0,0,34,63,66,69,75,77,81,83,87,89,
        92,96,106,110,115,120,131,134,144,147,153,166,172,198,202,213,227,
        229,234,238,246,253,260,271,280
    ]

class ToyLangParser ( Parser ):

    grammarFileName = "ToyLangParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'out'", "'do'", 
                     "'for'", "'in'", "'not in'", "'while'", "'until'", 
                     "'if'", "'elif'", "'else'", "'true'", "'false'", "'pass'", 
                     "'not'", "'and'", "'or'", "'xor'", "'+'", "'*'", "'@'", 
                     "'\\'", "'=='", "'<>'", "'>'", "'<'", "'>='", "'<='", 
                     "'->'", "'='", "':'", "';'", "','", "'('", "')'", "'{'", 
                     "'}'", "'['", "']'", "'..'" ]

    symbolicNames = [ "<INVALID>", "INDENT", "DEDENT", "OUT", "DO", "FOR", 
                      "IN", "NOT_IN", "WHILE", "UNTIL", "IF", "ELIF", "ELSE", 
                      "TRUE", "FALSE", "PASS", "NOT", "AND", "OR", "XOR", 
                      "UNION", "INTERSECTION", "CARTESIAN", "DIFFERENCE", 
                      "EQ", "NE", "GT", "LT", "GE", "LE", "ARROW", "EQUAL", 
                      "COLON", "SEMICOLON", "COMMA", "LPAREN", "RPAREN", 
                      "LBRACE", "RBRACE", "LBRACK", "RBRACK", "DOTDOT", 
                      "NEWLINE", "ID", "SKIP_" ]

    RULE_program = 0
    RULE_vars = 1
    RULE_subprograms = 2
    RULE_body = 3
    RULE_subprogram = 4
    RULE_statement = 5
    RULE_simple_statement = 6
    RULE_assignment = 7
    RULE_call = 8
    RULE_compound_statement = 9
    RULE_if_ = 10
    RULE_for_ = 11
    RULE_while_ = 12
    RULE_until_ = 13
    RULE_block = 14
    RULE_expr = 15
    RULE_atom = 16
    RULE_literal = 17
    RULE_set_ = 18
    RULE_in_params = 19
    RULE_out_params = 20
    RULE_bool_ = 21
    RULE_setOperator = 22
    RULE_conditionalOperator = 23
    RULE_elementOperator = 24
    RULE_comparisonOperator = 25
    RULE_logicalOperator = 26
    RULE_unaryOperator = 27
    RULE_funcOperator = 28
    RULE_emptySet = 29
    RULE_uniSet = 30

    ruleNames =  [ "program", "vars", "subprograms", "body", "subprogram", 
                   "statement", "simple_statement", "assignment", "call", 
                   "compound_statement", "if_", "for_", "while_", "until_", 
                   "block", "expr", "atom", "literal", "set_", "in_params", 
                   "out_params", "bool_", "setOperator", "conditionalOperator", 
                   "elementOperator", "comparisonOperator", "logicalOperator", 
                   "unaryOperator", "funcOperator", "emptySet", "uniSet" ]

    EOF = Token.EOF
    INDENT=1
    DEDENT=2
    OUT=3
    DO=4
    FOR=5
    IN=6
    NOT_IN=7
    WHILE=8
    UNTIL=9
    IF=10
    ELIF=11
    ELSE=12
    TRUE=13
    FALSE=14
    PASS=15
    NOT=16
    AND=17
    OR=18
    XOR=19
    UNION=20
    INTERSECTION=21
    CARTESIAN=22
    DIFFERENCE=23
    EQ=24
    NE=25
    GT=26
    LT=27
    GE=28
    LE=29
    ARROW=30
    EQUAL=31
    COLON=32
    SEMICOLON=33
    COMMA=34
    LPAREN=35
    RPAREN=36
    LBRACE=37
    RBRACE=38
    LBRACK=39
    RBRACK=40
    DOTDOT=41
    NEWLINE=42
    ID=43
    SKIP_=44

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vars_(self):
            return self.getTypedRuleContext(ToyLangParser.VarsContext,0)


        def subprograms(self):
            return self.getTypedRuleContext(ToyLangParser.SubprogramsContext,0)


        def body(self):
            return self.getTypedRuleContext(ToyLangParser.BodyContext,0)


        def getRuleIndex(self):
            return ToyLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = ToyLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 62
                self.vars_()


            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 65
                self.subprograms()


            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 13367012091184) != 0):
                self.state = 68
                self.body()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ToyLangParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(ToyLangParser.AssignmentContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ToyLangParser.NEWLINE)
            else:
                return self.getToken(ToyLangParser.NEWLINE, i)

        def getRuleIndex(self):
            return ToyLangParser.RULE_vars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVars" ):
                listener.enterVars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVars" ):
                listener.exitVars(self)




    def vars_(self):

        localctx = ToyLangParser.VarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_vars)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 75
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [43]:
                        self.state = 71
                        self.assignment()
                        self.state = 72
                        self.match(ToyLangParser.NEWLINE)
                        pass
                    elif token in [42]:
                        self.state = 74
                        self.match(ToyLangParser.NEWLINE)
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 77 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubprogramsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subprogram(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ToyLangParser.SubprogramContext)
            else:
                return self.getTypedRuleContext(ToyLangParser.SubprogramContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ToyLangParser.NEWLINE)
            else:
                return self.getToken(ToyLangParser.NEWLINE, i)

        def getRuleIndex(self):
            return ToyLangParser.RULE_subprograms

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubprograms" ):
                listener.enterSubprograms(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubprograms" ):
                listener.exitSubprograms(self)




    def subprograms(self):

        localctx = ToyLangParser.SubprogramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_subprograms)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 81
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [43]:
                        self.state = 79
                        self.subprogram()
                        pass
                    elif token in [42]:
                        self.state = 80
                        self.match(ToyLangParser.NEWLINE)
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 83 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ToyLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(ToyLangParser.StatementContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ToyLangParser.NEWLINE)
            else:
                return self.getToken(ToyLangParser.NEWLINE, i)

        def getRuleIndex(self):
            return ToyLangParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)




    def body(self):

        localctx = ToyLangParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 87
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4, 5, 8, 10, 13, 14, 15, 16, 30, 35, 37, 43]:
                    self.state = 85
                    self.statement()
                    pass
                elif token in [42]:
                    self.state = 86
                    self.match(ToyLangParser.NEWLINE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 89 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 13367012091184) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubprogramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ToyLangParser.ID, 0)

        def COLON(self):
            return self.getToken(ToyLangParser.COLON, 0)

        def block(self):
            return self.getTypedRuleContext(ToyLangParser.BlockContext,0)


        def in_params(self):
            return self.getTypedRuleContext(ToyLangParser.In_paramsContext,0)


        def out_params(self):
            return self.getTypedRuleContext(ToyLangParser.Out_paramsContext,0)


        def getRuleIndex(self):
            return ToyLangParser.RULE_subprogram

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubprogram" ):
                listener.enterSubprogram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubprogram" ):
                listener.exitSubprogram(self)




    def subprogram(self):

        localctx = ToyLangParser.SubprogramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_subprogram)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 91
                self.in_params()


            self.state = 94
            self.match(ToyLangParser.ID)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 95
                self.out_params()


            self.state = 98
            self.match(ToyLangParser.COLON)
            self.state = 99
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ToyLangParser.Simple_statementContext)
            else:
                return self.getTypedRuleContext(ToyLangParser.Simple_statementContext,i)


        def NEWLINE(self):
            return self.getToken(ToyLangParser.NEWLINE, 0)

        def EOF(self):
            return self.getToken(ToyLangParser.EOF, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(ToyLangParser.SEMICOLON)
            else:
                return self.getToken(ToyLangParser.SEMICOLON, i)

        def compound_statement(self):
            return self.getTypedRuleContext(ToyLangParser.Compound_statementContext,0)


        def getRuleIndex(self):
            return ToyLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = ToyLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 15, 16, 30, 35, 37, 43]:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.simple_statement()
                self.state = 106
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 102
                        self.match(ToyLangParser.SEMICOLON)
                        self.state = 103
                        self.simple_statement() 
                    self.state = 108
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==33:
                    self.state = 109
                    self.match(ToyLangParser.SEMICOLON)


                self.state = 112
                _la = self._input.LA(1)
                if not(_la==-1 or _la==42):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [4, 5, 8, 10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.compound_statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(ToyLangParser.AssignmentContext,0)


        def call(self):
            return self.getTypedRuleContext(ToyLangParser.CallContext,0)


        def PASS(self):
            return self.getToken(ToyLangParser.PASS, 0)

        def getRuleIndex(self):
            return ToyLangParser.RULE_simple_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_statement" ):
                listener.enterSimple_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_statement" ):
                listener.exitSimple_statement(self)




    def simple_statement(self):

        localctx = ToyLangParser.Simple_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_simple_statement)
        try:
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 119
                self.match(ToyLangParser.PASS)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ToyLangParser.ID, 0)

        def EQUAL(self):
            return self.getToken(ToyLangParser.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(ToyLangParser.ExprContext,0)


        def getRuleIndex(self):
            return ToyLangParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = ToyLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(ToyLangParser.ID)
            self.state = 123
            self.match(ToyLangParser.EQUAL)
            self.state = 124
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARROW(self, i:int=None):
            if i is None:
                return self.getTokens(ToyLangParser.ARROW)
            else:
                return self.getToken(ToyLangParser.ARROW, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ToyLangParser.ID)
            else:
                return self.getToken(ToyLangParser.ID, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ToyLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(ToyLangParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ToyLangParser.COMMA)
            else:
                return self.getToken(ToyLangParser.COMMA, i)

        def getRuleIndex(self):
            return ToyLangParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)




    def call(self):

        localctx = ToyLangParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8967891804160) != 0):
                self.state = 126
                self.expr(0)
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==34:
                    self.state = 127
                    self.match(ToyLangParser.COMMA)
                    self.state = 128
                    self.expr(0)
                    self.state = 133
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 136
            self.match(ToyLangParser.ARROW)
            self.state = 137
            self.match(ToyLangParser.ID)
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 138
                self.match(ToyLangParser.ARROW)
                self.state = 139
                self.match(ToyLangParser.ID)
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==34:
                    self.state = 140
                    self.match(ToyLangParser.COMMA)
                    self.state = 141
                    self.match(ToyLangParser.ID)
                    self.state = 146
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compound_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_(self):
            return self.getTypedRuleContext(ToyLangParser.If_Context,0)


        def for_(self):
            return self.getTypedRuleContext(ToyLangParser.For_Context,0)


        def while_(self):
            return self.getTypedRuleContext(ToyLangParser.While_Context,0)


        def until_(self):
            return self.getTypedRuleContext(ToyLangParser.Until_Context,0)


        def getRuleIndex(self):
            return ToyLangParser.RULE_compound_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompound_statement" ):
                listener.enterCompound_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompound_statement" ):
                listener.exitCompound_statement(self)




    def compound_statement(self):

        localctx = ToyLangParser.Compound_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_compound_statement)
        try:
            self.state = 153
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.if_()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.for_()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 151
                self.while_()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 152
                self.until_()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ToyLangParser.IF, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ToyLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(ToyLangParser.ExprContext,i)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(ToyLangParser.COLON)
            else:
                return self.getToken(ToyLangParser.COLON, i)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ToyLangParser.BlockContext)
            else:
                return self.getTypedRuleContext(ToyLangParser.BlockContext,i)


        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(ToyLangParser.ELIF)
            else:
                return self.getToken(ToyLangParser.ELIF, i)

        def ELSE(self):
            return self.getToken(ToyLangParser.ELSE, 0)

        def getRuleIndex(self):
            return ToyLangParser.RULE_if_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_" ):
                listener.enterIf_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_" ):
                listener.exitIf_(self)




    def if_(self):

        localctx = ToyLangParser.If_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_if_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(ToyLangParser.IF)
            self.state = 156
            self.expr(0)
            self.state = 157
            self.match(ToyLangParser.COLON)
            self.state = 158
            self.block()
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 159
                self.match(ToyLangParser.ELIF)
                self.state = 160
                self.expr(0)
                self.state = 161
                self.match(ToyLangParser.COLON)
                self.state = 162
                self.block()
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 169
                self.match(ToyLangParser.ELSE)
                self.state = 170
                self.match(ToyLangParser.COLON)
                self.state = 171
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ToyLangParser.FOR, 0)

        def ID(self):
            return self.getToken(ToyLangParser.ID, 0)

        def IN(self):
            return self.getToken(ToyLangParser.IN, 0)

        def expr(self):
            return self.getTypedRuleContext(ToyLangParser.ExprContext,0)


        def COLON(self):
            return self.getToken(ToyLangParser.COLON, 0)

        def block(self):
            return self.getTypedRuleContext(ToyLangParser.BlockContext,0)


        def getRuleIndex(self):
            return ToyLangParser.RULE_for_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_" ):
                listener.enterFor_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_" ):
                listener.exitFor_(self)




    def for_(self):

        localctx = ToyLangParser.For_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_for_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(ToyLangParser.FOR)
            self.state = 175
            self.match(ToyLangParser.ID)
            self.state = 176
            self.match(ToyLangParser.IN)
            self.state = 177
            self.expr(0)
            self.state = 178
            self.match(ToyLangParser.COLON)
            self.state = 179
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(ToyLangParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(ToyLangParser.ExprContext,0)


        def COLON(self):
            return self.getToken(ToyLangParser.COLON, 0)

        def block(self):
            return self.getTypedRuleContext(ToyLangParser.BlockContext,0)


        def getRuleIndex(self):
            return ToyLangParser.RULE_while_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_" ):
                listener.enterWhile_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_" ):
                listener.exitWhile_(self)




    def while_(self):

        localctx = ToyLangParser.While_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_while_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(ToyLangParser.WHILE)
            self.state = 182
            self.expr(0)
            self.state = 183
            self.match(ToyLangParser.COLON)
            self.state = 184
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Until_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(ToyLangParser.DO, 0)

        def COLON(self):
            return self.getToken(ToyLangParser.COLON, 0)

        def block(self):
            return self.getTypedRuleContext(ToyLangParser.BlockContext,0)


        def UNTIL(self):
            return self.getToken(ToyLangParser.UNTIL, 0)

        def expr(self):
            return self.getTypedRuleContext(ToyLangParser.ExprContext,0)


        def getRuleIndex(self):
            return ToyLangParser.RULE_until_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUntil_" ):
                listener.enterUntil_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUntil_" ):
                listener.exitUntil_(self)




    def until_(self):

        localctx = ToyLangParser.Until_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_until_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(ToyLangParser.DO)
            self.state = 187
            self.match(ToyLangParser.COLON)
            self.state = 188
            self.block()
            self.state = 189
            self.match(ToyLangParser.UNTIL)
            self.state = 190
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_statement(self):
            return self.getTypedRuleContext(ToyLangParser.Simple_statementContext,0)


        def NEWLINE(self):
            return self.getToken(ToyLangParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(ToyLangParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(ToyLangParser.DEDENT, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ToyLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(ToyLangParser.StatementContext,i)


        def getRuleIndex(self):
            return ToyLangParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = ToyLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.state = 202
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 15, 16, 30, 35, 37, 43]:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.simple_statement()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.match(ToyLangParser.NEWLINE)
                self.state = 194
                self.match(ToyLangParser.INDENT)
                self.state = 196 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 195
                    self.statement()
                    self.state = 198 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 8968965580080) != 0)):
                        break

                self.state = 200
                self.match(ToyLangParser.DEDENT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryOperator(self):
            return self.getTypedRuleContext(ToyLangParser.UnaryOperatorContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ToyLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(ToyLangParser.ExprContext,i)


        def LPAREN(self):
            return self.getToken(ToyLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ToyLangParser.RPAREN, 0)

        def atom(self):
            return self.getTypedRuleContext(ToyLangParser.AtomContext,0)


        def setOperator(self):
            return self.getTypedRuleContext(ToyLangParser.SetOperatorContext,0)


        def conditionalOperator(self):
            return self.getTypedRuleContext(ToyLangParser.ConditionalOperatorContext,0)


        def logicalOperator(self):
            return self.getTypedRuleContext(ToyLangParser.LogicalOperatorContext,0)


        def getRuleIndex(self):
            return ToyLangParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ToyLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.state = 205
                self.unaryOperator()
                self.state = 206
                self.expr(3)
                pass
            elif token in [35]:
                self.state = 208
                self.match(ToyLangParser.LPAREN)
                self.state = 209
                self.expr(0)
                self.state = 210
                self.match(ToyLangParser.RPAREN)
                pass
            elif token in [13, 14, 37, 43]:
                self.state = 212
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 229
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 227
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                    if la_ == 1:
                        localctx = ToyLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 215
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 216
                        self.setOperator()
                        self.state = 217
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = ToyLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 219
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 220
                        self.conditionalOperator()
                        self.state = 221
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = ToyLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 223
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 224
                        self.logicalOperator()
                        self.state = 225
                        self.expr(5)
                        pass

             
                self.state = 231
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(ToyLangParser.LiteralContext,0)


        def ID(self):
            return self.getToken(ToyLangParser.ID, 0)

        def getRuleIndex(self):
            return ToyLangParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = ToyLangParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_atom)
        try:
            self.state = 234
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.literal()
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.match(ToyLangParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def set_(self):
            return self.getTypedRuleContext(ToyLangParser.Set_Context,0)


        def bool_(self):
            return self.getTypedRuleContext(ToyLangParser.Bool_Context,0)


        def getRuleIndex(self):
            return ToyLangParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = ToyLangParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_literal)
        try:
            self.state = 238
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.set_()
                pass
            elif token in [13, 14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.bool_()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Set_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(ToyLangParser.LBRACE, 0)

        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ToyLangParser.AtomContext)
            else:
                return self.getTypedRuleContext(ToyLangParser.AtomContext,i)


        def RBRACE(self):
            return self.getToken(ToyLangParser.RBRACE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ToyLangParser.COMMA)
            else:
                return self.getToken(ToyLangParser.COMMA, i)

        def emptySet(self):
            return self.getTypedRuleContext(ToyLangParser.EmptySetContext,0)


        def uniSet(self):
            return self.getTypedRuleContext(ToyLangParser.UniSetContext,0)


        def getRuleIndex(self):
            return ToyLangParser.RULE_set_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSet_" ):
                listener.enterSet_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSet_" ):
                listener.exitSet_(self)




    def set_(self):

        localctx = ToyLangParser.Set_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_set_)
        self._la = 0 # Token type
        try:
            self.state = 253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.match(ToyLangParser.LBRACE)
                self.state = 241
                self.atom()
                self.state = 246
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==34:
                    self.state = 242
                    self.match(ToyLangParser.COMMA)
                    self.state = 243
                    self.atom()
                    self.state = 248
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 249
                self.match(ToyLangParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                self.emptySet()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 252
                self.uniSet()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class In_paramsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ToyLangParser.ID)
            else:
                return self.getToken(ToyLangParser.ID, i)

        def ARROW(self):
            return self.getToken(ToyLangParser.ARROW, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ToyLangParser.COMMA)
            else:
                return self.getToken(ToyLangParser.COMMA, i)

        def getRuleIndex(self):
            return ToyLangParser.RULE_in_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIn_params" ):
                listener.enterIn_params(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIn_params" ):
                listener.exitIn_params(self)




    def in_params(self):

        localctx = ToyLangParser.In_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_in_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(ToyLangParser.ID)
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 256
                self.match(ToyLangParser.COMMA)
                self.state = 257
                self.match(ToyLangParser.ID)
                self.state = 262
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 263
            self.match(ToyLangParser.ARROW)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Out_paramsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARROW(self):
            return self.getToken(ToyLangParser.ARROW, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ToyLangParser.ID)
            else:
                return self.getToken(ToyLangParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ToyLangParser.COMMA)
            else:
                return self.getToken(ToyLangParser.COMMA, i)

        def getRuleIndex(self):
            return ToyLangParser.RULE_out_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOut_params" ):
                listener.enterOut_params(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOut_params" ):
                listener.exitOut_params(self)




    def out_params(self):

        localctx = ToyLangParser.Out_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_out_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(ToyLangParser.ARROW)
            self.state = 266
            self.match(ToyLangParser.ID)
            self.state = 271
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 267
                self.match(ToyLangParser.COMMA)
                self.state = 268
                self.match(ToyLangParser.ID)
                self.state = 273
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(ToyLangParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ToyLangParser.FALSE, 0)

        def getRuleIndex(self):
            return ToyLangParser.RULE_bool_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_" ):
                listener.enterBool_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_" ):
                listener.exitBool_(self)




    def bool_(self):

        localctx = ToyLangParser.Bool_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_bool_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            _la = self._input.LA(1)
            if not(_la==13 or _la==14):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNION(self):
            return self.getToken(ToyLangParser.UNION, 0)

        def INTERSECTION(self):
            return self.getToken(ToyLangParser.INTERSECTION, 0)

        def CARTESIAN(self):
            return self.getToken(ToyLangParser.CARTESIAN, 0)

        def DIFFERENCE(self):
            return self.getToken(ToyLangParser.DIFFERENCE, 0)

        def getRuleIndex(self):
            return ToyLangParser.RULE_setOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetOperator" ):
                listener.enterSetOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetOperator" ):
                listener.exitSetOperator(self)




    def setOperator(self):

        localctx = ToyLangParser.SetOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_setOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15728640) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elementOperator(self):
            return self.getTypedRuleContext(ToyLangParser.ElementOperatorContext,0)


        def comparisonOperator(self):
            return self.getTypedRuleContext(ToyLangParser.ComparisonOperatorContext,0)


        def getRuleIndex(self):
            return ToyLangParser.RULE_conditionalOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionalOperator" ):
                listener.enterConditionalOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionalOperator" ):
                listener.exitConditionalOperator(self)




    def conditionalOperator(self):

        localctx = ToyLangParser.ConditionalOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_conditionalOperator)
        try:
            self.state = 280
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.elementOperator()
                pass
            elif token in [24, 25, 26, 27, 28, 29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 279
                self.comparisonOperator()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IN(self):
            return self.getToken(ToyLangParser.IN, 0)

        def NOT_IN(self):
            return self.getToken(ToyLangParser.NOT_IN, 0)

        def getRuleIndex(self):
            return ToyLangParser.RULE_elementOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementOperator" ):
                listener.enterElementOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementOperator" ):
                listener.exitElementOperator(self)




    def elementOperator(self):

        localctx = ToyLangParser.ElementOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_elementOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            _la = self._input.LA(1)
            if not(_la==6 or _la==7):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(ToyLangParser.EQ, 0)

        def NE(self):
            return self.getToken(ToyLangParser.NE, 0)

        def GT(self):
            return self.getToken(ToyLangParser.GT, 0)

        def LT(self):
            return self.getToken(ToyLangParser.LT, 0)

        def GE(self):
            return self.getToken(ToyLangParser.GE, 0)

        def LE(self):
            return self.getToken(ToyLangParser.LE, 0)

        def getRuleIndex(self):
            return ToyLangParser.RULE_comparisonOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonOperator" ):
                listener.enterComparisonOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonOperator" ):
                listener.exitComparisonOperator(self)




    def comparisonOperator(self):

        localctx = ToyLangParser.ComparisonOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_comparisonOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1056964608) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(ToyLangParser.AND, 0)

        def OR(self):
            return self.getToken(ToyLangParser.OR, 0)

        def XOR(self):
            return self.getToken(ToyLangParser.XOR, 0)

        def getRuleIndex(self):
            return ToyLangParser.RULE_logicalOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOperator" ):
                listener.enterLogicalOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOperator" ):
                listener.exitLogicalOperator(self)




    def logicalOperator(self):

        localctx = ToyLangParser.LogicalOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_logicalOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 917504) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ToyLangParser.NOT, 0)

        def getRuleIndex(self):
            return ToyLangParser.RULE_unaryOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryOperator" ):
                listener.enterUnaryOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryOperator" ):
                listener.exitUnaryOperator(self)




    def unaryOperator(self):

        localctx = ToyLangParser.UnaryOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_unaryOperator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(ToyLangParser.NOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARROW(self):
            return self.getToken(ToyLangParser.ARROW, 0)

        def getRuleIndex(self):
            return ToyLangParser.RULE_funcOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncOperator" ):
                listener.enterFuncOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncOperator" ):
                listener.exitFuncOperator(self)




    def funcOperator(self):

        localctx = ToyLangParser.FuncOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_funcOperator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(ToyLangParser.ARROW)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EmptySetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(ToyLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ToyLangParser.RBRACE, 0)

        def getRuleIndex(self):
            return ToyLangParser.RULE_emptySet

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptySet" ):
                listener.enterEmptySet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptySet" ):
                listener.exitEmptySet(self)




    def emptySet(self):

        localctx = ToyLangParser.EmptySetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_emptySet)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(ToyLangParser.LBRACE)
            self.state = 293
            self.match(ToyLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UniSetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(ToyLangParser.LBRACE, 0)

        def DOTDOT(self):
            return self.getToken(ToyLangParser.DOTDOT, 0)

        def RBRACE(self):
            return self.getToken(ToyLangParser.RBRACE, 0)

        def getRuleIndex(self):
            return ToyLangParser.RULE_uniSet

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUniSet" ):
                listener.enterUniSet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUniSet" ):
                listener.exitUniSet(self)




    def uniSet(self):

        localctx = ToyLangParser.UniSetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_uniSet)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(ToyLangParser.LBRACE)
            self.state = 296
            self.match(ToyLangParser.DOTDOT)
            self.state = 297
            self.match(ToyLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[15] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         




