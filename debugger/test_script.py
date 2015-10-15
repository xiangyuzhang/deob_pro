__author__ = 'xiangyuzhang'

from subprocess import call
import os
import sys
import argparse
parser = argparse.ArgumentParser(usage='python test_script [-h] <orac.v> <cam.v> [number]]', description='This program is used to chect the previous buggy circuit', )
parser.add_argument('<orac.v>', help = 'the oracle circuit')
parser.add_argument('<cam.v>', help='the cam circuit')
parser.add_argument('number', action='store', type=int, help='define which specific line applied in candidate list')

args = parser.parse_args()
Num_XOR = args.number
oraIn = sys.argv[1]
camIn = sys.argv[2]
camInPath = os.path.abspath(camIn)
oraInPath = os.path.abspath(oraIn)
creat_cmmd = "python Candidate_apply.py " + camIn + " Candidate " + str(Num_XOR)
call(creat_cmmd, shell = True)
target = camInPath.strip('.v')
target += "-XOR-" + str(Num_XOR) + '.v'
EC_cmmd = "python decam-v5-cmmdline.py " + oraInPath + " " + target
call(EC_cmmd, shell = True)