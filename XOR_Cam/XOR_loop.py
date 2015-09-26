__author__ = 'xiangyuzhang'
from subprocess import call
import os

camlist = ["c3540-mux4-1.v",
"c3540-mux4-11.v",
"c3540-mux4-21.v",
"c3540-mux4-31.v",
"c3540-mux4-41.v",
"c3540-mux4-51.v",
"c3540-mux4-61.v",
"c3540-mux4-71.v",
"c3540-mux4-81.v",
"c3540-mux4-91.v",
"c3540-mux4-101.v",
"c3540-mux4-111.v",
"c3540-mux4-121.v",
"c3540-mux4-131.v",
"c3540-mux4-141.v",
"c3540-mux4-151.v",
"c3540-mux4-161.v",
"c3540-mux4-171.v",
"c3540-mux4-181.v",
"c3540-mux4-191.v",
"c3540-mux4-201.v"]
for i in camlist:
    os.remove(i.strip(".v") + "-XOR.v")
    camd = "python XOR_Cam.py " + i
    call(camd, shell = True)