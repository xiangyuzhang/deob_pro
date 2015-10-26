__author__ = 'xiangyuzhang'
import argparse
import sys
import os
from wire_CircuitScanner import CircuitScanner


pair_list = []  # used to store the random selected gate pair
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
# gate modifier

# content builder

# circuit generator
