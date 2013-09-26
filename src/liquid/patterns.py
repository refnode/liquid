# Copyright 2011, refnode http://refnode.com
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


FilterSeparator             = "\|"
ArgumentSeparator           = ','
FilterArgumentSeparator     = ':'
VariableAttributeSeparator  = '.'
TagStart                    = "\{\%"
TagEnd                      = "\%\}"
VariableSignature           = "\(?[\w\-\.\[\]]\)?"
VariableSegment             = "[\w\-]"
VariableStart               = "\{\{"
VariableEnd                 = "\}\}"
VariableIncompleteEnd       = "\}\}?"
QuotedString                = "\"[^\"]*\"|'[^']*'"
QuotedFragment              = "%s|(?:[^\s,\|'\"]|%s)+" % (QuotedString, QuotedString)
StrictQuotedFragment        = "\"[^\"]+\"|'[^']+'|[^\s|:,]+"
FirstFilterArgument         = "%s(?:%s)" % (FilterArgumentSeparator, StrictQuotedFragment)
OtherFilterArgument         = "%s(?:%s)" % (ArgumentSeparator, StrictQuotedFragment)
SpacelessFilter             = "^(?:'[^']+'|\"[^\"]+\"|[^'\"])*%s(?:%s)(?:%s(?:%s)*)?" % (FilterSeparator, StrictQuotedFragment, FirstFilterArgument, OtherFilterArgument)
Expression                  = "(?:%s(?:%s)*)" % (QuotedFragment, SpacelessFilter)
TagAttributes               = "(\w+)\s*\:\s*(%s)" % (QuotedFragment)
AnyStartingTag              = "\{\{|\{\%"
PartialTemplateParser       = "%s.*?%s|%s.*?%s" % (TagStart, TagEnd, VariableStart, VariableIncompleteEnd)
TemplateParser              = "(%s|%s)" % (PartialTemplateParser, AnyStartingTag)
VariableParser              = "\[[^\]]+\]|%s+\??" % (VariableSegment)

