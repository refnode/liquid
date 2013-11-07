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


# import stdlibs
# import thirdparty libs
# import local libs
from liquid.strscan import Scanner


class Lexer(object):
    
    SPECIALS = {
        '|': ':pipe',
        '.': ':dot',
        ':': ':colon',
        ',': ':comma',
        '[': ':open_square',
        ']': ':close_square',
        '(': ':open_round',
        ')': ':close_round'
    }
    
    PATTERNS = (
        ('COMPARISON_OPERATOR', '==|!=|<>|<=?|>=?|contains', ':comparison'),
        ('SINGLE_STRING_LITERAL', "'[^\']*'", ':string'),
        ('DOUBLE_STRING_LITERAL', '"[^\"]*"', ':string'),
        ('NUMBER_LITERAL', '-?\d+(\.\d+)?', ':number'),
        ('IDENTIFIER', '[\w\-?!]+', ':id'),
        ('DOTDOT', '\.\.', ':dotdot')
    )
    
    def __init__(self, input):
        self.s = Scanner(input)
    
    def tokenize(self):
        output = []
        s = self.s
        while not s.eos():
            s.skip('\s*')
            if s.eos():
                break
            token = None
            for key, pattern, id in Lexer.PATTERNS:
                t = s.scan(pattern) 
                if t:
                    token = [id, t]
                    break
            if token is None:
                char = s.getch()
                id = Lexer.SPECIALS.get(char)
                if not id:
                    raise SyntaxError("Unexpected character %s" % char)
                token = [id, char]
            output.append(token)
        output.append([':end_of_string'])
        return output
