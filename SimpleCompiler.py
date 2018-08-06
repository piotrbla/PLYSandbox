import ply.lex as lex
from sys import stdin
from os import sys

tokens = ('NUMBER', 'ID', 'EQUAL', 'IF', 'THEN', 'ELSE', 'WHILE')
t_EQUAL = '=='
t_ignore = ' \t'

literals = ['+', '-', '*', '/', '(', ')', '=']
# literals = "+-*/()"
reserved = {
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'while': 'WHILE'
}


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def main():
    lexer = lex.lex()
    if len(sys.argv) > 1:
        fh = open(sys.argv[1], "r")
    else:
        fh = stdin

    lexer.input(fh.read())
    for token in lexer:
        print("line %d: %s(%s)" % (token.lineno, token.type, token.value))


if __name__ == '__main__':
    main()

