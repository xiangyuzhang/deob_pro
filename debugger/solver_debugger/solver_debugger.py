__author__ = 'parallels'
## This script will process cnf file from incre and nonincre is there is index shift based on shift index and original document
from decimal import Decimal


def shift_index(line, offset):
    origin_container = line.split(" ")
    result_container = []
    for i in origin_container[:-1]:
#        print Decimal(i.strip("-")) - offset
        if Decimal(i.strip("-")) > offset:
            if "-" in i:
                temp = ("-" + str((Decimal(i.strip("-")) - offset)) + " ")
            else:
                temp = (str((Decimal(i.strip("-")) - offset)) + " ")
        else:
            if "-" in i:
                temp = ("-" + str((Decimal(i.strip("-")))) + " ")
            else:
                temp = (str((Decimal(i.strip("-")))) + " ")
        result_container.append(temp)
    result_container.append("0")
    return  result_container


incre_cnf = []
incre_cnf_processed = []
nonincre_cnf = []
with open("incre_cnf_essential_difference.cnf",'r') as infile:
    incre_cnf = infile.read().split("\n")
for line in incre_cnf:
    if "c" in line:
        continue
    else:
        incre_cnf_processed.append(("").join(shift_index(line, 196)))

outxt = ('\n').join(incre_cnf_processed)
with open("new_file", "w") as outfile:
    outfile.write(outxt)