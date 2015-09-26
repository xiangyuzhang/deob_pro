__author__ = 'xiangyuzhang'


from subprocess import call
'''
camlist = ["c499-mux4-1.v", "c499-mux4-11.v", "c499-mux4-21.v", "c499-mux4-31.v", "c499-mux4-41.v", "c499-mux4-51.v",
           "c499-mux4-61.v", "c880-mux4-1.v", "c880-mux4-11.v","c880-mux4-21.v", "c880-mux4-31.v","c880-mux4-41.v",
           "c880-mux4-51.v", "c880-mux4-61.v"]

camlist_xor = ["c499-mux4-1-XOR.v", "c499-mux4-11-XOR.v", "c499-mux4-21-XOR.v", "c499-mux4-31-XOR.v", "c499-mux4-41-XOR.v", "c499-mux4-51-XOR.v",
           "c499-mux4-61-XOR.v", "c880-mux4-1-XOR.v", "c880-mux4-11-XOR.v","c880-mux4-21-XOR.v", "c880-mux4-31-XOR.v","c880-mux4-41-XOR.v",
           "c880-mux4-51-XOR.v", "c880-mux4-61-XOR.v"]
'''

camlist = ["c880-mux4-1.v", "c880-mux4-11.v","c880-mux4-21.v", "c880-mux4-31.v","c880-mux4-41.v",
           "c880-mux4-51.v", "c880-mux4-61.v"]

camlist_xor = ["c880-mux4-1-XOR.v", "c880-mux4-11-XOR.v","c880-mux4-21-XOR.v", "c880-mux4-31-XOR.v","c880-mux4-41-XOR.v",
           "c880-mux4-51-XOR.v", "c880-mux4-61-XOR.v"]
'''
for i in camlist[0:7]:
    cmmd_original = "python decam-v5-cmmdline.py c499-abcmap-fmt.v " + i + " -o " + i.strip(".v") + ".dat"
    call(cmmd_original, shell=True)
    print "finish " + i
'''
for i in camlist:
    cmmd_original = "python decam-v5-cmmdline.py c880-abcmap-fmt.v " + i + " -o " + i.strip(".v") + ".dat"
    call(cmmd_original, shell=True)
    print "finish " + i
'''
for i in camlist_xor[0:7]:
    cmmd_original = "python decam-v5-cmmdline.py c499-abcmap-fmt.v " + i + " -o " + i.strip(".v") + ".dat"
    call(cmmd_original, shell=True)
    print "finish " + i
'''
for i in camlist_xor:
    cmmd_original = "python decam-v5-cmmdline.py c880-abcmap-fmt.v " + i + " -o " + i.strip(".v") + ".dat"
    call(cmmd_original, shell=True)
    print "finish " + i