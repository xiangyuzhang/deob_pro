__author__ = 'xiangyuzhang'
from networkx import nx
import re


class Graph_class:
    def __init__(self, nodelist=[], edgelist=[], node_name_list=[], vertexes=0):
        self.nodelist = nodelist
        self.edgelist = edgelist
        self.node_name_list = node_name_list
        self.nodes = vertexes


    def Add_edge(self, front_name, back_name):
        if front_name not in self.node_name_list:
            input = Wire_class(front_name)
            self.nodelist.append(input)
            self.node_name_list.append(front_name)
            self.nodes += 1
        if back_name not in self.node_name_list:
            output = Wire_class(back_name)
            self.nodelist.append(output)
            self.node_name_list.append(back_name)
            self.nodes += 1
        for i in self.nodelist:
            if i.name == front_name:
                i.back.append(back_name)
                break
        for j in self.nodelist:
            if j.name == back_name:
                j.front.append(front_name)
                break
        print ''


    def print_circuit(self, type):
        if type == "node_forward":
            for i in self.nodelist:
                print "Node: ", i.name, ":\n"
                for j in i.back:
                    print j, " "
                print "\n"

class Gate_class:  # gate actually is just an edge to connect wires
    gate_count = 0

    def __init__(self, input_list=[], output_name="empty"):
        self.input_list = input_list
        self.output_name = output_name
        gate_count = + 1


class Wire_class:
    wire_count = 0

    def __init__(self, name, front=[], back=[]):
        self.name = name
        self.back = back
        self.front = front
        Wire_class.wire_count += 1


def gate_scaner(gate_info_string, circuit):
    gate_info = parser(gate_info_string)
    input_list = gate_info[0:-1]  # input and output here is just string
    output = gate_info[-1]
    for input in input_list:
        circuit.Add_edge(input, output)




def parser(gate_info_string):
    return_list = []
    temp_list = re.findall(r'(\(\w*\))', gate_info_string)
    for i in temp_list:
        if '(' in i or ')' in i:
            return_list.append(i.strip('(').strip(')'))
    return return_list

circuit = Graph_class()
with open("c432-abcmap-fmt-WIRE-2-original.v", "r") as infile:
    Vline = infile.read().split(";")

for line in Vline:
    line = line.strip("\n")
    if line != '' and '/' not in 'module' not in line and 'input' not in line and 'output' not in line and 'wire' not in line and 'endmodule' not in line:
        gate_scaner(line,circuit)

circuit.print_circuit("node_forward")