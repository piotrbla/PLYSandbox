from SimpleCompiler import *
import unittest


class TestSimpleCompiler(unittest.TestCase):

    def check_expectations(self, lexer, expected_tokens):
        for token, expected_token in \
                zip(lexer, expected_tokens):
            self.assertEqual(token.lineno, 1)
            self.assertEqual(expected_token[0], token.type)
            self.assertEqual(expected_token[1], token.value)

    def test_lexer_keyword(self):
        lexer = lex.lex()
        lexer.input('if (a == 10)')
        expected_tokens = [
            ('IF', 'if'),
            ('(', '('),
            ('ID',  'a'),
            ('EQUAL', '=='),
            ('NUMBER', 10),
            (')', ')')
        ]
        self.check_expectations(lexer, expected_tokens)

    def test_lexer_id(self):
        lexer = lex.lex()
        lexer.input('a b b99 99b')
        expected_tokens = [
            ('ID', 'a'),
            ('ID', 'b'),
            ('ID', 'b99'),
            ('NUMBER', 99),
            ('ID', 'b')
        ]
        self.check_expectations(lexer, expected_tokens)


if __name__ == '__main__':
    unittest.main()
