__author__ = 'xiangyuzhang'

import re


Camfile = "c432-mux4-1.v"
varIndexDict = {}
varIndex = 1
posIndex = []  # store integer indexes of pos to return
X_index = 1  # used to designate the index for XOR input
reg = r'\((N[0-9]+)\)'
# find a good model
port_in_1 = ""
port_in_2 = ""
port_out = ""
XOR_model = "xor2 gate( .a(in_1), .b(in_2), .O(out) );"

# find the first line of input and the output, and store in containers

inputs = []
new_inputs = []  #  used to contain the replaced inputs
outputs = []
new_outputs = []  # used to contain the replaced outputs
new_gates = []  # used to contain the new xor gated
with open(Camfile, 'r') as infile:
    inV = infile.read()
    Vlines = inV.split(';\n')

for line in Vlines:
    line = line.replace('\n', '')
    if 'input' in line and not '//' in line:
        PIs = re.search(r'(?<=input )(.*)(?=$)', line).group().replace(' ', '').split(',')
        tmpPis = []
        for pi in PIs:
            pi = pi.replace('\\', '').replace('[', '').replace(']', '')
            tmpPis.append(pi)
        inputs.append(tmpPis)

    elif 'output' in line and not '//' in line:
        POs = re.search(r'(?<=output )(.*)(?=$)', line).group().replace(' ', '').split(',')
        tmpPos = []
        for po in POs:
            po = po.replace('\\', '').replace('[', '').replace(']', '')
            outputs.append(po)

# change the gate verilog file only
with open(Camfile, 'r') as infile:
    inV = infile.read()
    Vlines = inV.split(';\n')

for line in Vlines:
    line = line.replace('\n', '')
    if line!='' and line[0]!='/' and not 'module' in line and not 'output' in line and not 'input' in line and not 'wire' in line:
        for out in outputs:
            if out in re.findall(reg, line):
                port_in_1 = "X_" + str(X_index)
                port_in_2 = out
                port_out = out + "_new"
                X_index += 1
                if port_out  not in new_outputs:
                    new_outputs.append(port_out)
                new_gates.append(XOR_model.replace("in_1", port_in_1).replace("in_2", port_in_2).replace("out", port_out))
        for ins in inputs[0]:
            if ins in re.findall(reg, line):
                port_in_1 = "X_" + str(X_index)
                port_in_2 = ins + "_new"
                port_out = ins
                X_index += 1
                if port_in_2 not in new_inputs:
                    new_inputs.append(port_in_2)
                new_gates.append(XOR_model.replace("in_1", port_in_1).replace("in_2", port_in_2).replace("out", port_out))

print new_gates

# -> replace the output/input name in  zone
# -> add new gates
