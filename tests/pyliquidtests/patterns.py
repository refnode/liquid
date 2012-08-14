# Copyright 2012, refnode
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
from pyliquid.patterns import *


class PatternsTest(unittest.TestCase):
    """
    """

    def test_empty(self):
        self.assertEqual([], re.findall(QuotedFragment, ''))

    def test_quote(self):
        self.assertEqual(['"arg 1"'], re.findall(QuotedFragment, '"arg 1"'))

    def test_words(self):
        self.assertEqual(['arg1','arg2'],
                         re.findall(QuotedFragment, 'arg1 arg2'))

    def test_tags(self):
        self.assertEqual(['<tr>','</tr>'],
                         re.findall(QuotedFragment, '<tr> </tr>'))
        self.assertEqual(['<tr></tr>'],
                         re.findall(QuotedFragment, '<tr></tr>'))
        self.assertEqual(['<style','class="hello">','</style>'],
                         re.findall(QuotedFragment,
                                    '<style class="hello">\' </style>'))

    def test_quoted_words(self):
        self.assertEqual(['arg1','arg2','"arg 3"'],
                         re.findall(QuotedFragment, 'arg1 arg2 "arg 3"'))

    def test_quoted_words(self):
        self.assertEqual(['arg1', 'arg2', "'arg 3'"],
                         re.findall(QuotedFragment, 'arg1 arg2 \'arg 3\''))

    def test_quoted_words_in_the_middle(self):
        self.assertEqual(['arg1', 'arg2', '"arg 3"', 'arg4'],
                         re.findall(QuotedFragment, 'arg1 arg2 "arg 3" arg4   '))

    def test_variable_parser(self):
        self.assertEqual(['var'], re.findall(VariableParser, 'var'))
        self.assertEqual(['var', 'method'],
                         re.findall(VariableParser, 'var.method'))
        self.assertEqual(['var', '[method]'],
                         re.findall(VariableParser, 'var[method]'))
        self.assertEqual(['var', '[method]', '[0]'],
                         re.findall(VariableParser, 'var[method][0]'))
        self.assertEqual(['var', '["method"]', '[0]'],
                         re.findall(VariableParser, 'var["method"][0]'))
        self.assertEqual(['var', '[method]', '[0]', 'method'],
                         re.findall(VariableParser, 'var[method][0].method'))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(PatternsTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
