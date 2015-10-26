__author__ = 'xiangyuzhang'

import re
import argparse
import os
import sys
import random

parser = argparse.ArgumentParser(usage='python XOR_Cam.py [-h] <cam.v> [number]]', description='This program will use '
                                                                                               'cam.v to generate a evener '
                                                                                               'harder circuit.', )
parser.add_argument('<cam.v>', help='input cam circuit that will be made harder')
parser.add_argument('number', action='store', type=int, help='define the specific number of gates for both input and '
                                                              'output to re-camouflage')

args = parser.parse_args()
Num_XOR = args.number
camIn = sys.argv[1]
camInPath = os.path.abspath(camIn)

if not os.path.isfile(camInPath):
    print 'Invalid cam circuit file!!!!\n'

Camfile = camInPath


varIndex = 1
posIndex = []  # store integer indexes of pos to return
X_index = 1  # used to designate the index for XOR input
reg = r'(N\w*)'
port_in_1 = ""
port_in_2 = ""
port_out = ""
XOR_model = "xor2 gate( .a(in_1), .b(in_2), .O(out) );"
content = []  # contain the refreshed codes
inputs = []
inputs_copy = []
new_inputs = []  # used to contain the replaced inputs
outputs = []
outputs_copy = []
new_outputs = []  # used to contain the replaced outputs
new_gates = []  # used to contain the new xor gated
X_inputs = []  # used to store the new input

target_PIPO = []  # here I will store all the original gate_ame about PIPO
random.random()
# random.seed(1)
random_sequence = []  # this is the list store the srand sequence
random_couter = 0
PI_info = ""  # updated input[0] will be stored here
PO_info = "" # updated output will be stored here
wire_info = "" # updated wire will be stored here
gates_info = [] # updated gates will be stored here
XOR_info = [] # updade XOR will be stored here
replaced_PIPO = [] # store the removed PIPO (removed by _new)
CB = ""
gateline = [] # store Vlines[5:-2]

with open(Camfile, 'r') as infile:
    inV = infile.read()
    Vlines = inV.split(';\n')
# here I collect the inputs and outputs
for line in Vlines:
    line = line.replace('\n', '')
    if 'input' in line and '//' not in line:
        PIs = re.search(r'(?<=input )(.*)(?=$)', line).group().replace(' ', '').split(',')
        tmpPis = []
        for pi in PIs:
            pi = pi.replace('\\', '').replace('[', '').replace(']', '')
            tmpPis.append(pi)
        inputs.append(tmpPis)

    elif 'output' in line and '//' not in line:
        POs = re.search(r'(?<=output )(.*)(?=$)', line).group().replace(' ', '').split(',')
        tmpPos = []
        for po in POs:
            po = po.replace('\\', '').replace('[', '').replace(']', '')
            outputs.append(po)
target_PIPO.extend(inputs[0])
target_PIPO.extend(outputs)

# here I generate the random sequence
while random_couter < Num_XOR:
    temp = random.randint(0, len(target_PIPO)-1)
    if temp not in random_sequence:
        random_sequence.append(temp)
        random_couter += 1


# PI_info is the updated inputs[0] PO_info is the updated output


with open(Camfile, 'r') as infile:
    inV = infile.read()
    Vlines = inV.split(';\n')
for line in Vlines:
    if 'input' in line and '//' not in line:
        line += ','
        for i in random_sequence:
            line = line.replace(target_PIPO[i]+",", target_PIPO[i]+"_new,")
            PI_info = line
            if target_PIPO[i] not in replaced_PIPO:
                replaced_PIPO.append(target_PIPO[i])
        break


for line in Vlines:
    if 'output' in line and '//' not in line:
        line += ','
        for i in random_sequence:
            line = line.replace(target_PIPO[i]+",", target_PIPO[i]+"_new,")
            PO_info = line
            if target_PIPO[i] not in replaced_PIPO:
                replaced_PIPO.append(target_PIPO[i])

for line in Vlines:
    if 'wire' in line and '//' not in line:     # wire_info is like wire N12, N224, N422,
        line = line.strip(";")
        for old_PIPO in replaced_PIPO:
            line = line +  ',' + old_PIPO
        wire_info = line + ";"

for i in replaced_PIPO:
    with open("Candidate", "a") as outfile:
        outfile.write(i + " ")
with open("Candidate", "a") as outfile:
    outfile.write("\n")
# from the following block I collect all the XOR gates
with open(Camfile, 'r') as infile:
    inV = infile.read()
    Vlines = inV.replace('\n', '').split(';')
for line in Vlines:
    line = line.replace('\n', '')
    if line != '' and line[0] != '/' and not 'module' in line and not 'output' in line and not 'input' in line and not 'wire' in line:
        for candidate in replaced_PIPO: # find a gate
            if candidate in re.findall(reg, line)[:-1]: # if target in this gate and is a input

                gateline.append(line)
                port_in_1 = "X_" + str(X_index) # create the CB
                port_in_2 = candidate + "_new" # create the new input
                port_out = candidate # make the original input output
                X_index += 1
                X_inputs.append(port_in_1)
                gates_info.append(XOR_model.replace("in_1", port_in_1).replace("in_2", port_in_2).replace("out", port_out))
                temp = replaced_PIPO.index(candidate)
                replaced_PIPO[temp] = "NULL"
            elif candidate in re.findall(reg, line)[-2:]: # if target in this gate and is a output

                gateline.append(line)
                port_in_1 = "X_" + str(X_index) # create the new CB
                port_in_2 = candidate # make the output input
                port_out = candidate + "_new" # create the new output
                X_index += 1
                X_inputs.append(port_in_1)
                gates_info.append(XOR_model.replace("in_1", port_in_1).replace("in_2", port_in_2).replace("out", port_out))
                temp = replaced_PIPO.index(candidate)
                replaced_PIPO[temp] = "NULL"
                # print len(inputs[0])




with open(Camfile, 'r') as infile:
    inV = infile.read()
    Vlines = inV.replace('\n', '').split(';')

if (len(PI_info) == 0):
    PI_info = Vlines[1]
if (len(PO_info) == 0):
    PO_info = Vlines[3]

Vlines[2] = Vlines[2].strip(";")
CB = Vlines[2]
for X in range(1, X_index):
    CB = CB + ',' + 'X_' + str(X)
CB+=';'
PI_info = PI_info[:-1]
PO_info = PO_info[:-1]
content.append(Vlines[0] + ";\n\n")
content.append(PI_info + ";\n\n")
content.append(CB + "\n\n")
content.append(PO_info + ";\n\n")
content.append(wire_info + "\n\n")
for i in Vlines[5:-1]:
    content.append(i + ";\n")

for i in gates_info:
    if ';' in i:
        content.append(i +  "\n")
    else:
        content.append(i +  ";\n")
content.append("\nendmodule")



for i in content:
    with open(Camfile.replace(".v", "-XOR-" + str(Num_XOR) + ".v"), "a") as outfile:
        outfile.write(i)
print ""
#    if line != '' and line[0] != '/' and not 'module' in line and not 'output' in line and not 'input' in line and not 'wire' in line:

