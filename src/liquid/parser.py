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
from liquid.lexer import Lexer


class Parser(object):
    
    def __init__(self, string):
        self.l = Lexer(string)
        self.tokens = self.l.tokenize()
        self.pointer = 0
    
    def jump(self, point):
        self.pointer += point
        
    def consume(self, token_type=None, force_type=False):
        token = self.tokens[self.pointer]
        if force_type:
            if token[0] != token_type:
                return False
        else:
            if token_type and token[0] != token_type:
                raise SyntaxError("Expected %s but found %s" % (token_type, token[0]))
        self.pointer += 1
        return token[1]

    def id(self, string):
        token = self.tokens[self.pointer]
        if token and token[0] != ':id': return False
        if token[1] != string: return False
        self.pointer += 1
        return token[1]
    
    def look(self, token_type, ahead=0):
        token = self.tokens[self.pointer + ahead]
        if not token: return False
        if token[0] == token_type: return True
        return False 
    
    def expression(self):
        token = self.tokens[self.pointer]
        if token[0] == ':id':
            return self.variable_signature()
        elif token[0] in (':string', ':number'):
            return self.consume()
        elif token[0] == ':open_round':
            self.consume()
            first = self.expression()
            self.consume(':dotdot')
            last = self.expression()
            self.consume(':close_round')
            return "(%s..%s)" % (first, last)
        else:
            raise SyntaxError("%s is not a valid expression" % str(token))
    
    def argument(self):
        string = ""
        # might be a keyword argument (identifier: expression)
        if self.look(':id') and self.look(':colon', 1):
            string += self.consume() + self.consume() + ' '
        string += self.expression()
        return string

    def variable_signature(self):
        string = self.consume(':id')
        if self.look(':open_square'):
            string += self.consume()
            string += self.expression()
            string += self.consume(':close_square')
        if self.look(':dot'):
            string += self.consume()
            string += self.variable_signature()
        return string

#     def variable_signature
#       str = consume(:id)
#       if look(:open_square)
#         str << consume
#         str << expression
#         str << consume(:close_square)
#       end
#       if look(:dot)
#         str << consume
#         str << variable_signature
#       end
#       str
#     end
#   end