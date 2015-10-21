__author__ = 'xiangyuzhang'
from subprocess import call
from EC_lib import EC
import os
# first, get runtime about original camouflage

cam_list = [
"c432-mux4-1.v",
"c432-mux4-11.v",
"c432-mux4-21.v",
"c432-mux4-31.v",
"c432-mux4-41.v",
"c432-mux4-51.v",
"c432-mux4-61.v",
"c432-mux4-71.v",
"c432-mux4-81.v",
"c432-mux4-91.v",
"c432-mux4-101.v"
  ]

with open("time_info_original", "a") as outfile:
    outfile.write("#Number of gate                  #BASE\n")


# run simp and it will generate the finalsolu and iterationinfo

for i in cam_list:
    cmmd = "/usr/bin/time -v -o temp-time ./minisat-incre-simp decam-incre c432-abcmap-fmt.v " + i
    call(cmmd, shell = True)
# rename iterationinfo
    os.rename("increIterationInfo.log", i.strip(".v") + "-interationInfo.dat")

# check EC and import to a txt

    res = EC("c432-abcmap-fmt.v", i, "finalSolu.log")
    if (res == 1):
        content = "Circuit: " + i + " is CORRECT!\n"
    elif (res == 0):
        content = "Circuit: " + i + " is WRONG!\n"
    else:
        content = "Circuit: " + i + " is BUG!\n"
    with open("EC_result.txt", "a") as output:
        output.write(content)

    with open("time_info_original", "a") as outfile:
        outfile.write(i.strip("c432-mux4-").strip(".v") + "                    ")
    with open("temp-time", "r") as infile:
        timeline = infile.read().split("\n")

    for line in timeline:
        if "User time (seconds):" in line:
            time_info = line.replace("User time (seconds):", "")
            break

    with open("time_info_original", "a") as outfile:
        outfile.write(time_info + "\n")
    os.remove("temp-time")
# second, get runtime about original camouflage

with open("time_info_XOR", "a") as outfile:
    outfile.write("#Number of gate                  #BASE\n")

for j in range(1, 44):         #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!need change if use other circuit
    i = "c432-mux4-1-XOR-" + str(j) + ".v"
# create file

    make_cmmd = " python ./XOR_Cam_randmom.py c432-mux4-1.v " + str(j)
    call(make_cmmd , shell = True)

    cmmd = "/usr/bin/time -v -o temp-time ./minisat-incre-simp decam-incre c432-abcmap-fmt.v " + i
    call(cmmd, shell = True)
# rename iterationinfo
    os.rename("increIterationInfo.log", i.strip(".v") + "-interationInfo.dat")

# check EC and import to a txt

    res = EC("c432-abcmap-fmt.v", i, "finalSolu.log")
    if (res == 1):
        content = "Circuit: " + i + " is CORRECT!\n"
    elif (res == 0):
        content = "Circuit: " + i + " is WRONG!\n"
    else:
        content = "Circuit: " + i + " is BUG!\n"
    with open("EC_result.txt", "a") as output:
        output.write(content)

    with open("time_info_XOR", "a") as outfile:
        outfile.write(i.strip("c432-mux4-1-XOR").strip(".v") + "                    ")
    with open("temp-time", "r") as infile:
        timeline = infile.read().split("\n")

    for line in timeline:
        if "User time (seconds):" in line:
            time_info = line.replace("User time (seconds):", "")
            break

    with open("time_info_XOR", "a") as outfile:
        outfile.write(time_info + "\n")
    os.remove("temp-time")