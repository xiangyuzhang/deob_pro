__author__ = 'xiangyuzhang'
import re
import argparse
import os
import sys
import random

parser = argparse.ArgumentParser(usage='python Debugger.py [-h] <cam.v> <xor.v>]')
parser.add_argument('<cam.v>', help='input cam circuit that will be used as reference')
parser.add_argument('<xor.v>',  help='input xor circuit that need to verify')

args = parser.parse_args()
camIn = sys.argv[1]
xorIn = sys.argv[2]
camInPath = os.path.abspath(camIn)
xorInPath = os.path.abspath(xorIn)

reg = r'(N[0-9]+_new)'
reg_x = r'(X_[0-9]+)'
reg_net = r'(\(.*\))'
inputs = []
outputs = []
check = 0
reference = []
X_list = []
with open(camIn, "r") as infile:
    orig_line = infile.read().split(";")
for raw in range(0,len(orig_line)):
    orig_line[raw] = orig_line[raw].strip("\n")

reference = orig_line[5:-1]

with open(xorIn, "r") as infile:
    xor_line = infile.read().split(";")
for raw in range(0,len(xor_line)):
    xor_line[raw] = xor_line[raw].strip("\n")

inputs = re.findall(reg,xor_line[1])
outputs = re.findall(reg,xor_line[3])

if(str((len(inputs) + len(outputs)) )!= xorIn.replace("c7552-mux4-1-XOR-", "").replace(".v", "")):
    print "Buggy circuit, number of XOR gates mismatch\n"
    print "actual lenth is: " + str(len(inputs) + len(outputs)) + " ,which is supposed to be " + xorIn.replace("c880-mux4-1-XOR-", "").replace(".v", "") + "\n"

for i in xor_line[5:-(len(inputs) + len(outputs))-1]:
    if i not in reference:
        print "XOR: gate line mismatch: " + i.strip("\n") + "\n"
for j in reference:
    if j not in xor_line:
        print "Cam: gate line mismatch: " + j.strip("\n") + "\n"

X_list = re.findall(reg_x, xor_line[2])
if X_list[-1].strip("X_") != xorIn.replace("c7552-mux4-1-XOR-", "").replace(".v", ""):
    print "number of X CB is mismatched\n"
    print "actual number is: " + X_list[-1].strip("X_") + ", which is supposed to be " + xorIn.replace("c880-mux4-1-XOR-", "").replace(".v", "")

for i in inputs:
    if i.strip("_new") not in xor_line[4]:
        print "Buggy circuit, replaced net " + i.strip("_new") + " is not in wire\n"
    for gate in xor_line[5:-1]:
        if i in gate:
            check += 1
#            if i not in re.findall(reg_net,gate)[:-1]:
 #               print "In gate line: " + i +" input is misplaced in output\n"
            X_CB = re.findall(reg_x, gate)
            if X_CB[0]  not in xor_line[2]:
                print "In gate line: " + i + "new XOR gate's CB is not in input\n"

    if check is 0:
        print i + " is not in gates line\n"
    if check >> 2:
        print i + " shows to much in gates line\n"
    check = 0
for i in outputs:
    if i.strip("_new") not in xor_line[4]:
        print "Buggy circuit, replaced net is not in wire\n"
    for gate in xor_line[5:-1]:
        if i in gate:
            check += 1
#            if i not in re.findall(reg,gate)[-2:]:
#                print "In gate line " + i + " output is misplaced in input\n"
            X_CB = re.findall(reg_x, gate)
            if X_CB[0]  not in xor_line[2]:
                print "In gate line" + i + "new XOR gate's CB is not in input\n"

    if check is 0:
        print i + " is not in gates line\n"
    if check >> 2:
        print i + " shows to much in gates line\n"
    check = 0