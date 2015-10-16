__author__ = 'xiangyuzhang'
import re
'''
candidate = "N88"
gateline = []
reg = r'\((N[0-9]+)\)'
X_index = 1
X_inputs = []
gates_info = []
XOR_model = "xor2 gate( .a(in_1), .b(in_2), .O(out) );"

line = "or2 gate19( .a(N87), .b(N88), .O(N298) );"
if candidate in re.findall(reg, line)[:-1]: # if target in this gate and is a input
    gateline.append(line)
    port_in_1 = "X_" + str(X_index) # create the CB
    port_in_2 = candidate + "_new" # create the new input
    port_out = candidate # make the original input output
    X_index += 1
    X_inputs.append(port_in_1)
    gates_info.append(XOR_model.replace("in_1", port_in_1).replace("in_2", port_in_2).replace("out", port_out))
    print ''
#    replaced_PIPO.remove(candidate)
'''
'''
new = []
temp = []
word = ''
with open("c7552-mux4-1-XOR-37.v", "r") as infile:
    line = infile.read().split(';')



temp= line[1].split(",")
for i in temp:
    if "new" in i:
        i = i.replace(" ", "").replace("input","").replace("\n","").replace("_new","")
        new.append(i)
temp = line[3].split(",")
for i in temp:
    if "new" in i:
        i = i.replace(" ", "").replace("output","").replace("\n","").replace("_new","")
        new.append(i)
#
#for i in new:
#    if i not in line[4]:
 #       print i + " "

with open("c7552-mux4-1-XOR-37.v", "r") as infile:
    line = infile.read()

for i in new:
    word = "(" + i + "_new)"
    if word not in line:
        print i
'''
'''
with open("Candidate") as infile:
    line = infile.read().split("\n")

temp = line[36].split()

for i in temp:
    if i not in new:
        print i + " "
for i in new:
    if i not in temp:
        print i + " "
'''
line = "buf1 gate3513( .a(N241_I), .O(N241_O) );"
reg = r'(N\w*)'
re.findall(reg, line)

print ''