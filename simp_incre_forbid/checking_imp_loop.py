__author__ = 'xiangyuzhang'
from subprocess import call
from EC_lib import  EC
import os

'''
cam_list = [
"c7552-mux4-1.v",
"c7552-mux4-1-XOR.v",
"c7552-mux4-11.v",
"c7552-mux4-11-XOR.v",
"c7552-mux4-21.v",
"c7552-mux4-21-XOR.v",
"c7552-mux4-31.v",
"c7552-mux4-31-XOR.v",
"c7552-mux4-41.v",
"c7552-mux4-41-XOR.v",
"c7552-mux4-51.v",
"c7552-mux4-51-XOR.v",
"c7552-mux4-61.v",
"c7552-mux4-61-XOR.v",
"c7552-mux4-71.v",
"c7552-mux4-71-XOR.v",
"c7552-mux4-81.v",
"c7552-mux4-81-XOR.v",
"c7552-mux4-91.v",
"c7552-mux4-91-XOR.v",
"c7552-mux4-101.v",
"c7552-mux4-101-XOR.v",
"c7552-mux4-111.v",
"c7552-mux4-111-XOR.v",
"c7552-mux4-121.v",
"c7552-mux4-121-XOR.v",
"c7552-mux4-131.v",
"c7552-mux4-131-XOR.v",
"c7552-mux4-141.v",
"c7552-mux4-141-XOR.v",
"c7552-mux4-151.v",
"c7552-mux4-151-XOR.v",
"c7552-mux4-161.v",
"c7552-mux4-161-XOR.v",
"c7552-mux4-171.v",
"c7552-mux4-171-XOR.v",
"c7552-mux4-181.v",
"c7552-mux4-181-XOR.v",
"c7552-mux4-191.v",
"c7552-mux4-191-XOR.v",
"c7552-mux4-201.v",
"c7552-mux4-201-XOR.v"
    ]

with open("time_info", "a") as outfile:
    outfile.write("#Number of gate                  #BASE                 #XOR\n")

# run simp and it will generate the finalsolu and iterationinfo
for i in cam_list:
    cmmd = "/usr/bin/time -v -o temp-time ./minisat-incre-simp decam-incre c7552-abcmap-fmt.v " + i
    call(cmmd, shell = True)
# rename iterationinfo
    os.rename("increIterationInfo.log", i.strip(".v") + "-interationInfo.dat")

# check EC and import to a txt

    res = EC("c7552-abcmap-fmt.v", i, "finalSolu.log")
    if (res == 1):
        content = "Circuit: " + i + " is CORRECT!\n"
    elif (res == 0):
        content = "Circuit: " + i + " is WRONG!\n"
    else:
        content = "Circuit: " + i + " is BUG!\n"
    with open("EC_result.txt", "a") as output:
        output.write(content)


    with open("temp-time", "r") as infile:
        timeline = infile.read().split("\n")
    if "XOR" not in i:
        with open("time_info", "a") as outfile:
            outfile.write(i.strip("c7552-mux4-").strip(".v") + "                 ")
        for line in timeline:
                if "User time (seconds):" in line:
                    time_info = line.replace("User time (seconds):", "")
                    break

        with open("time_info", "a") as outfile:
            outfile.write(time_info + "                 ")
    else:
        for line in timeline:
            if "User time (seconds):" in line:
                time_info = line.replace("User time (seconds):", "")
                break

        with open("time_info", "a") as outfile:
            outfile.write(time_info + "\n")
    os.remove("temp-time")

'''

'''
cam_list = [
"c5315-mux4-1.v",
"c5315-mux4-1-XOR.v",
"c5315-mux4-11.v",
"c5315-mux4-11-XOR.v",
"c5315-mux4-21.v",
"c5315-mux4-21-XOR.v",
"c5315-mux4-31.v",
"c5315-mux4-31-XOR.v",
"c5315-mux4-41.v",
"c5315-mux4-41-XOR.v",
"c5315-mux4-51.v",
"c5315-mux4-51-XOR.v",
"c5315-mux4-61.v",
"c5315-mux4-61-XOR.v",
"c5315-mux4-71.v",
"c5315-mux4-71-XOR.v",
"c5315-mux4-81.v",
"c5315-mux4-81-XOR.v",
"c5315-mux4-91.v",
"c5315-mux4-91-XOR.v",
"c5315-mux4-101.v",
"c5315-mux4-101-XOR.v",
"c5315-mux4-111.v",
"c5315-mux4-111-XOR.v",
"c5315-mux4-121.v",
"c5315-mux4-121-XOR.v",
"c5315-mux4-131.v",
"c5315-mux4-131-XOR.v",
"c5315-mux4-141.v",
"c5315-mux4-141-XOR.v",
"c5315-mux4-151.v",
"c5315-mux4-151-XOR.v",
"c5315-mux4-161.v",
"c5315-mux4-161-XOR.v",
"c5315-mux4-171.v",
"c5315-mux4-171-XOR.v",
"c5315-mux4-181.v",
"c5315-mux4-181-XOR.v",
"c5315-mux4-191.v",
"c5315-mux4-191-XOR.v",
"c5315-mux4-201.v",
"c5315-mux4-201-XOR.v"
    ]

with open("time_info_5315", "a") as outfile:
    outfile.write("#Number of gate                  #BASE                 #XOR\n")

# run simp and it will generate the finalsolu and iterationinfo
for i in cam_list:
    cmmd = "/usr/bin/time -v -o temp-time ./minisat-incre-simp decam-incre c5315-abcmap-fmt.v " + i
    call(cmmd, shell = True)
# rename iterationinfo
    os.rename("increIterationInfo.log", i.strip(".v") + "-interationInfo.dat")

# check EC and import to a txt

    res = EC("c5315-abcmap-fmt.v", i, "finalSolu.log")
    if (res == 1):
        content = "Circuit: " + i + " is CORRECT!\n"
    elif (res == 0):
        content = "Circuit: " + i + " is WRONG!\n"
        break
    else:
        content = "Circuit: " + i + " is BUG!\n"
        break
    with open("EC_result.txt", "a") as output:
        output.write(content)


    with open("temp-time", "r") as infile:
        timeline = infile.read().split("\n")
    if "XOR" not in i:
        with open("time_info_5315", "a") as outfile:
            outfile.write(i.strip("c5315-mux4-").strip(".v") + "              ")
        for line in timeline:
                if "User time (seconds):" in line:
                    time_info = line.replace("User time (seconds):", "")
                    break

        with open("time_info_5315", "a") as outfile:
            outfile.write(time_info + "              ")
    else:
        for line in timeline:
            if "User time (seconds):" in line:
                time_info = line.replace("User time (seconds):", "")
                break

        with open("time_info_5315", "a") as outfile:
            outfile.write(time_info + "\n")
    os.remove("temp-time")


'''
'''
cam_list = [
"c3540-mux4-1.v",
"c3540-mux4-1-XOR.v",
"c3540-mux4-11.v",
"c3540-mux4-11-XOR.v",
"c3540-mux4-21.v",
"c3540-mux4-21-XOR.v",
"c3540-mux4-31.v",
"c3540-mux4-31-XOR.v",
"c3540-mux4-41.v",
"c3540-mux4-41-XOR.v",
"c3540-mux4-51.v",
"c3540-mux4-51-XOR.v",
"c3540-mux4-61.v",
"c3540-mux4-61-XOR.v",
"c3540-mux4-71.v",
"c3540-mux4-71-XOR.v",
"c3540-mux4-81.v",
"c3540-mux4-81-XOR.v",
"c3540-mux4-91.v",
"c3540-mux4-91-XOR.v",
"c3540-mux4-101.v",
"c3540-mux4-101-XOR.v",
"c3540-mux4-111.v",
"c3540-mux4-111-XOR.v",
"c3540-mux4-121.v",
"c3540-mux4-121-XOR.v",
"c3540-mux4-131.v",
"c3540-mux4-131-XOR.v",
"c3540-mux4-141.v",
"c3540-mux4-141-XOR.v",
"c3540-mux4-151.v",
"c3540-mux4-151-XOR.v",
"c3540-mux4-161.v",
"c3540-mux4-161-XOR.v",
"c3540-mux4-171.v",
"c3540-mux4-171-XOR.v",
"c3540-mux4-181.v",
"c3540-mux4-181-XOR.v",
"c3540-mux4-191.v",
"c3540-mux4-191-XOR.v",
"c3540-mux4-201.v",
"c3540-mux4-201-XOR.v"
    ]

with open("time_info_3540", "a") as outfile:
    outfile.write("#Number of gate                  #BASE                 #XOR\n")

# run simp and it will generate the finalsolu and iterationinfo
for i in cam_list:
    cmmd = "/usr/bin/time -v -o temp-time ./minisat-incre-simp decam-incre c3540-abcmap-fmt.v " + i
    call(cmmd, shell = True)
# rename iterationinfo
    os.rename("increIterationInfo.log", i.strip(".v") + "-interationInfo.dat")

# check EC and import to a txt

    res = EC("c3540-abcmap-fmt.v", i, "finalSolu.log")
    if (res == 1):
        content = "Circuit: " + i + " is CORRECT!\n"
    elif (res == 0):
        content = "Circuit: " + i + " is WRONG!\n"
        break
    else:
        content = "Circuit: " + i + " is BUG!\n"
        break
    with open("EC_result.txt", "a") as output:
        output.write(content)


    with open("temp-time", "r") as infile:
        timeline = infile.read().split("\n")
    if "XOR" not in i:
        with open("time_info_3540", "a") as outfile:
            outfile.write(i.strip("c3540-mux4-").strip(".v") + "              ")
        for line in timeline:
                if "User time (seconds):" in line:
                    time_info = line.replace("User time (seconds):", "")
                    break

        with open("time_info_3540", "a") as outfile:
            outfile.write(time_info + "              ")
    else:
        for line in timeline:
            if "User time (seconds):" in line:
                time_info = line.replace("User time (seconds):", "")
                break

        with open("time_info_3540", "a") as outfile:
            outfile.write(time_info + "\n")
    os.remove("temp-time")
'''

cam_list = [
#"c1908-mux4-1.v",
#"c1908-mux4-1-XOR.v",
#"c1908-mux4-11.v",
#"c1908-mux4-11-XOR.v",
#"c1908-mux4-21.v",
#"c1908-mux4-21-XOR.v",
#"c1908-mux4-31.v",
#"c1908-mux4-31-XOR.v",
#"c1908-mux4-41.v",
#"c1908-mux4-41-XOR.v",
#"c1908-mux4-51.v",
#"c1908-mux4-51-XOR.v",
#"c1908-mux4-61.v",
#"c1908-mux4-61-XOR.v",
#"c1908-mux4-71.v",
#"c1908-mux4-71-XOR.v",
#"c1908-mux4-81.v",
#"c1908-mux4-81-XOR.v",
"c1908-mux4-91.v",
"c1908-mux4-91-XOR.v",
"c1908-mux4-101.v",
"c1908-mux4-101-XOR.v",
"c1908-mux4-111.v",
"c1908-mux4-111-XOR.v",
"c1908-mux4-121.v",
"c1908-mux4-121-XOR.v",
"c1908-mux4-131.v",
"c1908-mux4-131-XOR.v",
"c1908-mux4-141.v",
"c1908-mux4-141-XOR.v",
"c1908-mux4-151.v",
"c1908-mux4-151-XOR.v",
"c1908-mux4-161.v",
"c1908-mux4-161-XOR.v",
"c1908-mux4-171.v",
"c1908-mux4-171-XOR.v",
"c1908-mux4-181.v",
"c1908-mux4-181-XOR.v",
"c1908-mux4-191.v",
"c1908-mux4-191-XOR.v",
"c1908-mux4-201.v",
"c1908-mux4-201-XOR.v"
    ]

with open("time_info_1908", "a") as outfile:
    outfile.write("#Number of gate                  #BASE                 #XOR\n")

# run simp and it will generate the finalsolu and iterationinfo
for i in cam_list:
    cmmd = "/usr/bin/time -v -o temp-time ./minisat-incre-simp decam-incre c1908-abcmap-fmt.v " + i
    call(cmmd, shell = True)
# rename iterationinfo
    os.rename("increIterationInfo.log", i.strip(".v") + "-interationInfo.dat")

# check EC and import to a txt

    res = EC("c1908-abcmap-fmt.v", i, "finalSolu.log")
    if (res == 1):
        content = "Circuit: " + i + " is CORRECT!\n"
    elif (res == 0):
        content = "Circuit: " + i + " is WRONG!\n"
        break
    else:
        content = "Circuit: " + i + " is BUG!\n"
        break
    with open("EC_result.txt", "a") as output:
        output.write(content)


    with open("temp-time", "r") as infile:
        timeline = infile.read().split("\n")
    if "XOR" not in i:
        with open("time_info_1908", "a") as outfile:
            outfile.write(i.strip("c1908-mux4-").strip(".v") + "              ")
        for line in timeline:
                if "User time (seconds):" in line:
                    time_info = line.replace("User time (seconds):", "")
                    break

        with open("time_info_1908", "a") as outfile:
            outfile.write(time_info + "              ")
    else:
        for line in timeline:
            if "User time (seconds):" in line:
                time_info = line.replace("User time (seconds):", "")
                break

        with open("time_info_1908", "a") as outfile:
            outfile.write(time_info + "\n")
    os.remove("temp-time")
