__author__ = 'xiangyuzhang'
from subprocess import call
from EC_lib import EC
with open("time_info", "a") as outfile:
    outfile.write("#Number of gate                  #BASE                 #XOR\n")

cmmd_base = "/usr/bin/time -v -o temp-time ./minisat-incre-simp decam-incre c7552-abcmap-fmt.v "
Num_XOR = 20
# each time run original graduatelly and XOR one by one

c7552 = [
        'c7552-mux4-11.v',
        'c7552-mux4-21.v',
        'c7552-mux4-31.v',
        'c7552-mux4-41.v',
        'c7552-mux4-51.v',
        'c7552-mux4-61.v',
        'c7552-mux4-71.v',
        'c7552-mux4-81.v',
        'c7552-mux4-91.v',
        'c7552-mux4-101.v',
        'c7552-mux4-111.v',
        'c7552-mux4-121.v',
        'c7552-mux4-131.v',
        'c7552-mux4-141.v',
        'c7552-mux4-151.v',
        'c7552-mux4-161.v',
        'c7552-mux4-171.v',
        'c7552-mux4-181.v',
        'c7552-mux4-191.v',
        'c7552-mux4-201.v']

for original in c7552:
    cmmd_original = cmmd_base + original
    cmmd_XOR_1 = "python XOR_Cam_partial.py c7552-mux4-1.v " + str(Num_XOR)
    Num_XOR += 20
    Xor_circuit = "c7552-mux4-1-" + str(Num_XOR)
    cmmd_XOR_2 = cmmd_base + Xor_circuit + '.v'

    #Now I should run check EC and collect the time info and store in file

    #Run
    call(cmmd_original, shell = True)
    #Check
    res = EC("c7552-abcmap-fmt.v", original, "finalSolu.log")
    if (res == 1):
        content = "Circuit: " + original + " is CORRECT!\n"
    elif (res == 0):
        content = "Circuit: " + original + " is WRONG!\n"
    else:
        content = "Circuit: " + original + " is BUG!\n"
    with open("EC_result.txt", "a") as output:
        output.write(content)
    #write gate number
    gate_number = original.strip("c7552-mux4-").strip(".v")
    with open("time_info", "a") as outfile:
        outfile.write(gate_number + "                   ")
     #time info
    with open("temp-time", "r") as infile:
        timeline = infile.read().split("\n")
    for line in timeline:
        if "User time (seconds):" in line:
            time_info = line.replace("User time (seconds):", "")
            break
    with open("time_info", "a") as outfile:
        outfile.write(time_info + "                   ")

    #generate XOR circuit
    call(cmmd_XOR_1, shell = True)


    #Run
    call(cmmd_XOR_2, shell = True)
    #Check
    res = EC("c7552-abcmap-fmt.v", Xor_circuit, "finalSolu.log")
    if (res == 1):
        content = "Circuit: " + Xor_circuit + " is CORRECT!\n"
    elif (res == 0):
        content = "Circuit: " + Xor_circuit + " is WRONG!\n"
    else:
        content = "Circuit: " + Xor_circuit + " is BUG!\n"
    with open("EC_result.txt", "a") as output:
        output.write(content)
     #time info
    with open("temp-time", "r") as infile:
        timeline = infile.read().split("\n")
    for line in timeline:
        if "User time (seconds):" in line:
            time_info = line.replace("User time (seconds):", "")
            break
    with open("time_info", "a") as outfile:
        outfile.write(time_info)

