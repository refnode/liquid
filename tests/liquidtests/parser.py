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
import unittest
# import third party
# import local
from liquid.parser import Parser


class ParserTest(unittest.TestCase):
    """
    """

    def test_consume(self):
        p = Parser("wat: 7")
        self.assertEqual('wat', p.consume(':id'))
        self.assertEqual(':', p.consume(':colon'))
        self.assertEqual('7', p.consume(':number'))

    def test_jump(self):
        p = Parser("wat: 7")
        p.jump(2)
        self.assertEqual('7', p.consume(':number'))

    def test_consume_false(self):
        p = Parser("wat: 7")
        self.assertEqual('wat', p.consume(':id', force_type=True))
        self.assertFalse(p.consume(':dot', force_type=True))
        self.assertEqual(':', p.consume(':colon'))
        self.assertEqual('7', p.consume(':number', force_type=True))

    def test_id_false(self):
        p = Parser("wat 6 Peter Hegemon")
        self.assertEqual('wat', p.id('wat'))
        self.assertFalse(p.id('endgame'))
        self.assertEqual('6', p.consume(':number'))
        self.assertEqual('Peter', p.id('Peter'))
        self.assertFalse(p.id('Achilles'))
    
    def test_look(self):
        p = Parser("wat 6 Peter Hegemon")
        self.assertTrue(p.look(':id'))
        self.assertEqual('wat', p.consume(':id'))
        self.assertFalse(p.look(':comparison'))
        self.assertTrue(p.look(':number'))
        self.assertTrue(p.look(':id', 1))
        self.assertFalse(p.look(':number', 1))
    
    def test_expressions(self):
        p = Parser("hi.there hi[5].! hi.there.bob")
        self.assertEqual('hi.there', p.expression())
        self.assertEqual('hi[5].!', p.expression())
        self.assertEqual('hi.there.bob', p.expression())
        
        p = Parser("567 6.0 'lol' \"wut\"")
        self.assertEqual('567', p.expression())
        self.assertEqual('6.0', p.expression())
        self.assertEqual("'lol'", p.expression())
        self.assertEqual('"wut"', p.expression())
    
    def test_ranges(self):
        p = Parser("(5..7) (1.5..9.6) (young..old) (hi[5].wat..old)")
        self.assertEqual('(5..7)', p.expression())
        self.assertEqual('(1.5..9.6)', p.expression())
        self.assertEqual('(young..old)', p.expression())
        self.assertEqual('(hi[5].wat..old)', p.expression())
    
    def test_arguments(self):
        p = Parser("filter: hi.there[5], keyarg: 7")
        self.assertEqual('filter', p.consume(':id'))
        self.assertEqual(':', p.consume(':colon'))
        self.assertEqual('hi.there[5]', p.argument())
        self.assertEqual(',', p.consume(':comma'))
        self.assertEqual('keyarg: 7', p.argument())
    
    def test_invalid_expression(self):
        self.assertRaises(SyntaxError, Parser("==").expression)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ParserTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
