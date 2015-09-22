__author__ = 'xiangyuzhang'

import re
string = 'and9 gate46( .a(N254), .b(N159), .c(N162), .d(N165), .e(N168), .f(N171), .g(N174), .h(N177), .i(N180), .O(N199) );'


reg = r'\((N[0-9]+)\)'
arr = re.findall(reg, string)
print arr