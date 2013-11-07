# Copyright 2013, refnode http://refnode.com
# All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# import std
import re
import unittest
# import third party
# import local
from liquid.lexer import Lexer


class LexerTest(unittest.TestCase):
    """
    """

    def test_simple_strings(self):
        tokens = Lexer(''' "double quote test" ''').tokenize()
        self.assertListEqual(tokens, [[':string', '"double quote test"'],
                                      [':end_of_string']])
        tokens = Lexer(""" 'single quote test' """).tokenize()
        self.assertListEqual(tokens, [[':string', "'single quote test'"],
                                      [':end_of_string']])

    def test_strings(self):
        tokens = Lexer(''' 'this is a test""' "wat 'lol'" ''').tokenize()
        self.assertListEqual(tokens, [[':string', """'this is a test""'"""],
                                      [':string', '''"wat 'lol'"'''],
                                      [':end_of_string']])

    def test_integer(self):
        tokens = Lexer('hi 50').tokenize()
        self.assertListEqual(tokens, [[':id' ,'hi'],
                                      [':number', '50'],
                                      [':end_of_string']])
 
    def test_float(self):
        tokens = Lexer('hi 5.0').tokenize()
        self.assertListEqual(tokens, [[':id', 'hi'],
                                      [':number', '5.0'],
                                      [':end_of_string']])
 
    def test_comparison(self):
        tokens = Lexer('== <> contains').tokenize()
        self.assertListEqual(tokens, [[':comparison', '=='],
                                      [':comparison', '<>'],
                                      [':comparison', 'contains'],
                                      [':end_of_string']])

    def test_specials(self):
        tokens = Lexer('| .:').tokenize()
        self.assertListEqual(tokens, [[':pipe', '|'],
                                      [':dot', '.'],
                                      [':colon', ':'],
                                      [':end_of_string']])
        tokens = Lexer('[,]').tokenize()
        self.assertListEqual(tokens, [[':open_square', '['],
                                      [':comma', ','],
                                      [':close_square', ']'],
                                      [':end_of_string']])

    def test_fancy_identifiers(self):
        tokens = Lexer('hi! five?').tokenize()
        self.assertListEqual(tokens, [[':id' ,'hi!'],
                                      [':id', 'five?'],
                                      [':end_of_string']])

    def test_whitespace(self):
        tokens = Lexer("five|\n\t ==").tokenize()
        self.assertListEqual(tokens, [[':id', 'five'],
                                      [':pipe', '|'],
                                      [':comparison', '=='],
                                      [':end_of_string']])

    def test_unexpected_character(self):
        self.assertRaises(SyntaxError, Lexer("%").tokenize)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LexerTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
