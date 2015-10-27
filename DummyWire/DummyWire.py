__author__ = 'xiangyuzhang'
import argparse
import sys
import os
import re
import random
from wire_CircuitScanner import CircuitScanner


def abcmap_MUX_OBF_netlist(pi1, pi2, pi3, pi4, output, seed, programbit):
    D_bit1 = 'D_' + str(programbit)
    D_bit2 = 'D_' + str(programbit + 1)
    D_bit1_not = 'D_' + str(programbit) + "_NOT"
    D_bit2_not = 'D_' + str(programbit + 1) + "_NOT"
    new_netlist = []
    wire = []
    CB = []
    result = []
    new_netlist.append("inv1 gate( .a(" + D_bit1 + "),.O(" +  D_bit1_not + ") );\n")
    new_netlist.append("inv1 gate( .a(" + D_bit2 + "),.O(" +  D_bit2_not + ") );\n")
    new_netlist.append("and2 gate( .a(" + pi1 + "), .b(" + D_bit1_not + "), .O(" + "ED_" + str(seed) + ") );\n")
    new_netlist.append("and2 gate( .a(" + pi2 + "), .b(" + D_bit1 + "), .O(" + "ED_" + str(seed + 1) + ") );\n")
    new_netlist.append("and2 gate( .a(" + pi3 + "), .b(" + D_bit1_not + "), .O(" + "ED_" + str(seed + 2) + ") );\n")
    new_netlist.append("and2 gate( .a(" + pi4 + "), .b(" + D_bit1 + "), .O(" + "ED_" + str(seed + 3) + ") );\n")
    new_netlist.append("and2 gate( .a(" + "ED_" + str(seed) + "), .b(" + D_bit2_not + "), .O(" + "ED_" + str(seed + 4) + ") );\n")
    new_netlist.append("and2 gate( .a(" + "ED_" + str(seed + 1) + "), .b(" + D_bit2 + "), .O(" + "ED_" + str(seed + 5) + ") );\n")
    new_netlist.append("and2 gate( .a(" + "ED_" + str(seed + 2) + "), .b(" + D_bit2_not + "), .O(" + "ED_" + str(seed + 6) + ") );\n")
    new_netlist.append("and2 gate( .a(" + "ED_" + str(seed + 3) + "), .b(" + D_bit2 + "), .O(" + "ED_" + str(seed + 7) + ") );\n")
    new_netlist.append("or2  gate( .a(" +  "ED_" + str(seed + 4) + "), .b(" + "ED_" + str(seed + 5) +"), .O(" + "ED_" + str(seed + 8) +") );\n")
    new_netlist.append("or2  gate( .a(" +  "ED_" + str(seed + 6) + "), .b(" + "ED_" + str(seed + 8) +"), .O(" + "ED_" + str(seed + 9) +") );\n")
    new_netlist.append("or2  gate( .a(" +  "ED_" + str(seed + 9) + "), .b(" + "ED_" + str(seed + 7) +"), .O(" + str(output) +") );\n")

    wire.append(D_bit1_not).append(D_bit2_not)
    for i in range(0,10):
        wire.append("ED_" + str(seed + i))
    CB.append(D_bit1).append(D_bit2)
    result.append(new_netlist).append(wire).append(CB).append(output)
    return result
# seed is the initial index for wires
# program bit is the initial index for CBs
# return [wire, CB, netlist, output]


def find_backup_Mux_in(circuitIn):
    result = []
    with open(circuitIn, 'r') as infile:
        inV = infile.read()
        Vlines = inV.replace('\r','').replace(';\n')

    for line in Vlines:
        line = line.replace('\n', '')
        if 'input' in line:
            PIs=re.search(r'(?<=input )(.*)(?=$)', line).group().replace(' ','').split(',')
            for pi in PIs:
                pi = pi.replace('\\','').replace('[','').replace(']','')
                result.append(pi)
    return result
#   return list result['N12','N23','N1234','N6723']


def random_sequence_generator(limit_num, select_range):

    random_counter = 1
    random.random()
    random_sequence = []
    while random_counter < limit_num:
        temp = random.randint(0, select_range-1)
    if temp not in random_sequence:
        random_sequence.append(temp)
        random_counter += 1

    return random_sequence
# limit_num is the length of random_sequence
# select_range is the range of int can be selected
# return list; random_sequence[1,23,55, ...]


def camouflage_builder(target_pair, back_up_MUX_in, seed, programbit, output):
    this_gate_in_net = []
    this_gate_out_net = []
    wire = []   # contain extra wire
    random_sequence = []
    CB = []     # contain extra CB
    netlist = []

    this_gate_in_net = target_pair.in_netName
    this_gate_out_net = target_pair.out_netName
    if len(target_pair.in_netName) >= 4:
        result = abcmap_MUX_OBF_netlist(this_gate_in_net[0], this_gate_in_net[1], this_gate_in_net[2], this_gate_out_net, output, seed, programbit)
    else:
        random_sequence = random_sequence_generator((4 - len(this_gate_in_net)), len(back_up_MUX_in))
        if len(this_gate_in_net) is 1:
            result = abcmap_MUX_OBF_netlist(this_gate_in_net[0], back_up_MUX_in(random_sequence[0]), back_up_MUX_in(random_sequence[1]),this_gate_out_net, output, seed, programbit)
        if len(this_gate_in_net) is 2:
            result = abcmap_MUX_OBF_netlist(this_gate_in_net[0], this_gate_in_net[1], back_up_MUX_in(random_sequence[1]),this_gate_out_net, output, seed, programbit)
        if len(this_gate_in_net) is 3:
            result = abcmap_MUX_OBF_netlist(this_gate_in_net[0], this_gate_in_net[1], this_gate_in_net[2],this_gate_out_net, output, seed, programbit)

    return result

print abcmap_MUX_OBF_netlist("N1", "N2", "N3", "N4", "Output", 0, 1)

pair_list = []  # used to store the random selected gate pair
back_up_MUX_in = []
seed = 0
programbit = 0
MUX_O_index = 0
new_netlist = []    # used to contain MUX
# parser
parser = argparse.ArgumentParser(usage='python DummyWire.py [-h]  <circuit.v> [number]]', description='This program will camouflage <circuit.v> with dummy wire',)
parser.add_argument('<circuit.v>', help='input circuit to be camouflaged')
parser.add_argument('number', action='store', type=int, help='define the maximum number of gates to be selected, trade off between time and difficulty')
args = parser.parse_args()
Num_pair = args.number
circuitIn = sys.argv[1]
CircuitPath = os.path.abspath(circuitIn)

if not os.path.isfile(CircuitPath):
    print 'Invalid input circuit file!!!\n'
# pair_list generator
pair_list= CircuitScanner(CircuitPath, Num_pair)
# get back up MUX_in
back_up_MUX_in = find_backup_Mux_in(circuitIn)
# MUX builder
for target_pair in pair_list:
    new_netlist = camouflage_builder(target_pair, back_up_MUX_in, seed, programbit, 'MUX_O_' + MUX_O_index)
    seed += 10
    programbit += 2
    MUX_O_index += 1

# content builder

# circuit generator
